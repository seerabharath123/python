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














