player = input("do you want to play a quiz game? ")
if player.lower() != "yes":
    quit()
score = 0;

answer = input("what does cpu stand for? ")
if answer.lower() == "central processing unit":
    print("correct")
    score += 1
else:
    print("incorrect")

answer = input("what does gpu stand for? ")
if answer.lower() == "graphics processing unit":
    print("correct")
    score += 1
else:
    print("incorrect")

answer = input("what does ram stand for? ")
if answer.lower() == "random access memory":
    print("correct")
    score += 1
else:
    print("incorrect")

answer = input("what does psu stand for? ")
if answer.lower() == "power supply":
    print("correct")
    score += 1
else:
    print("incorrect")

print("you got "+str(score)+" questions correct")
