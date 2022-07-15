import loggerFile as lg

try:
    class IneuronClass:

        def __init__(self,name,time):
            self.name = name
            self.time = time

        def class_details(self):
            """Dispaly class related details"""
            print(f'Regular class at {self.time} andled by {self.name}')


    class RevisionClass(IneuronClass):

        def __init__(self, name, time):
            IneuronClass.__init__(self, name, time)

        def class_details(self):                            #overrides the parent class method
            """Dispaly class related details"""
            print(f'Revision class at {self.time} andled by {self.name}')


    i1 = IneuronClass('Sudh','3pm')
    i1.class_details()
    # i1.mentor_name()
    # i1.class_details()
    #
    r1 = RevisionClass('Sunny','3pm')
    r1.class_details()

except Exception as e:
    lg.logg.info(e)
