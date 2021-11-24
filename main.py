#! /usr/bin/env python3
from birthdays import return_birthday
from birthdays import birthday_month
from birthdays import birthday_day
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("name", help="Insert a name to retrieve its birthday")
parser.add_argument("--month","-m",action="store_true", help="Input this flag to obtain only the month")
parser.add_argument("--day","-d",action="store_true", help="Input this flag to obtain only the day")
args = parser.parse_args()


if args.month:
	to_print = birthday_month(args.name)
	print("The birthday month of {} is {}".format(args.name,to_print))
elif args.day:
	to_print = birthday_day(args.name)
	print("The birthday day of {} is {}".format(args.name,to_print))
else:	
	to_print = return_birthday(args.name)
	print("The birthday  of {} is {}".format(args.name,to_print))


