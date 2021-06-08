# a=input('Enter name')
# b=input('Enter age')
# c=input('enter')
class student:
    def __init__(self,name,age,std):
        self.name=name
        self.age=age
        self.std=std

    def get_info(self):
        print(self.name)
        print(self.age)
        print(self.std)
    @classmethod
    def user_info(self):
        name=input('Enter name - ')
        age=input('Enter age - ')
        std=input('Enter std - ')
        return self(name,age,std)

student1 = student.user_info()
student1.get_info()