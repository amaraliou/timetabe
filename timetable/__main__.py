from classes import Timetable, Slot, iCal
from datetime import datetime
import click
import json

try:
    calendar = iCal('timetable/data/uogtimetable.ics')
    coursesbyweek = calendar.getalleventsbyweek()
    coursesbydate = calendar.getalleventsbydate()
except:
    jsonweek = open('timetable/data/lecturesbyweek.json', 'r')
    jsondate = open('timetable/data/lecturesbydate.json', 'r')
    coursesbyweek = json.load(jsonweek)
    coursesbydate = json.load(jsondate)

@click.group()
def timetable():
    pass

@timetable.command()
@click.option('--date', default = str(datetime.now().date()), help = 'Timetable of the given YYYY-MM-DD date.')
def datetimetable(date):
    try:
        courses = coursesbydate[date]
        for course in courses:
            print('{:<8}-{:<8} {:<20}\n'.format(course['start'], course['end'], course['title'] + ' ' + course['type']))
    except:
        print('No courses on this day')
    return

@timetable.command()
@click.option('--week', default = 0, help = 'Timetable of given academic week.')
def weektimetable(week):
    try:
        t = Timetable()
        map(t.insert_slot, coursesbyweek[week])
        print('\n')
        t.prettyprint()
        t.emptytable()
    except:
        print('No courses this week')
    return

if __name__ == '__main__':
    timetable()