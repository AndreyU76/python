class Student:
    def __init__(self, name, surname, birth_date, school, class_room, rod, tea):
        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        self.school = school
        # Символ нижнего подчеркивания говорит пользователям класса, что атрибут для внутреннего использования
        self._class_room = {'class_num': int(class_room.split()[0]),
                            'class_char': class_room.split()[1]}
        self.rod = rod
        self.tea = tea
        
    # @property - позволяет обращаться к методу, как к атрибуту
    # .class_room() --> .class_room

    @property
    def class_room(self):
        return "{} {}".format(self._class_room['class_num'], self._class_room['class_char'])

    def next_class(self):
        self._class_room['class_num'] += 1

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def set_name(self, new_name):
        self.name = new_name

    def set_rod(self):
        self.rod = rod

    def set_tea(self):
        self.tea = tea

    def school(self):
        self.school = school

    #def class_num(self):
     #   self.class_num - clas_num

print("******После изменения класса*******")
students = [Student("Александр", "Иванов", '10.11.1998', "8 гимназия", "5 А", "Родитель Иванов Павел Александр", "Учитель Математики Румянова"),
            Student("Алексей", "Алексеев", '10.01.2000', "8 гимназия", "3 Г", "Родитель Алексеев Павел Петрович", "Учитель Географии Панов"),
            Student("Петр", "Сидоров", '10.01.1995', "8 гимназия", "8 Б", "Родитель Сидоров Павел Петрович", "Учитель Географии Панов"),
            Student("Иван", "Петров", '12.11.1999', "8 гимназия", "4 В", "Родитель Петров Глеб Иванович", "Учитель Физики Любимов"),
            ]

for student in students:
    student.next_class()

for num, student in enumerate(students, start=1):
    #print("{}) {} класс: {}:  {}:  {}".format(num, student.get_full_name(), student.class_room, student.rod, student.tea))
    print(" класс: {} ".format(student.school))
    print(" класс: {} ".format(student.rod))
    #print(" класс: {} ".format(student.rod))
    print(" класс: {} ".format(student.tea))
    print(" класс: {} ".format(student.class_room.split()))
