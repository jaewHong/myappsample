#!/usr/bin/env python3
import datetime

if __name__ == '__main__':
    print("user name:",end='')
    username = input()
    date = datetime.datetime.now()
    print("Hello {0}! Today is [{1}/{2}/{3}].".format(username,date.month,date.day,date.year))
