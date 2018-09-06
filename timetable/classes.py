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

    def __init__(self):
        pass


class Timetable:

    def __init__(self):
        pass


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
    pass

#Get the 39 weeks of the academic year
def get39weeks():
    pass

#Parse a date string and convert it to datetime object
def dateparser(datestring):
    pass


if __name__ == '__main__':
    pass