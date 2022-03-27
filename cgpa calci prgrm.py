

#CGPA CALCULATOR PROGRAM
import sys

print("*** CGPA CALCULATOR **** \n")
x=input("---ENTER YOUR REGULATION :---")
y=input("Enter your department name:")

sem=int(input(" ENTER THE NUMBER OF SEMESTERS COMPLETED:"))
finalgpa=[]
flag=0
for a in range(0,sem):
    print("\n**Entering the marks  of Semester :\n",(a+1))
    n=int(input("\nEnter no.of Subjects: "))
    marks=[]
    credit=[]
    for i in range(n):
        print("\nEnter the ",(i+1),end="th subject marks: ")
        x=int(input())
        marks.append(x)
    for i in range(n):
        print("\nEnter the ",(i+1),end="th subject credits: ")
        x=int(input())
        credit.append(x)
    GPA=[]
    Grade=[]
    for i in range(len(marks)):
        if(marks[i]<=100 and marks[i]>=90):
            GPA.append(10)
            Grade.append("O")  #OUTSTANDING
        elif(marks[i]<90 and marks[i]>=80):
            GPA.append(9)
            Grade.append("A+")  #EXCELLANT
        elif(marks[i]<80 and marks[i]>=70):
            GPA.append(8)
            Grade.append("A")  #VERY GOOD
        elif(marks[i]<70 and marks[i]>=60):
            GPA.append(7)
            Grade.append("B+") #good
        elif(marks[i]<60 and marks[i]>=50):
            GPA.append(6)
            Grade.append("B")  #average
        else:
            GPA.append(0)
            Grade.append("RA")
    print("Your Grade in Respective Subjects are....")       
    for i in range(n):
        print("Grade in ",(i+1),"th Subject is :",Grade[i])
    gpa=0
    for i in range(n):
        if(marks[i]<50):
            print("Since You have a Marks Less than 50 / Grade='RA' you are not eligible to caluclate the GPA")
            sys.exit()              
    for i in range(n):
        gpa=gpa+(GPA[i]*credit[i])
    finalgpa.append(gpa)
    print("\n ___Your GPA is :_______"+"{:.2f}".format(finalgpa[a]/sum(credit)))
    flag=flag+sum(credit)
print("\n !!!! Your CGPA is : !!!!!!!!!! "+("{:.2f}".format(sum(finalgpa)/flag))) 



