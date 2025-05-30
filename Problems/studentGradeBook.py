"""
Write a Python program that does the following:

Takes input from the user for student names and their marks (in 3 subjects).

Stores the data in a dictionary.

Calculates the average marks for each student.

Finds and prints:

Student with the highest average

Student with the lowest average

All students with average >= 50 marked as "Pass", others "Fail"
"""

def main():
    num_students = int(input("Enter number of students: "))
    students = {}

    for i in range(num_students):
        name = input(f"Student {i+1} Name: ")
        marks = list(map(float, input(f"Enter 3 marks for {name}: ").split()))
        if len(marks) != 3:
            print("Please enter exactly 3 marks!")
            return
        average = sum(marks) / 3
        students[name] = {
            "marks": marks,
            "average": average,
            "status": "Pass" if average >= 50 else "Fail"
        }

    # Find topper and lowest
    topper = max(students, key=lambda x: students[x]['average'])
    lowest = min(students, key=lambda x: students[x]['average'])

    print("\nResults:")
    for name, data in students.items():
        print(f"{name} - Average: {data['average']:.2f} - {data['status']}")

    print(f"Topper: {topper}")
    print(f"Lowest: {lowest}")

if __name__ == "__main__":
    main()
