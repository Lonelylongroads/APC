# 1. Single Inheritance
class Parent:
    def show_parent(self):
        print("Parent class")

class Child(Parent):
    def show_child(self):
        print("Child class")

c = Child()
c.show_parent()
c.show_child()