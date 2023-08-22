class Person:
    def __init__(self, fio, age, massa, pas_seriya):
        self.__fio = fio
        self.__age = age
        self.__massa = massa
        self.__pas_seriya = pas_seriya

    @property
    def fio(self):
        return self.__fio
    
    @fio.setter
    def fio(self, value):
        self.__fio = value.split(" ")

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, value):
        if value > 18:
            self.__age = value
        else:
            raise ValueError        

    @property
    def massa(self):
        return self.__massa
    
    @massa.setter
    def massa(self,value):
        if value < 90:
            self.__massa = value
        else:
            raise ValueError
    
    @property
    def pas_seriya(self):
        return self.__pas_seriya
    
    @pas_seriya.setter
    def pas_seriya(self, value):
        one = value[0:2]
        two = value[2:9]
        if one.isupper() and two.isnumeric():
            self.__pas_seriya = value
        else:
            raise ValueError

pt = Person("", "", "", "")
pt.fio = "Javohir Hamdamov"
pt.age = 2
pt.massa = 75
pt.pas_seriya = "AB1234567"
print(pt.__dict__)