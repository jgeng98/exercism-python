from datetime import date
import calendar
import numpy

class MeetupDayException(Exception):
    pass

def meetup(year, month, week, day_of_week):
    days_of_week = {"Sunday": 0, "Monday": 1, "Tuesday": 2, "Wednesday": 3, "Thursday": 4, "Friday": 5, "Saturday": 6}

    # create a calendar object where the first day of the week is Sunday
    cal = calendar.Calendar(6)

    # store the calendar for the given year and month in a numpy array 
    # ie. a list where the elements are lists consisting of the dates in each week (from Sunday to Monday)
    cal_array = numpy.array(cal.monthdayscalendar(year, month))
    print(cal_array)

    # create a list that only contains the dates on the specified day_of_week 
    # ie. if "Monday" is passed as an argument, then days_of_week_in_month consists of the dates of all Mondays in the given month + year 
    days_of_week_in_month = cal_array[:, days_of_week.get(day_of_week)]
    # remove any zeros in the list 
    days_of_week_in_month = numpy.delete(days_of_week_in_month, numpy.where(days_of_week_in_month==0))
    print(days_of_week_in_month)

    # dictionary to determine which element in days_of_week_in_month to access 
    # ie. "1st" week refers to the element in position 0 of days_of_week_in_month
    descriptors = {"1st": 0, "2nd": 1, "3rd": 2, "4th": 3, "5th": 4, "last": len(days_of_week_in_month)-1}

    # if the descriptor passed is "teenth", then we have to find the element in days_of_week_in_month that is in the range [13, 19]
    if week == "teenth":
        day = [day for day in days_of_week_in_month if day in range(13, 20)]
        day = int(''.join(map(str, day)))
    # if the date at position descriptors.get(week) throws an exception, then we raise a MeetupDayException error
    else:
        try:
            day = days_of_week_in_month[descriptors.get(week)]
        except:
            raise MeetupDayException("The date you're looking for does not exist.")

    return date(year, month, day)
