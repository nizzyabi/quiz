from options import options
from options import correct_options
from questions import questions


user_name =input("Enter Your name: ")
print(f"Hey, {user_name},your Questions are here each carries 10 points \n All the best..! \n")  

score = 0
right_ans =0

for i in range(0, len(questions)):
    curr = str(i+1)
    print(questions[curr])
    for option in options[curr]:
        print(f"{option}", end=" ")
    print()
    ans = input()
    if (ans.lower() == correct_options[curr]):
        score += 10
        right_ans += 1
        print("Correct answer \nYou have scared 10 points\n")
    else:
        print("Oops!! Wrong Answer\n")



print(f'''{user_name} you have successfully completed this Quiz!\n 
Your Result is as follows =>\n 
Questions Attempted:10\n 
Correct answers: {right_ans} \n
Total score: {score}\n''')

if(score >= 50):
    print("CONGRATULATIONS\n")
elif(score > 0 and score < 50):
    print("GOOD\n")
elif(score == 0):
    print("Better luck next time\n")