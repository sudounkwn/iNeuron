import loggerFile

try:

    class IneuronMembers:

        def __init__(self, name, age, role):
            """Constructor to initialize the class variables"""
            self.name = name
            self.age = age
            self.role = role

        def print_data(self):
            """Fucntion that prints all the variable values"""
            print('Variables values are name:: ', self.name, ' and age:: ', self.age,
                  ' role in the organization:: ',
                  self.role)


    i1 = IneuronMembers('Raj', 28, 'Student')
    i1.print_data()


###################################################################################################################

    class IneuronStudent:

        def __init__(self,name, course, expyrs=0):
            """Constructor to initialize the class variables"""
            self.name = name
            self.course = course
            self.expyrs = expyrs

        def dispay(self):
            """Fucntion that prints all the variable values"""
            print('Student details, Name::',self.name, ' enrolled Course::',self.course, ' Years of exp::',self.expyrs)

    is1 = IneuronStudent('Shyam','FSDS', 4)
    is1.dispay()

###################################################################################################################

    class ExpStudent(IneuronStudent):
        def __init__(self,name, course, expyrs, domain):
            """Constructor to initialize the class variables"""
            IneuronStudent.__init__(self,name, course, expyrs)
            self.domain = domain

        def dispay(self):
            """Fucntion that prints all the variable values"""
            print('Student details, Name::',self.name, ' enrolled Course::',self.course, ' Years of exp::',self.expyrs ,' in domain::',self.domain)

    e1 = ExpStudent('Ramesh','FSDS',8,'DBA')
    e1.dispay()

except Exception as e:
    loggerFile.logg.info(e)
