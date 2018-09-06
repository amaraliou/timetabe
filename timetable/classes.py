from icalendar import Calendar, Event
from datetime import datetime, timedelta, tzinfo
import dateutil
import json
import pytz
import re

LONDON = pytz.timezone('Europe/London')
DAYS = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
EMPTYTABLE = [[''] + DAYS] + [[str((datetime(2018, 9, 10, 9, 0, 0, 0, tzinfo = None) + timedelta(hours = i)).time())] + ['' for i in range(5)] for i in range(9)]
DAYSTOINT = dict(zip(DAYS, [1,2,3,4,5]))
INTODAYS = dict(zip([0,1,2,3,4], DAYS))
LONGTOSHORT = {'Algs & Data Structures 2': 'ADS2',
               'Java Programming 2': 'JP2',
               'Web App Development 2': 'WAD2',
               'Alg Foundations 2': 'AF2'}
HOURSTOINT = {str((datetime(2018, 9, 10, 9, 0, 0, 0, tzinfo = None) + timedelta(hours = i)).time()): i + 1 for i in range(9)}

class iCal:

    def __init__(self, icsfilepath):
        self.calobject = Calendar.from_ical(open(icsfilepath, 'rb').read())

    def get_calobject(self):
        return self.calobject

    def geteventdetails(self, eventobject):
        self.slot = Slot(INTODAYS[eventobject['dtstart'].dt.weekday()],
                         eventobject['dtstart'].dt.replace(tzinfo = pytz.utc),
                         eventobject['dtend'].dt.replace(tzinfo = pytz.utc),
                         str(eventobject['summary']),
                         str(eventobject['location']),
                         str(eventobject['description']))
        return self.slot

    #Serializable list of events
    def getallevents(self):
        self.events = []
        for event in self.calobject.walk('vevent'):
            self.details = self.geteventdetails(event)
            self.events.append(self.details.get_slot())
        return self.events

    #Serializable dictionary of events by date
    def getalleventsbydate(self):
        self.es = self.getallevents()
        self.eventsbydate = {}
        self.eventsbydate = {d['date']: [] for d in self.es if not d['date'] in self.eventsbydate}
        for ev in self.es:
            self.date = ev['date']
            ev.__delitem__('date')
            self.eventsbydate[self.date].append(ev)
        return self.eventsbydate
    
    #Serializable dictionary of events by week
    def getalleventsbyweek(self):
        self.es = self.getallevents()
        self.eventsbyweek = {}
        self.eventsbyweek = {d['week']: [] for d in self.es if not d['date'] in self.eventsbyweek}
        for ev in self.es:
            self.week = ev['week']
            ev.__delitem__('week')
            self.eventsbyweek[self.week].append(ev)
        return self.eventsbyweek

    def jsonevents(self, filepath, eventfunction):
        self.filejson = open(filepath, 'w+')
        self.jsondata = eventfunction()
        json.dump(self.jsondata, self.filejson)
        return


class Timetable:

    def __init__(self):
        self.timetable = [[''] + DAYS] + [[str((datetime(2018, 9, 10, 9, 0, 0, 0, tzinfo = None) + timedelta(hours = i)).time())] + ['' for i in range(5)] for i in range(9)]
    
    def prettyprint(self):
        for i in self.timetable:
            if not i[1::] == [''] * 5:
                print("{:<10} {:<20} {:<17} {:<17} {:<17} {:<17}\n".format(*i))

    def insert_slot(self, slot):
        self.x = DAYSTOINT[slot['weekday']]
        self.y = HOURSTOINT[slot['start']]
        if not (HOURSTOINT[slot['end']] - HOURSTOINT[slot['start']]) >= 2:
            self.timetable[self.y][self.x] = slot['title'] + ' ' + slot['type']
        else:
            self.timetable[self.y][self.x] = slot['title'] + ' ' + slot['type']
            self.timetable[self.y + 1][self.x] = slot['title'] + ' ' + slot['type']
        return

    def emptytable(self):
        self.timetable = [[''] + DAYS] + [[str((datetime(2018, 9, 10, 9, 0, 0, 0, tzinfo = None) + timedelta(hours = i)).time())] + ['' for i in range(5)] for i in range(9)]
        return


class Slot:

    def __init__(self, weekday = "", start = datetime.now(), end = datetime.now(), title = "", location = "", desc = ""):
        self.weekday = weekday
        self.week = get39weeks().index(getweek(start.date()))
        self.starts_at = start.astimezone(LONDON).time()
        self.ends_at = end.astimezone(LONDON).time()
        self.date = start.date()
        self.temptitle = re.findall('Level 2 Enrolment|Maths 2A|Maths 2B|Maths 2C|Maths 2D|Maths 2E|Maths 2F|OOSE2|NOSE 2|Algs & Data Structures 2|Java Programming 2|Alg Foundations 2|Web App Development 2', desc)[0]
        try:
            self.title = LONGTOSHORT[self.temptitle]
        except:
            self.title = self.temptitle
        self.location = location
        self.desc = desc
        try:
            self.lecturetype = re.findall('Lecture|Seminar|Laboratory|Tutorial', desc)[0]
        except:
            self.lecturetype = None

    def get_slot(self):
        self.ks = ['weekday', 'week', 'start', 'end', 'date', 'title', 'location', 'desc', 'type']
        self.vs = [self.weekday, self.week, str(self.starts_at), str(self.ends_at), str(self.date), self.title, self.location, self.desc, self.lecturetype]
        return dict(zip(self.ks, self.vs))

#Get the start and the end of a week given a date
def getweek(date):
    start = date - timedelta(days=date.weekday())
    end = start + timedelta(days=6)
    return start, end

#Get the 39 weeks of the academic year
def get39weeks():
    return [getweek(datetime(2018, 9, 10, 0, 0, 0, 0, tzinfo = LONDON).date() + timedelta(days = i*7)) for i in range(40)]

#Parse a date string and convert it to datetime object
def dateparser(datestring):
    return dateutil.parser.parse(datestring)


if __name__ == '__main__':
    pass