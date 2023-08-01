from time import *
import random as r
##function of functionality
def mistake(parTest,userTest):
    error = 0
    for i in range(len(parTest)):
        try:
            if parTest[i]!=userTest[i]:
                error += 1
        except :
            error+=1
    return error
def speed_time(time_s,time_e,userInput):
    time_delay = time_e - time_s
    time_R = round(time_delay,2)
    speed = len(userInput) / time_R
    return round(speed)
test_str = ["Welcome to the 1 minute typing test program to check your real typing speed and accuracy",
            "Our one minute typing speed test application was developed to provide free and most accurate",
            "typing test service to our visitors.","We also have several typing test application to practice",
            "typing and check your typing skill. We believe accuracy is more important than speed.",
            "That's why we provide a complete result of your typing test skill, which includes the accuracy rate.",
            "Nowadays, typing is an essential skill for students and office workers.",
            "And that's why everyone should learn typing and achieve a good typing speed."]

test1 = r.choice(test_str)
print("*********Typing Speed***********")
print(test1)
print()
time_1 = time()
userInput = input("Start typing :")
time_2 = time()
print('speed : ', speed_time(time_1,time_2,userInput),"w\sec")
print("You write : ",userInput)
print('error : ', mistake(test1,userInput))





