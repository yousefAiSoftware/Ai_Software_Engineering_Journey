class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.courses = {}
    def enroll(self,course_code,credits):
        self.courses.update({course_code : {"credits" : credits , "grade" : None}})
    def record_grade(self, course_code, grade):
        if course_code in self.courses:
            course = self.courses[course_code]
            course["grade"] = grade
        else:
            print("Course doesn't found")
    def calc_GPA(self):
        if len(self.courses) > 0:
            total_credits = 0
            total_grades = 0
            for value in self.courses.values():
                if value["grade"] == None:
                    continue;
                total_credits += value["credits"]
                total_grades += (value["credits"] * value["grade"])
            GPA = total_grades / total_credits
        else:
            print("You has not Courses yet")
            GPA = 0
        return GPA
    
std1 = Student("Yousef", "231419")
std1.enroll("CE222",4)
std1.enroll("CS371",4)
std1.enroll("LA201",3)
std1.enroll("CS413",3)
std1.record_grade("CE222",92)
std1.record_grade("CS371",98)
std1.record_grade("LA201", 98)
print(std1.calc_GPA())
    