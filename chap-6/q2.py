# Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user. 

sub1 = int(input("Enter marks of subject 1: "))
sub2 = int(input("Enter marks of subject 2: "))
sub3 = int(input("Enter marks of subject 3: "))

total_percentange = (( sub1 + sub2 + sub3) * 100 ) / 300

if((total_percentange >= 40) and (sub1 >= 33) and (sub2 >= 33) and (sub3 >= 33)):
    print(f"You are passed and you have got {total_percentange}%")
else:
    print(f"You are failed try again next year, you got {total_percentange}%")    