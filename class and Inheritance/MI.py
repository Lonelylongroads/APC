# 2. Multiple Inheritance
class Father:
    def father_trait(self):
        print("Father's trait")

class Mother:
    def mother_trait(self):
        print("Mother's trait")

class Child(Father, Mother):
    def child_trait(self):
        print("Child's trait")

c = Child()
c.father_trait()
c.mother_trait()
c.child_trait()