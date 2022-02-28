class Person:
    def __init__(self, name, address, telephone_number):
        self.__name = name
        self.__address = address
        self.__telephone_number = telephone_number

    def print_person(self):
        print("The person's name is: ", self.__name)
        print("The person's address is: ", self.__address)
        print("The person's telephone number is: ", self.__telephone_number)


class Customer(Person):
    def __init__(self, name, address, telephone_number, customer_number, mailing_list):

        Person.__init__(self, name, address, telephone_number)

        self.__customer_number = customer_number
        self.__mailing_list = mailing_list

    def print_person(self):
        Person.print_person(self)
        print("The customer's customer_number is: ", self.__customer_number)
        print("The customer's mailing list preference is: ", self.__mailing_list)
