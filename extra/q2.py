students = [
    {"name": "Alice", "scores": [88, 92, 79, 93]},
    {"name": "Bob", "scores": [70, 75, 80, 65]},
    {"name": "Charlie", "scores": [95, 100, 92, 98]}
]

def cal_avg(students):

    result = {}

    for item in students:
        std_name = item.get("name")
        std_score = item.get("scores")


        print(std_name)
        print(std_score)

        avg = round(sum(std_score) / len(std_score), 2)

        # print(avg)

        if avg >= 90 and avg <= 100:
            Grade = "A"
        elif avg >= 80: 
            Grade = "B"
        elif avg >= 70: 
            Grade = "C"
        elif avg >= 60: 
            Grade = "D"
        elif avg >= 50: 
            Grade = "E"
        else:
            Grade= "F"   

        result[std_name] = {"Grade": Grade, "Avg marks": avg}
        

    print(result)

cal_avg(students)
