class Father:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("name of father is ",name)
        print("age is ",age)
    def prop(self):
        print("he can drive car")
class mother:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("name of mother is",name)
        print("age is ",age)
    def property(self):
        print("she will  cook well")
class Xwife:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("name of mother is",name)
        print("age is ",age)
    def property(self):
        print("she teaches well")
class child1(Father,mother):
    def chil(self):
        print("he can draw ")
class child2(Father,Xwife):
    def sam(self):
        print("he study well")
fath=Father("farj",51)
moth=mother("angel",42)
step=Xwife("rose",28)
chi=child1("name",18)
chil2=child2("name",10)
fath.prop()
moth.property()
step.property()
chi.chil()
chil2.sam()
