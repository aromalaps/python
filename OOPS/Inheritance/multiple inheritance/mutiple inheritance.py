class A :
    def sample(self):
        print(10)
class B:
    def sample1(self):
        print(20)
class C(A,B):
    pass
obj=C()
obj.sample()
obj.sample1()