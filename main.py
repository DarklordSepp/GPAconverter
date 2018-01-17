import os
import platform


def setup():
    sys = platform.system().upper()
    print(sys)
    desktop_file = 'null'
    if sys == 'WINDOWS':
        desktop_file = os.path.expanduser('~\Desktop\EGPA.txt')
    elif 'OSX':
        desktop_file = os.path.expanduser('~\Desktop\EGPA.txt')
    elif 'LINUX':
        desktop_file = os.path.expanduser('~\Home\EGPA.txt')
    else:
        desktop_file = 'null'
    return desktop_file


df = setup()


def convert(score):
    score = score
    # Don't forget to cast it as a float.. and then a string again when printing. :(
    score = float(score / 800 * 4)
    data_out(str(score))


def data_out(data_in):
    str_cngrts = 'Your High school equivalent GPA is '
    data = str_cngrts + data_in
    if df is not 'null':
        file = open(df, 'w+')
        # file = open('EGPA.txt', 'w+')
        file.write(data)
        file.close()
        print(data)
    else:
        print(data)


def chequ(str):
    str = str
    i = True
    data = 'null'
    while i:
        try:
            data = int(input(str))
        except:
            # noinspection PyStatementEffect
            ValueError

        if type(data) is not int:
            print('Integers only. Try again.')
        elif data < 0:
            print('Scores must be between 0 and 200')
        elif data > 200:
            print('Scores must be between 0 and 200')
        else:
            i = False
    return data


# So cordial.
mathScore = chequ("First enter your Math score: ")
ssScore = chequ("Now Social Studies: ")
langScore = chequ("and Language arts: ")
sciScore = chequ("finally your Science score: ")
total = mathScore + ssScore + langScore + sciScore
tOut = total
total = str(total)

print("That's " + total + ". Congratulations!")
convert(tOut)

# Java > Python but I'm learning it anyway. I suppose this is my first python program.
# I made this to figure out my gpa so I'd know my chances of getting into the computer science program
# I wan't to earn my degree from.

# TODO make a gui
