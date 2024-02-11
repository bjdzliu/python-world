#!/usr/bin/env python3
"""
Example:
given input of year=2016, month=1, day=3.
The function should return 3 as the date 2016-01-03 is the 3rd day of the year 2016.

"""
def dayOfYear(year,month,day):
    #verify the month and year is valid
    if month<=0 or month>12 or year <=0 :
        return 'month or year is out of index'
    elif month%1==0 and year%1==0 and day%1==0:
        pass
    else:
        return 'include not int'

    x = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    D,i=day,0

    #leap year
    if (year%4==0 and year%100!=0) or (year%400==0) :
        ### set Feb 29 day
        x[1] = 29
        ### verify day is valid
        if day <= 0 or day > x[month - 1] :
            print("your input day is out of index")
            return ''
        ### if is Jan , directly return day
        if month == 1: return D
        ### Feb=jan+D -- > x[0]+D ;Mar=Jan+Feb+D --> x[0]+x[1]+D
        while i+1<month :
            D+=x[i]
            i+=1
        return D
    else:
        x[1] = 28
        ### verify day is valid
        if day <= 0 or day > x[month - 1] :
            print("your input day is out of index")
            return ''
        ### if is Jan , directly return day
        if month == 1: return D
        while i+1<month :
            D+=x[i]
            i+=1
        return D

if __name__=='__main__':
    print(dayOfYear(1984,3,1))
