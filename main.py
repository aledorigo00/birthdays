#! /usr/bin/env python3
from birthdays import return_birthday
import sys


if len(sys.argv) > 1:
    my_argv= sys.argv[1]+" "+sys.argv[2]
    to_print = return_birthday(my_argv)
else:
    print('You have to rinput a name')
    exit()

print("The name of this program is {}".format(sys.argv[0]))
print("The birthday of {} is {}".format(my_argv,to_print))



