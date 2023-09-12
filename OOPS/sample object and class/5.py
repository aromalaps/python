# teacher  and student
class collage:
    def __init__(self):
        self.collage='synnefo'
        self.department="pyhton"
        self.place="kollam"
    def student(self):
        name="anu"
        age=21
        address="nextof"
        id="ssss"
        print("Details of student")
        print("student id  :  ",id)
        print("Name        :  ",name)
        print("Age         :  ",age)
        print("address     :  ",address)
        print("collage     :  ",self.collage)
        print("Department  :  ",self.department)
        print("place       :  ",self.place)
    def teacher(self):
        name="arun"
        age=25
        address="errkl"
        id="23344"
        print("Details of Teacher")
        print("teacher id  :",id)
        print("Teacher     :",name)
        print("Age         :",age)
        print("address     :",address)
        print("collage     :",self.collage)
        print("Department  :",self.department)
        print("place       :",self.place)
        print("   ")
obj=collage()
user=input("you need to enter (student or teacher or both )to get the details of")
if user=="student":
    obj.student()
elif user=="teacher":
    obj.teacher()
elif user=="both":
        obj.teacher()
        obj.student()