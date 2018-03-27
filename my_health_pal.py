# HELLO MUZINDA HUB, I AM VICTOR KATSANDE. MY PROGRAM LETS PEOPLE ENTER THEIR PHYSICAL AND PHYSIOLOGICAL INFORMATION AND IT TELLS THEM IF THEY ARE NORMAL OR THEY NEED TO SEE A DOCTOR


# GREETINGS AND WELCOMING MESSAGE

print("Hello and welcome to My Health Pal, a program designed to monitor your health. ")


# ENTER YOUR NAME
def client_name(name):
    print("Please enter your name below. ")
    name = input("> ")
    return name
    print("Weldone {} just a few more steps and we are done".format(client_name))

# bmi parameters
def bmi(height, weight):
    print("What is your height? Please enter your height in meters below. ")
    height = int(input("> "))

    print("We need to know your weight too, please enter weight below in kilograms. ")
    weight = int(input("> "))
    return height,weight
    their_bmi = weight / height ** 2
    normal_bmi = range[18, 27]
    if their_bmi > normal_bmi:
        print("Oops {}, you have more weight for your height. You may need to start on an exercise regime.".format(client_name))
    elif their_bmi < normal_bmi:
        print("okay {}, Your weight is kinda lower for your height, we may need to put on some weight".format(client_name))
    else:
        print("Okie Dokie {}, Everything is normal for our weight to height ratio. keep it healthy".format(client_name))


# Pulse parameters
def pulse_for_age(age, pulse):
    print("How old are you? {} , please enter your age in digits. ".format(client_name))
    age = int(input("> "))
    print("""
    Okay {} , you are doing great. Now last thing we need your pulse..it's easy to do really,
    Just find the beat on your wrist and count how many beats you got in a minute
    """.format(client_name))
    pulse = int(input("> "))
    return age,pulse

    while age > 16:
        normal_pulse = range[60, 100]
    if pulse > normal_pulse:
        print("Oops, your pulse is above normal value, if it persists please see a doctor")
    elif pulse < normal_pulse:
        print("Oops, your pulse is below normal value, if it persists please see a doctor")
    else:
        print("Congrats, your pulse is normal. Keep it healthy")

    while age <= 16:
        normal_pulse = range[70, 100]
        if pulse > normal_pulse:
            print("Oops, your pulse is above normal value, if it persists please see a doctor")
        elif pulse < normal_pulse:
            print("Oops, your pulse is below normal value, if it persists please see a doctor")
        else:
            print("Congrats, your pulse is normal. Keep it healthy")
        continue


# QUIT APP
def quit():
    print("""
    okay, that's it for now.
    Enter V if you wish to start over
    Otherwise enter any other key to quit
    """)
    input("> ")
    return input
    if input == "V":
        client_name()
    else:
        print("BYE")




