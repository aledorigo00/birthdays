#! /usr/bin/env python3
from birthdays import return_birthday
import sys


if len(sys.argv) > 1:
    to_print = return_birthday(sys.argv[1])
else:
    print('You have to rinput a name')
    exit()

print("The name of this program is {}".format(sys.argv[0]))
print("The birthday of {} is {}".format(sys.argv[1],to_print))



