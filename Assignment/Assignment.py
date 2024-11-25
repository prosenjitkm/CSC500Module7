room_numbers = {
    "CSC101": "3004",
    "CSC102": "4501",
    "CSC103": "6755",
    "NET110": "1244",
    "COM241": "1411"
}
instructors = {
    "CSC101": "Haynes",
    "CSC102": "Alvarado",
    "CSC103": "Rich",
    "NET110": "Burke",
    "COM241": "Lee"
}
meeting_times = {
    "CSC101": "8:00 a.m.",
    "CSC102": "9:00 a.m.",
    "CSC103": "10:00 a.m.",
    "NET110": "11:00 a.m.",
    "COM241": "1:00 p.m."
}

def display_course_info(course_number):
    if course_number in room_numbers:
        print(f"Course: {course_number}")
        print(f"Room Number: {room_numbers[course_number]}")
        print(f"Instructor: {instructors[course_number]}")
        print(f"Meeting Time: {meeting_times[course_number]}")
    else:
        print(f"Course {course_number} not found.")

def main():
    while True:
        course_number = input("Enter a course number (or 'q' to quit): ")
        if course_number.lower() == 'q':
            print("Goodbye!")
            break
        display_course_info(course_number)

if __name__ == "__main__":
    main()
