name=input("Enter your name :")
print("Welcome",name ,"to my quiz world!!")
playing=input("Are you excited to play?")

if playing.lower()!="yes":
    quit()

print("Okay! Let's play!!")
score=0

answer=input("What does CPU stands for?")
if answer.lower()=="central processing unit":
    print("correct")
    score+=1
else:
    print("Incorrect")    

answer=input("What does ROM stands for?")
if answer.lower()=="read only memory":
    print("correct")
    score+=1
else:
    print("Incorrect") 

answer=input("What does CU stands for?")
if answer.lower()=="control unit":
    print("correct")
    score+=1
else:
    print("Incorrect") 

answer=input("What does PC stands for?")
if answer.lower()=="program counter":
    print("correct")
    score+=1
else:
    print("Incorrect") 

answer=input("What does IR stands for?")
if answer.lower()=="instruction register":
    print("correct")
    score+=1
else:
    print("Incorrect") 

answer=input("What does MAR stands for?")
if answer.lower()=="memory address register":
    print("correct")
    score+=1
else:
    print("Incorrect") 

answer=input("What does GPU stands for?")
if answer.lower()=="graphics processing unit":
    print("correct")
    score+=1
else:
    print("Incorrect") 

answer=input("What does RAM stands for?")
if answer.lower()=="random acesss memory":
    print("correct")
    score+=1
else:
    print("Incorrect") 

answer=input("What does ps stands for?")
if answer.lower()=="power supply":
    print("correct")
    score+=1
else:
    print("Incorrect") 

answer=input("What does MBR stands for?")
if answer.lower()=="memory buffer register":
    print("correct")
    score+=1
else:
    print("Incorrect")

print(name,"You have got" +str((score/10)*100)+"%")
print("Congratulations!!",name)                 
