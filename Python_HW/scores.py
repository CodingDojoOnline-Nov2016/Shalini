def grades():

    for counter in range(1,11):
        score = int(raw_input("What is your score"))

        if (score <= 59):
            print score, "Your Grade is F"
        elif (score>59 and score<=69):
            print score, "Your Grade is D"
        elif (score<=79 and score>=70):
            print score, "Your Grade is C"
        elif (score>=80 and score<90):
            print "Your Grade is B"
        else:
            print score, "Your Grade is A"
    print "End of the program. Bye!"

print grades()
