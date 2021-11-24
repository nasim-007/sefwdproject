class Person:

    #class attrubutes
    designation = 'Software Engineer'
    
    #instant attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('Hello Person!')
    
    def greetings(self):

        print('Hello '+ self.name+'!')
    
    def myage(self, hobby):
        print('I am '+str(self.age)+' years old and my hobby is '+hobby+'.')


class Nasim(Person):

    def __init__(self, name, age, reading, coding):
        
        self.reading = reading
        self.coding = coding
        super().__init__(name, age)
    
    def books(self):
        print('I love reading '+self.reading+' books.')

    def greetings(self):
        print('Nasim Mahmud!')


#initiate the class
name_obj = Person('Nasim', 25)
nasim_obj = Nasim('Nasim', 25, 'programming', 'Python')

name_obj.greetings()
print('I am a '+name_obj.__class__.designation+'.')
name_obj.myage('Coding')

nasim_obj.greetings()
nasim_obj.books()



def search(request):
    
    queryset1 = Project.objects.all()
    queryset2 = Service.objects.all()
    
    query = request.GET.get('q')
    
    if query:
        queryset1 = queryset1.filter(
            Q(title__icontains=query) | Q(short_description__icontains=query) |
            Q(category__icontains=query)


        ).distinct()
        
        queryset2 = queryset2.filter(
            Q(title__icontains=query) | Q(short_description__icontains=query)

        ).distinct()
    
    
    context = {
        'queryset1': queryset1,
        'queryset2': queryset2,
        'query': query


    }
    return render(request, 'nimuit/search.html', context)