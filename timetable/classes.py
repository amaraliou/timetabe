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

    def __init__(self):
        pass

#Get the start and the end of a week given a date
def getweek(date):
    pass

#Get the 39 weeks of the academic year
def get39week():
    pass

#Parse a date string and convert it to datetime object
def dateparser(datestring):
    pass


if __name__ == '__main__':
    pass