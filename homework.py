#https://chatgpt.com/s/t_6a7dd5bbe2e48191919bab9fa66dbd54

def calculate_avg_marks(marks):
    total=0
    num_sub=len(marks)
    for i in range(num_sub):
        total+=marks[i] 
        avg_of_marks=total/num_sub
    return total,avg_of_marks

check_pass_fail = lambda avg: "PASS" if avg >= 50 else "FAIL"

def calculate_grade(avg_score):
    if 90<=avg_score<=100:
        return "A+"
    elif 80<=avg_score<=89:
        return "A"
    elif 70<=avg_score<=79:
        return "B"
    elif 60<=avg_score<=69:
        return "C"
    elif 50<=avg_score<=59:
        return "D"
    else:
        return "F"
    
def grade_pattern(grade):
    if grade=="A+":
        return "*****"
    elif grade=="A":
        return "****"
    elif grade=="B":
        return "***"
    elif grade=="C":
        return "**"
    elif grade=="D":
        return "*"
    else:
        return "F"
def display_result(name,roll_no,course,subjects,marks,total,avg_of_marks,result_status,calculate_grade,pattern):
    def line():
        print("="*50)
    def greet():    
        print("-"*50)

    line()
    print("        RESULT     ")
    line()
    print(f"Name     :{name}")
    print(f"Roll No  :{roll_no}")
    print(f"Course   :{course}")
    greet()
    print("subject"+" "*15+"Marks")
    greet()

    for i in range(len(subjects)): 
        print(f"{subjects[i]}{' ' * 15}{marks[i]}")
    
    greet()
    print(f"Total         :{total}")
    print(f"Average       :{avg_of_marks}")
    print(f"Result        :{result_status}")
    print(f"Grade         :{calculate_grade}")
    print(f"Grade pattern :\n{pattern}")
    line()
    

def main():
    while True:
        print("=" * 50)
        print("       STUDENT RESULT ANALYZER       ")
        print("=" * 50)
        name=input("enter student name:")
        roll_no=input("Enter roll number:")
        course=input("enter course name:")
        print("enter marks for 5 subjects")
        subjects=["python","HTML","CSS","Javascript","Django"]
        marks=[]
        for i in range(len(subjects)):
            mark = float(input(f"Enter marks for {subjects[i]}: "))
            marks.append(mark)
    

    
        total,avg_of_marks=calculate_avg_marks(marks)
        result_status=check_pass_fail(avg_of_marks)
        student_grade=calculate_grade(avg_of_marks)
        pattern=grade_pattern(student_grade)

        display_result(name,roll_no,course,subjects,marks,total,avg_of_marks,result_status,student_grade, grade_pattern)


        choice=input("\nDo you want to enter another student? (yes/no):")
        if choice!="yes":
            print("\nThank you!")
            break
if __name__=="__main__":
        main()
 
   
