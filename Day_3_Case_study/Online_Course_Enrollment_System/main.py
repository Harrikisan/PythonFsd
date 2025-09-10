from course import Course
from student import Student
from premium_student import PremiumStudent

python_course = Course("Python beginners", "PY102", 3, 500)
data_science = Course("Data Science ", "DS101", 4, 700)
ml_course = Course("Machine Learning", "ML201", 5, 1000)

harri = Student("Harri")
bob = PremiumStudent("Kisan")


harri.enrollment.enroll_course(python_course)
harri.enrollment.enroll_course(data_science)
harri.enrollment.enroll_course(ml_course)
harri.enrollment.display_enrollment()
harri.display_totals()

print("\n---\n")

# another enrollment
bob.enrollment.enroll_course(python_course)
bob.enrollment.enroll_course(data_science)
bob.enrollment.enroll_course(ml_course)
bob.enrollment.drop_course("DS101")
bob.enrollment.display_enrollment()
bob.display_totals()