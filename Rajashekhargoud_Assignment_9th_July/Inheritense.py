import loggerFile
import constrImplementation as con  # importing constrImplementation.py for reuseability

try:
    class IneuronMentors(con.IneuronMembers):
        """Constructor to initialize the class variables"""

        def __init__(self, name, age, role, topic):
            con.IneuronMembers.__init__(self, name, age, role)
            self.topic = topic

        def mentordisplay(self):
            """Dispalying detials of user who are mentors under INeuron"""
            if self.role.upper() == 'MENTOR':
                print(self.name, ' is a mentor for topic ', self.topic)
            else:
                print(self.name, 'is not a mentor')


    m1 = IneuronMentors('Sudhanshu', 12, 'Mentor', 'FSDS')
    m1.mentordisplay()


#############################################Mutli Level Inheritense###################################

    class SeniorMentor(IneuronMentors):

        def __init__(self, name, age, role, topic):
            """Constructor to initialize the class variables"""
            IneuronMentors.__init__(self, name, age, role, topic)

        def senior_disp(self):
            """Dispalying detials of user who are mentors under INeuron"""
            if self.age >= 60 and self.role.upper() == 'MENTOR':
                print(self.name, ' is a senior mentor ')
            else:
                pass


    s1 = SeniorMentor('Prem', 66, 'Mentor','DB')
    s1.senior_disp()

except Exception as e:
    loggerFile.logg.info(e)
