class MyClass:
    class_variable = "Hello, world!"

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

# Create an object of MyClass
obj = MyClass("This is an instance variable.")

# Access class variables using class object
print("Accessing class variable using class object:", MyClass.class_variable)

# Access instance variable using class object (not recommended)
print("Accessing instance variable using class object (not recommended):", obj.instance_variable)
