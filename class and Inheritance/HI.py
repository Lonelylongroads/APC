# 4. Hierarchical Inheritance
class Parent:
    def parent_feature(self):
        print("Parent feature")

class Child1(Parent):
    def child1_feature(self):
        print("Child 1 feature")

class Child2(Parent):
    def child2_feature(self):
        print("Child 2 feature")

c1 = Child1()
c2 = Child2()
c1.parent_feature()
c1.child1_feature()
c2.parent_feature()
c2.child2_feature()