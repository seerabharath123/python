class Employee():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def DisplayDetails(self):
        print(self.name)
        print(self.age)

EE=Employee("SARA",30)
print(EE.name)
print(EE.age)
EE.DisplayDetails()


class DataBinding():
    def __init__(self):
        self._x="It is Protected Access"
        print(self._x)

DD=DataBinding()
print(DD._x)

class Banking():
    def PublicMethod(self):
        print("Public Method")
    def _ProtectMethod(self):
        print("Protect Method")
    def __PrivateMethod(self):
        print("Private Method")

#CreatingInstance
BB=Banking()
BB.PublicMethod()
BB._ProtectMethod()
BB._Banking__PrivateMethod()

class
class Account:
"""This is docstring, explains brief about the class"""
	pass
sb_account=Account()
current_account=Account()
class MyBank_SBI():
           pass
class MyBank_AB:
          pass
class MyBank_HDFC(object):
          pass
#SS is an Object or Instance
SS=MyBank_SBI()
print(SS)
#AA is an Object or Instance
AA=MyBank_AB()
print(AA)
#HH is an Object or Instance
HH=MyBank_HDFC()
print(HH)

obj
Object1: Human
Identity: Midhun
Properties: Color, Height, Weight
Functionalities: walk () , see() , run() ....

method
class Banking():
#It is a Method of Member
#Class inside all are members
    def MyCustomer():
        print("Welcome to Banking")
        return()
#Driver Code
BB=Banking()
BB.MyCustomer()
#TypeError: MyCustomer() takes 0 positional arguments but 1 was given









