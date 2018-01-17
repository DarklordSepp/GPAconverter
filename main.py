import csv

def convert(score):
    score = score
    # Don't forget to cast it as a float.. and then a string again when printing. :(
    score = float(score / 800)
    score = score * 4
    print("Your High school equivalent GPA is: " + str(score) + "!")
    dataOut(str(score) + ' Equivalent GPA.')


def dataOut(pas_one):
    data = pas_one
    file = open('EGPA.txt', 'w+')
    file.write(data)
    file.close()


# So cordial.
mathScore = input("First enter your Math score: ")
ssScore = input("Now Social Studies: ")
langScore = input("and Language arts: ")
sciScore = input("finally your Science score: ")




# This wouldn't be needed in Java, but Python doesn't seem to like typecasting.
# There really has to be a better way.
mathScore = int(mathScore)
ssScore = int(ssScore)
langScore = int(langScore)
sciScore = int(sciScore)
total = mathScore + ssScore + langScore + sciScore
tOut = total
total = str(total)


print("That's " + total + ". Congratulations!")

convert(tOut)

# Java > Python but I'm learning it anyway. I suppose this is my first python program.
# I made this to figure out my gpa so I'd know my chances of getting into the computer science program
# I wan't to earn my degree from.

# TODO make a gui
