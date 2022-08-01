print('Welcome to the Name Generator\n')
import random, time, sys, string


def generat_name():
    letters_string = string.ascii_lowercase
    digitis_string = string.digits

    upper = string.ascii_uppercase

    digitis_list = []
    letters = []
    upper_list = []

    for letter in letters_string:
        letters.append(letter)

    for letter in upper:
        upper_list.append(letter)

    for digtis in digitis_string:
        digitis_list.append(digtis)

    vornamen = ['Copper', 'Elephant', 'Monkey', 'Coach', 'Cyan', 'Maroon', 'Big', 'Ben', 'Jonny', 'Pig']
    nachnahmen = ['Elephant', 'Goose', 'Sonka', 'Opossum', 'OSLEX', 'Brother', 'Ben', 'Big', 'Widsom']
    endings = ['™', '', '\=']

    def vor_nachnahme():
        vorname = random.choice(vornamen)
        nachnahme = random.choice(nachnahmen)
        end = random.choice(endings)

        if end == '\=':
            start = '=\\'

        else:
            start = ''

        while True:
            if vorname == nachnahme:
                nachnahme = random.choice(nachnahmen)

            else:
                break

        print(f'{start}{vorname} {nachnahme}{end}')

    def normal_name():
        name_list = []
        name = ''
        for x in range(2):
            name_list.append(random.choice(letters))


        name_list.append(random.choice(upper_list))

        for x in range(2):
            name_list.append(random.choice(digitis_list))

        name_list.append(random.choice(upper_list))

        for x in range(2):
            name_list.append(random.choice(letters))

        for letter in name_list:
            name = name + letter

        print(name)

    moeglichkeiten = ['vor_nachname', 'normal_name']

    step = random.choice(moeglichkeiten)
    if step == 'vor_nachname':
        vor_nachnahme()
    elif step == 'normal_name':
        normal_name()

    else:
        print('Error')

generat_name()

while True:
    nextStep = input('\nPress Enter for a new Name, type \'E\' to Exit the Programm: ')
    print()
    if nextStep == 'E' or nextStep == 'e':
        sys.exit()

    else:
        generat_name()