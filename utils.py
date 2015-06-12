# Optimum API
# Copyright 2015 Jordan Facibene

import datetime

def genDatetimeObjFromTimestring(timestring):
    year = int(timestring[2])
    month = int(timestring[4])
    day = int(timestring[3])
    hour = int(timestring[5])
    minute = int(timestring[6])
    second = 0
    obj = genDatetimeObj(year,
                         month,
                         day,
                         hour,
                         minute,
                         second)
    return obj

def genDatetimeObj(year,
                   month,
                   day,
                   hour,
                   minute,
                   second):
    obj = datetime.datetime(int(year),
                            int(month),
                            int(day),
                            int(hour),
                            int(minute),
                            int(second))
    return obj

def genDatetimeObjFromScheduled(timestring):
    timestring = timestring.split(" ")
    date = timestring[0].split("-")
    time = timestring[1]
    month = date[0]
    day = date[1]
    year = "20" + date[2]
    hour = time[:2]
    minute = time[2:]
    second = 0
    obj = genDatetimeObj(year,
                         month,
                         day,
                         hour,
                         minute,
                         second)
    return obj

def genDatetimeObjFromReleaseDate(release_date):
    release_date = release_date.split(" ")
    date = release_date[0].split("-")
    time = release_date[1].split(":")
    year = date[0]
    month = date[1]
    day = date[2]
    hour = time[0]
    minute = time[1]
    second = time[2]
    obj = genDatetimeObj(year,
                         month,
                         day,
                         hour,
                         minute,
                         second)
    return obj
def adjustTimeFromGMT(datetime_obj):
    datetime_obj = datetime_obj - datetime.timedelta(hours=4)
    return datetime_obj

def addSeconds(datetime_obj, seconds):
    datetime_obj = datetime_obj + datetime.timedelta(seconds=seconds)
    return datetime_obj

def genRecordRequestTime(datetime_obj):
    return datetime_obj.strftime("%Y%m%d%H%M00")

def genTimestamp():
    """Generates a timestamp in a format accepted by Cablevision's servers"""
    now = datetime.datetime.now()
    timestamp = now.strftime("%A, %B %-d, %y %-I:%M:00 %p -04:00")
    return timestamp

def genTimestamp2():
    now = datetime.datetime.now()
    timestamp = now.strftime("%m/%d/%Y %I:%M:%S.%f %p")
    return timestamp

def genTimestamp3():
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%dT%H:%M:%S.%f0-04:00")
    return timestamp

def genTimestamp4():
    now = datetime.datetime.now()
    timestamp = now.strftime("%")

def getDate():
    return datetime.datetime.now().date()

def genEventTimestamp():
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%dT%H:%M:%S.%f0-04:00")
    return timestamp

def formatXMLValue(value):
    if value:
        return "<value>{}</value>".format(value)
    else:
        return "<value />"

def parseSearchTime(string):
    timestring = string.split(":")
    year = int(timestring[2])
    month = int(timestring[4])
    day = int(timestring[3])
    hour = int(timestring[5])
    minute = int(timestring[6])
    second = 0
    obj = datetime.datetime(year,
                            month,
                            day,
                            hour,
                            minute,
                            second)
    duration = int(timestring[7])
    return (obj, duration)

