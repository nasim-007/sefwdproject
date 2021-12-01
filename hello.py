#Object oriented programming

class Person():

    #Class attribute
    designation = 'Software Engineer'
    
    #Instant attrubute
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('My name is '+self.name+'!')
        print('My age is '+str(self.age)+'.')
    
    def greetings(self, hobby):
        print('Hello '+self.name+'!')
        print('My hobby is '+hobby+'.')

#Initiate the object
myobj = Person('Nasim', 25)
myobj2= Person('Mahmud', 27)
print('I am a '+myobj.__class__.designation+'.')
myobj.greetings('Coding')