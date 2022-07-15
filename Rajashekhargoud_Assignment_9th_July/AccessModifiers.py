import loggerFile as lg  # import for logging purpose

try:
    class MentorDetails():
        name = None  # public variable
        _subject = None  # protected variable
        __phone = None  # private variable

        def __init__(self, name, subject, phone):
            """initialization of class variables"""
            self.name = name
            self._subject = subject
            self.__phone = phone

        def _mentor_sub(self):  # Protected method
            """Protected class that displays name of mentor and subject handles by him which protected variable"""
            print(f'Name of mentor is {self.name} and the course handled is {self._subject}')

        def __mentor_personal(self):  # Private method
            """Private method which can be called or accessed inside class only"""
            print(f'Personal contact number of mentor is {self.__phone}')

        def mentor_details(self):
            """Public method whcih can be accessed from anywhere"""
            self._mentor_sub()
            self.__mentor_personal()


    m1 = MentorDetails('Sudhanshu', 'FSDS', '9876543210')
    m1._mentor_sub()       #not a recommended approach to call protected members outside the class
    m1.mentor_details()
    m1.__mentor_personal()  # this will throw exception because private methos/variables are not accessible outside the class



except Exception as e:
    lg.logg.info(e)
