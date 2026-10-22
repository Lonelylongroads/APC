# 3. Multilevel Inheritance
class Grandparent:
    def grand_feature(self):
        print("Grandparent feature")

class Parent(Grandparent):
    def parent_feature(self):
        print("Parent feature")

class Child(Parent):
    def child_feature(self):
        print("Child feature")

c = Child()
c.grand_feature()
c.parent_feature()
c.child_feature()