a=input("Enter Your name: ")
print("Hey",a,"your Questions are here each carries 10 points \n All the best..! \n")  
s=0
c=0
options=["a.Assam","b.Maharashtra","c.Gujrat","d.Rajasthan","a.Narendra Modi","b.Drupadi Murmu","c.Nirmala Sitaraman","d.Ramnath Kovind","a.ISRO","b.NASA","c.CIA","d.SpaceX","a.Indian","b.Artic","c.Pacific","d.Atlantic","a.Jordan & Sudan","b.India & Pakisthan","c.Jordan & Israel","d.UAE & Egypt","a.Japan","b.New Zealand","c.Fiji","d.China","a.Asia","b.Europe","c.Africa","d.North America","a.India","b.Sri Lanka","c.Thailand","d.Malaysia","a.Iceland","b.Norway","c.Finland","d.Switzerland","a.Finland","b.Borneo","c.Sumatra","d.Greenland"]
print("1] Where is Statue of Unity Situated ?\n")
q1=input(options[0:4])
if(q1=="c"):
    s=s+10
    c=c+1
    print("Correct answer \nYou have scared 10 points\n")
else:
    print("Wrong Answer\n")
print("2] Who is the President of India ?\n")
q2=input(options[4:8])
if(q2=="b"):
    s=s+10
    c=c+1
    print("Correct answer \nYou have scared 10 points\n")
else:
    print(" Wrong Answer\n")
print("3] Name of the Indian Space Agency is:\n")
q3=input(options[8:12])
if(q3=="a"):
    s=s+10
    c=c+1
    print("Correct answer \nYou have scared 10 points\n")
else:
    print("Wrong Answer\n")
print("4] Which is the smallest Ocean in the world ?\n")
q4=input(options[12:16])
if(q4=="b"):
    s=s+10
    c=c+1
    print("Correct answer \nYou have scared 10 points\n")
else:
    print("Wrong Answer\n")
print("5] Dead Sea is located between which two counties:\n")
q5=input(options[16:20])
if(q5=="c"):
    s=s+10
    c=c+1
    print("Correct answer \nYou have scared 10 points\n")
else:
    print("Wrong Answer\n")
print("6] Which Country is know as the Land of Rising Sun ?")
q6=input(options[20:24])
if(q6=="a"):
    s=s+10
    c=c+1
    print("Correct answer \nYou have scared 10 points\n")
else:
    print("Wrong Answer\n")
print("7] Which Continent has the highest number of Countries ?\n")
q7=input(options[24:28])
if(q7=="a"):
    s=s+10
    c=c+1
    print("Correct answer \nYou have scared 10 points\n")
else:
    print("Wrong Answer\n")
print("8] In Which Country, White Elephant is found ?")
q8=input(options[28:32])
if(q8=="c"):
    s=s+10
    c=c+1
    print("Correct answer \nYou have scared 10 points\n")
else:
    print("Wrong Answer\n")
print("9] Which Country is known as the Land of 1000 lakes ?")
q9=input(options[32:36])
if(q9=="c"):
    s=s+10
    c=c+1
    print("Correct answer \nYou have scared 10 points\n ")
else:
    print("Wrong Answer\n")
print("10] Which is the biggest island in the world ?")
q10=input(options[36:40])
if(q10=="d"):
    s=s+10
    c=c+1
    print("Correct answer \nYou have scared 10 points\n")
else:
    print("Wrong Answer\n")
print(a,"you have Successfully completed this Quiz\n Your Result is as follows\n Questions Attempted:10\n Correct answers:",c,"\nTotal score",s,"\n")
if(c>=50):
    print("CONGRATULATIONS\n")
elif(c>0 and c<50):
    print("GOOD\n")
elif(c==0):
    print("Better luck next time\n")