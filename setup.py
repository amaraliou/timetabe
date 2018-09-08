from setuptools import setup

setup(
    name='timetable',
    version='1.0',
    py_modules=['timetable'],
    install_requires=[
        'Click',
        'icalendar', 
        'datetime', 
        'python-dateutil',
        'pytz', 
    ],
    entry_points='''
        [console_scripts]
        timetable=timetable.__main__:timetable
<<<<<<< HEAD
        '''
=======
        ''',
    include_package_data = True
>>>>>>> Setting up main and init and testing in virtual environment
)