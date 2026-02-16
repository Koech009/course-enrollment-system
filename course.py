# ===============================
# COURSE ENROLLMENT SYSTEM
# ===============================

# Initial enrolled courses (SEQUENCE → LIST)
enrolled_courses = [
    "Math 101",
    "Computer Science 301",
    "Data Science 202"
]


# ===============================
# FEATURE 1: DISPLAY COURSES (READ)
# ===============================
def display_courses(courses):
    print("\n📚 Enrolled Courses:")
    if not courses:
        print("No courses enrolled.")
        return

    for i, course in enumerate(courses, start=1):
        print(f"{i}. {course}")


# ===============================
# FEATURE 2: ADD COURSE (CREATE)
# ===============================
def add_course(courses, new_course):
    if new_course not in courses:
        courses.append(new_course)
        print(f"\n✅ '{new_course}' added successfully.")
    else:
        print("\n⚠️ Course already enrolled.")


# ===============================
# FEATURE 3: REMOVE COURSE (DELETE)
# ===============================
def remove_course(courses, course_name):
    if course_name in courses:
        courses.remove(course_name)
        print(f"\n❌ '{course_name}' removed.")
    else:
        print("\n⚠️ Course not found.")


# ===============================
# FEATURE 4: FILTER COURSES
# (LIST COMPREHENSION)
# ===============================
def filter_courses(courses, keyword):
    filtered = [
        course for course in courses
        if keyword.lower() in course.lower()
    ]

    print(f"\n🔎 Courses containing '{keyword}':")
    if filtered:
        for c in filtered:
            print("-", c)
    else:
        print("No matching courses found.")


# ===============================
# FEATURE 5: GENERATOR EXPRESSION
# (LAZY PROCESSING)
# ===============================
def course_generator(courses, keyword):
    return (
        course for course in courses
        if keyword.lower() in course.lower()
    )


def process_with_generator(courses, keyword):
    print(f"\n⚡ Processing courses lazily for '{keyword}'")

    gen = course_generator(courses, keyword)

    try:
        while True:
            print("→", next(gen))
    except StopIteration:
        print("Finished processing.")


# ===============================
# MAIN PROGRAM (SYSTEM FLOW)
# ===============================
def main():

    # READ
    display_courses(enrolled_courses)

    # CREATE
    add_course(enrolled_courses, "Physics 102")
    display_courses(enrolled_courses)

    # DELETE
    remove_course(enrolled_courses, "Math 101")
    display_courses(enrolled_courses)

    # FILTER (LIST COMPREHENSION)
    filter_courses(enrolled_courses, "Science")

    # GENERATOR PROCESSING
    process_with_generator(enrolled_courses, "Science")


# Run program
main()
