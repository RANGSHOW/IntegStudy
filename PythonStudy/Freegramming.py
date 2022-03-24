class Person():
    def __init__(self):
        self.name = None
    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.name

me = Person()
print(me.get_name())
me.set_name("ChangHyeon")
print(me.get_name())