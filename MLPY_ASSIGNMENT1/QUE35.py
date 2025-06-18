# use elif to grade students based on score

score = int(input("Enter student score:"))

if(score > 90):
    print("Grade A+")
elif(score >= 80 or score < 90):
    print("Grade A")
elif(score >= 70 or score < 80):
    print("Grade B+")
elif(score >= 60 or score < 70):
    print("Grade B")
elif(score >= 50 or score < 60):
    print("Grade C+")
elif(score >= 40 or score < 50):
    print("Grade C")
elif(score >= 30 or score < 40):
    print("Grade D")
else:
    print("Fail!!")