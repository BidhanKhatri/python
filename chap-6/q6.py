#  Write a program to calculate the grade of a student from his marks from the following scheme: 
# 90 – 100 => Ex 
# 80 – 90 => A 
# 70 – 80 => B 
# 60 – 70  =>C 
# 50 – 60 => D 
# <50 => F

mark = int(input("Enter you mark to find you grade: "))

if(mark > 90 and mark <= 100 ):
    print("Grade: Ex")
elif(mark > 80 and mark <= 90):
    print("Grade: A")    
elif(mark > 70 and mark <= 80):
    print("Grade: B")    
elif(mark > 60 and mark <= 70):
    print("Grade: C")    
elif(mark > 50 and mark <= 60):
    print("Grade: D")
elif(mark < 50 ):
    print("Grade: F")       