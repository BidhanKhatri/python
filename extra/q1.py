#Write a program that:
# Prints each student’s average grade
# Finds the student with the highest average.

students = {
    "Alice": {"age": 20, "grades": [85, 90, 92]},
    "Bob": {"age": 22, "grades": [70, 88, 95]},
    "Charlie": {"age": 19, "grades": [100, 100, 100]}
}

key_el = students.keys()
value_el = students.values()


def find_avg(students, keys, values):

    highest = {}

    for name in keys:
        # print(name)
        total_sum = sum(students[name].get("grades"))

        avg = total_sum / (len(keys))
        print(f"Avarage marks of {name} is {avg} ")

        print(" ")

        highest.update({name: avg })

    top_student = max(highest, key=highest.get)
    print(f"Top student: {top_student} with {highest[top_student]:.2f}")


find_avg(students, key_el, value_el)       

    
       
        

