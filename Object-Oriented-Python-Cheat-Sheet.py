

"""
This is how we write a class in python.
A class is a template for creating instances
A class contains data and functions associated with it, called attributes and methods

"""
class Employee:
    """
We define class variables at the begiinning of the class outside of the __init__() magic method
"""
    raise_amount = 1.04
    num_of_employees = 0
    

    """
    All class methods in python pass the instance they are called upon as the first argument. Thus our first parameter is self
    """
    def __init__(self, first, last, pay): # The self keyword refers to the instance of the class in this case
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
        Employee.num_of_employees += 1
        """
The aboe syntax is how you set instance variables for each instance. Note that these are instance variables, not class variables meaning
that these can only be accessed through the instance level and are unique to each instance
"""

    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        #                           or Employee.raise_amount
        self.pay = int(self.pay * self.raise_amount)
        """Even though we have defined the raise_amount class variable above, simply accessing it
        with the variable name will result in a name error becuase when we execute the method the method will look for the variable outside of the class
        scope. Instead, when we refer to a class variable, we must do so through the class itself or an instace of the class
        """

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
    """ This is a class method, meaning that python makes it take in a class as the first argument automatically. The standard convention for a class
    paramenter in python is cls. A normal instance method can be redefined/modified by wrapping the @classmethod decorator around it, resulting in the
    formation of a class method. We can only refer to class arributes/variables using class methods
    """

    @classmethod
    def from_string(cls, emp_string):
        first, last, pay = emp_string.split('-')
        return cls(first, last, pay)
    """ In the above I have created an alternative constructor method, which is a class method that is used to construct an object alternatively to the __init__ method
    We use alternative constructors when we want to create a class in ways that the __init__ method cannot. On a side not, we usually start to name an alternative constructor
    with the 'from' keyword.
    """

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
    """ This is a static method, which is a method that does not take in a class or an instance as it's first argument. Becuase of this we don't need to specify cls or self as
    the first parameter of the method. Basically a static method is like a typical function. We use static methods when we do not need to acess instance or the class anywhere
    within the function
    """

    
    """
    We can use the property decorator to make a method and attribute. An example is shown all the way down
    """
    @property
    def property_email(self):
        return f"The email is {self.first}.{self.last}@gmail.com"

    """
    This is a setter decorrator in python (remeber CSA?). The setter decorator will be named after the attribute that it is applied on with a dot followed by the keyword setter. The setter
    method must also be named after the attribute which is being set.
    """

    @property
    def fullname_property(self):
        return f"{self.first} {self.last}"

    @fullname_property.setter
    def fullname_property(self, name):
        self.first, self.last = name.split(" ")

    """
    This is a delter decorrator in python. The syntax for deleter is the same, however the deleter decorator is used to specify code for what to do when deleting an attribute. The
    deleter method gets executed when the del keyword is used
    """
    @fullname_property.deleter
    def fullname_property(self):
        print("Fullname Deleted!")
        self.first = None
        self.last = None

        


"""
Creating a subclass is similar to creating a regular class in python, and we can specify the classes we inherit from by mentioning the names of those classes in parenthesis
after the subclass name.
"""
class Developer(Employee):
    raise_amount = 1.25

    """
    Here we are modifying the __init__ method from the Employee super class to fit the needs of the Developer subclass. Since we need to add an extra argument to the __init__ method
    which is prog_lang - the programming language of the Developer, we could simply initialize each argument individually by using self. however that is very inefficient. A faster method
    is to initialize the common/shared/existing parameters by using the __init__ method of the Employee super class. This can be done with the super() keyword, which directly refers to the
    immediate super class, and then calling the __init__ method on the super() keyword (which is like calling the __init__ method from the actual super class). The remaining parameters
    we can initialized individually
    """
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay) # Employee.__init__(self, first, last, pay) also works
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        """
        It is generally not recommended for default arguments to functions to be of mutable data types. This is why we write the code below
        """
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for i in self.employees:
            print(f'--> {i.fullname()}')

    def __repr__(self):
        """
        The repr duner method is predefined in python and is used to represent an object. Typically, the repr dunder method is seen as the repr() function and
        it is predefined to return the exect python command used to instantiate the object. We can modify this dunder method to our needs. Also if the
        str dunder method is not defined in a class, when the str method is executed the __repr__ dunder method will be executed automatically inplace of it.
        The repr dunder method is typically used by developers for logging and debugging purposes
        """
        return f"Employee({self.first},{self.last},{self.pay})"
        

    def __str__(self):
        """
        The str dunder method returns the string version of the object that it is applied on. This is usally the location of the object in memory, but this can be changed
        to fit the users needs
        """
        return f"{self.fullname()} - {self.email}"


    def __add__(self, other):
        """
        The __add__ dunder method is used to specify how an objects should be have when they are added together like this: object1 + object2
        """
        return self.pay + other.pay
    

    def __len__(self):
        """
        The len method is used to specify how an object should behave when the len() function is applied to it. 
        """
        return len(self.fullname())
    


"""
This is an example of an instance in python.
We create instances from classes
"""

print(Employee.num_of_employees)
emp_1 = Employee("Jesus","Chirst",900000)
emp_2 = Employee("Gautham", "Buddtha", 700000)


"""
Each instance is created at a seperate location in memory, with its own unique memory address
Every time we create an instance of a class, the __init__ magic method gets run automatically
"""
print(emp_1)
print(emp_2)

"""
Instance variables are variables that contain data that is unique to each instance
You can add instance variables using the syntax shown below
"""
emp_1.first = "Sid"
emp_1.last = "Vadyalam"
emp_1.email = "sidvadyalam@company.com"
emp_1.pay = 500000

emp_2.first = "Test"
emp_2.last = "User"
emp_2.email = "testuser@company.com"
emp_2.pay = 600000


"""
We can refer to atrributes within a class by using these syntax
"""
print(emp_1.email)
print(emp_2.email)

print(f"{emp_1.first} {emp_1.last}")

"""
We can refer to a method using the syntax below. If we don't put the parenthesis after the method name then we will
get the location in memory of the method printed out. However if we do put parenthesis after the method name then we
will get the return value of the method along with method execution
"""
print(emp_1.fullname)
print(emp_2.fullname())

"""
You can also call/run methods from the class level, but when we do we must remember to pass in an instance into the method
"""
print(Employee.fullname(emp_1))


"""
Whenever we access an attribute through an instance, python will first check if the instance contains that atrribute, and if it doesnt
find it then it will check if the class contains that attribute and if it doesn't find it then it will check if the inherited super class contains
the attribute and this will continue until it reaches the highest level. If it doesnt find the variable it will return a variable not defined error
"""
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

"""
We can access the namespace of an instance by using the __dict__ attribute and by doing so we see that the instances dont have class
variables in their name spaces. Instead the classes themselves have the class variables in their name spaces. 
"""
print(Employee.__dict__)
print(emp_1.__dict__)
print(emp_2.__dict__)


"""
We can change the value of class variables by accessing them through classes or instances and reassigning their value. If we were to change the value by
accessing it through an instance then only the instance's copy of the class variable is changed and the class variable within the class stays the same, which
means that all other instances created from the class will have the the original value assigned within the class variable rather than the changed class variable
done by the instance. Basically, when we assign a new value of a class variable by accessing it through an instance, python adds a new instance attribute that
happens to have the same name as the class variable into the namespace of the instance, and so since instance attributes are accessed first in python before
class variables, the newly created instance variable get printed out
"""
emp_1.raise_amount = 1.10
print(emp_1.__dict__)
print(Employee.__dict__)
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)


"""
If we change a class variable value by accessing it through the class, then the class variable value will change within the class and for every instance of the
class from that point onwards. Specifally if an instance cannot find the class variable at the instance level it will look for class variable at the class level
and find that it has been changed to the new updated value
"""
Employee.raise_amount = 1.20
print(emp_1.__dict__)
print(Employee.__dict__)
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)



print(Employee.num_of_employees)


"""
We can use class methods just like how we use instance methods. Also class methods need not be applied only on class, for we can apply class methods on objects
as well. The class method will simply consider the class of the object that it is being executed on. It is often ill advised to do this however
"""
Employee.set_raise_amount(1.06) # This is the class method being run on a class
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(Employee.raise_amount)

emp_1.set_raise_amount(1.10) # This is the class method being run on an instance of the class. This is not recommended
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(Employee.raise_amount)

"""
Here I am creating an instance of a class using the alternative constructor that was defined above
"""

emp_3 = Employee.from_string("Jesse-Dough-45000")
print(emp_3)

""" Now I'm testing the Static method that we created above by passing in a datetime object and checking if it is a workday. Static methods can also be used by the instances and classes
"""
import datetime

my_date = datetime.date(2012, 7, 10)
print(Employee.is_workday(my_date))

"""
Here I am using the Developer subclass to create two developer objects. Since the Developer subclass is an instance of the Employee class, it will have access to the attributes
and methods within the Employee class, including it's __init__ method, which allows me to create an object of the Developer subclass without having to redifine an __init__ method.
Basically whenever we create an instance fof the Developer class, python will check the develper class for the __init__ method or whatever method we may be calling at that moment
and if it doesn't find it, it then looks for the method in the class that the subclass inherits from and if it still doesn't find the method, it then looks at the next highest class
. Python will continue to move up this chain of inheritance until it either finds the method or reaches the highest class level, upon which it throws an error. This chain if
inheritance upon which python checks for methods is called the method resolution order. We can look at the method resolution order by using the help() method
"""

dev_1 = Developer("Steve", "Jobs", 1000000, "python")
dev_2 = Employee("Thanos", "Stones", 500000)

print(dev_1.email)
print(dev_2.email)
print(help(Developer))



"""
Whenever we try to execute a method  or access an attribute from our parent class, from an instance of a subclass. Python, first checks if that method/attribute is within the subclass first.
If it finds the method, it will then execute that method regardless of the fact that the same method exists on the parent class. If it doesnt find the method, it will walk up the method
resolution order until it finds the method/attribute. This means that python will always prefer to execute the method/attribute the attribute that is in the nearest class of the instance that said
method/attribute was accessed from. The highest parent class in the method resolution order is the buitins.object class, which is the superclass that all classes inherit from.
Using the help function gives us all the methods/attributes that a subclass inherits from.
"""

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)


print(dev_2.pay)
dev_2.apply_raise()
print(dev_2.pay)

"""
We can also access attributes that are specific to a subclass
"""

print(dev_1.prog_lang)

"""
Here I am creating an instance of the manager class
"""

mgr_1 = Manager("Sue", "Smith", 90000, [dev_1])

print(mgr_1.email)
mgr_1.add_emp(dev_1)
mgr_1.print_emps()
mgr_1.remove_emp(dev_1)
mgr_1.add_emp(dev_2)

"""
The isinstance(object, class) function returns True if an object is an instance of a class and returns False if it isn't
"""

print(isinstance(mgr_1, Developer))
print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Manager))

"""
The issubclass(subclass, class) function returns True if an subclass is an subclass of a class and returns False if it isn't
"""

print(issubclass(Developer, Employee))
print(isinstance(Manager, Employee))

"""
When a method is sorrounded by double underscores (__) we call that dunder. So a duner method is a method sorrounded by double underscore. So __init__ is called the dunder init method.
Python has some special/magic methods that modify some of the default ingrained functionality in python. For instance the __repr__ method is a method that is predefined in python to
produce the set of class instantiations that led to the creation of the object. Thusly, we can use the repr dunder method to redefine it and make it output the object in a more readable manner.
"""

print(emp_3.__repr__)
print(emp_3.__str__)
print(repr(emp_3))
print(str(emp_3))

"""
Another important set of duner methods is arithmetic dunder methods like the dunder add or __add__ method. These methods, define how objects should behave when manipulated arithmetically. For
instance the __add__ method is show below and is predefined for integers to add the integers together and is predefined to strings to add strings together. We can predefine this for
our own classes and specify how ojects of our class should arithmetically add toegther. Also we can define how to arithmeticly multiply, subratct, divide etc. on objects by using the correspoing
dunder methods.
"""

print(int.__add__(1, 2))
print(str.__add__("a","b"))
print(emp_1 + emp_2)


"""
The dunder len method is a nother special method that is predefined in python. This special method is used in strings and lists to get the length of the strong/list. We can define this lenth
method for our own classes using the __len__ method. 
"""

print(len(emp_1))



"""
The list of all python dunder methods is in this documentation: https://docs.python.org/3/reference/datamodel.html#special-method-names
The return NotImplemented keyword is used to define how an object behaves when the execution of a dundermethod fails
"""


"""
The @property decorator allows a method to be converted to an attribute, so when we want to "execute" the method, we can simply call it like an attribute
"""
print(emp_1.property_email)









