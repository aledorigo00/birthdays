#! /usr/bin/env python3
from birthdays import return_birthday
from birthdays import birthday_month
from birthdays import birthday_day
import argparse
import csv


parser = argparse.ArgumentParser()
parser.add_argument("name", help="Insert the name to retrieve its birthday")
parser.add_argument("surname", help="Insert the surname to retrieve its birthday")
parser.add_argument("--month","-m",action="store_true", help="Input this flag to obtain only the month")
parser.add_argument("--day","-d",action="store_true", help="Input this flag to obtain only the day")
args = parser.parse_args()

'''
if len(sys.argv) > 1:
    my_argv= sys.argv[1]+" "+sys.argv[2]
    to_print = return_birthday(my_argv)
else:
    print('You have to rinput a name')
    exit()

print("The name of this program is {}".format(sys.argv[0]))
print("The birthday of {} is {}".format(my_argv,to_print))

'''
completeName = args.name+" "+args.surname
if args.month:
	to_print = birthday_month(completeName)
	print("The birthday month of {} is {}".format(completeName,to_print))
elif args.day:
	to_print = birthday_day(completeName)
	print("The birthday day of {} is {}".format(completeName,to_print))
else:	
	to_print = return_birthday(completeName)
	print("The birthday  of {} is {}".format(completeName,to_print))


