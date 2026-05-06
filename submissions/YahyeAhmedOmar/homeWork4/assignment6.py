# scope_demo.py

course_name = "Python Bootcamp"

# Global variables can be accessed anywhere.
# Local variables only exist inside the function.

def show_course():
    course_name = "Advanced Python"
    print("Inside function:", course_name)

print("Before function:", course_name)

show_course()

print("After function:", course_name)
