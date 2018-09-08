from classes import iCal

calendar = iCal('timetable/data/uogtimetable.ics')
calendar.jsonevents('timetable/data/lecturesbydate.json',
                    calendar.getalleventsbydate)
calendar.jsonevents('timetable/data/lecturesbyweek.json',
                    calendar.getalleventsbyweek)