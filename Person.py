class Person(object):
    __name = ''
    __age = 0
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
    def show(self):
        print(self.__name, self.__age)

    def __str__(self):
        return self.__name + ' ' + str(self.__age)

