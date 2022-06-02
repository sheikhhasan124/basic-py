""" class Person:
    def __init__(self,name,job):
        self.name = name
        self.job = job

tamim = Person('tamim', 'cricker')
print(tamim.name,'and his pesa is', tamim.job)        """

# class with method
class Person:
    def __init__(self,name,job):
        self.name = name
        self.job = job
    def myFun(nam):
        print('his name is ' + nam.name)
    
tamim = Person('tamim', 'cricker')
# print(tamim.name,'and his pesa is', tamim.job) 
tamim.myFun()      