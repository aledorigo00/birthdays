birthdays = {
    'Albert Einstein': '03/14/1879',
    'Benjamin Franklin': '01/17/1706',
    'Ada Lovelace': '12/10/1815',
    'Donald Trump': '06/14/1946',
    'Rowan Atkinson': '01/6/1955',
    'Fabio Toffolo': '21/05/2000',
    'Alan Turing': '23/07/1890'}

def print_birthdays():
    print('Welcome to the birthday dictionary. We know the birthdays of these people:')
    for name in birthdays:
        print(name)

def return_birthday(name):
    if name in birthdays:
        date = birthdays[name]
        return date
    else:
        print('Sadly, we don\'t have {}\'s birthday.'.format(name))

def birthday_month(name):
    if name in birthdays:
        date = birthdays[name]
        date_elem = date.split('/')
        return date_elem[1]
    else:
        print('Sadly, we don\'t have {}\'s birthday.'.format(name))

def birthday_day(name):
    if name in birthdays:
        date = birthdays[name]
        date_elem = date.split('/')
        return date_elem[0]
    else:
        print('Sadly, we don\'t have {}\'s birthday.'.format(name))


#commento
#marco
#fabio
#risoluzione issue 1
#risoluzione issue 2
