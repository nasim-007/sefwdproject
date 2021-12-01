# Object oriented progrmming

class Person():

    #Class attribute
    designation = 'Software Engineer'

    #Instant Attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('Hello '+self.name+'!')
        print('My age is '+str(self.age)+'.')
    def greetings(self, hobby):
        print('I am '+self.name+' and my hobby is '+hobby+'.')

#Initiate the class
myobj = Person('Nasim', 25)
myobj2 = Person('Mahmud', 25)
myobj.greetings('Coding')
print('I am a '+myobj.__class__.designation+'.')