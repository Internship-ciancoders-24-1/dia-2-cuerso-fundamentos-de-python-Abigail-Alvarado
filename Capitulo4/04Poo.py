class Person:
    def __init__(self, name, age ):
        self.name = name 
        self.age = age

    def Say_hello(self):
        print('Hello mi name is {} and I am {} years old'.format(self.name, self.age))


if __name__ == '__main__':
    person = Person('Abigail', 21)
    print('Age: {}'.format(person.age))
    person.Say_hello()
