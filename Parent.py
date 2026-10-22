class Parent:
    def single_parent(self):
        print("Single Inheritance: Parent")

class ChildSingle(Parent):
    def single_child(self):
        print("Single Inheritance: Child")


class Father:
    def father_info(self):
        print("Multiple Inheritance: Father")

class Mother:
    def mother_info(self):
        print("Multiple Inheritance: Mother")

class ChildMultiple(Father, Mother):
    def child_info(self):
        print("Multiple Inheritance: Child")


class Grandparent:
    def grandparent_info(self):
        print("Multilevel Inheritance: Grandparent")

class ParentLevel(Grandparent):
    def parent_info(self):
        print("Multilevel Inheritance: Parent")

class ChildLevel(ParentLevel):
    def child_info(self):
        print("Multilevel Inheritance: Child")


class ParentHierarchical:
    def parent_info(self):
        print("Hierarchical Inheritance: Parent")

class ChildA(ParentHierarchical):
    def child_a_info(self):
        print("Hierarchical Inheritance: Child A")

class ChildB(ParentHierarchical):
    def child_b_info(self):
        print("Hierarchical Inheritance: Child B")


class Base:
    def base_info(self):
        print("Hybrid Inheritance: Base")

class FeatureA(Base):
    def feature_a(self):
        print("Hybrid Inheritance: Feature A")

class FeatureB(Base):
    def feature_b(self):
        print("Hybrid Inheritance: Feature B")

class HybridChild(FeatureA, FeatureB):
    def hybrid_info(self):
        print("Hybrid Inheritance: Hybrid Child")


print("--- 1. Single Inheritance ---")
obj1 = ChildSingle()
obj1.single_parent()
obj1.single_child()

print("\n--- 2. Multiple Inheritance ---")
obj2 = ChildMultiple()
obj2.father_info()
obj2.mother_info()
obj2.child_info()

print("\n--- 3. Multilevel Inheritance ---")
obj3 = ChildLevel()
obj3.grandparent_info()
obj3.parent_info()
obj3.child_info()

print("\n--- 4. Hierarchical Inheritance ---")
obj4_a = ChildA()
obj4_b = ChildB()
obj4_a.parent_info()
obj4_a.child_a_info()
obj4_b.parent_info()
obj4_b.child_b_info()

print("\n--- 5. Hybrid Inheritance ---")
obj5 = HybridChild()
obj5.base_info()
obj5.feature_a()
obj5.feature_b()
obj5.hybrid_info()