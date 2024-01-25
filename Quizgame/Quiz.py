print("Welcome to my computer quiz")
playing=input("Do you Want to paly?")
if playing.lower() !="yes":
    quit()
print("Okay! let's play :")
score=0
answer=input("what does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score+=1
else:
    print("Incoorect")
answer=input("what does gpu stand for? ")
if answer.lower() == "graphic processing unit":
    print("Correct!")
    score +=1
else:
    print("Incoorect")
answer=input("what does RAM stand for? ")
if answer.lower() == "random acess memory":
    print("Correct!")
    score +=1
else:
    print("Incoorect")
print("You got"+ str(score) +"question correct!")
print("You got"+ str((score/4)*100)+"%" )