class Student:
    def __init__(self, name , roll):
        self.name=name
        self.roll=roll

    def show_name(self):
        return self.name
    def show_roll(self):
        return self.roll
    
student_1= Student("Rabi", "006-03-02")

name_display= student_1.show_name
roll_display= student_1.show_roll

print(name_display,roll_display)
