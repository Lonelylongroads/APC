# 5. Hybrid Inheritance
class A:
    def feature_a(self):
        print("Feature A")

class B(A):
    def feature_b(self):
        print("Feature B")

class C(A):
    def feature_c(self):
        print("Feature C")

class D(B, C):
    def feature_d(self):
        print("Feature D")

d = D()
d.feature_a()
d.feature_b()
d.feature_c()
d.feature_d()