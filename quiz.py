#create a dictonary that contain true/false questions.


question1="ROUND 1:-\nQuestion 1:The atomic number for lithium is 17.\n(a)True\n(b)False\n"      #questions
question2="\nROUND 2:-\nQuestion 2:Pinocchio was Walt Disney's first animated feature film in full colour.\n(a)True\n(b)False\n"
question3="\nROUND 3:-\nQuestion 3:The national sport of India is Hockey.\n(a)True\n(b)False\n"
question4="\nROUND 4:-\nQuestion 4:Nepal is the only country in the world without the rectangular flag.\n(a)True\n(b)False\n"
question5="\nROUND 5:-\nQuestion 5:The world's largest island is Greenland.\n(a)True\n(b)False\n"

dict={question1:"b",question2:"b",question3:"a",question4:"a",question5:"a"}  #contains questions and answers

score=0

for i in dict:
    print(i)
    ans=input("Enter your answer: ")       #give the answer in lowercase
    if ans==dict[i]:
        print("Congratulations!!!!. Your answer is Correct")
        score=score+1
    else:
        print("Your answer is Incorrect.")

print("\nTotal Score Obtained:",score,"/ 5")
