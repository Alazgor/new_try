class A:
    def foo(self):
        print("A.foo")

class B(A):
    def foo(self):
        print("B.foo")
    # pass
class C(A):
    def foo(self):
        print("C.foo")

class D(B, C):
    pass

d = D()

d.foo()

print(D.__mro__)
#
# class A:
#     def foo(self):
#         print("A.foo")
#
# class B(A):
#     def bar(self):
#         print("B.bar")
#
# class C(B):
#     def baz(self):
#         print("C.baz")
#
# a = A()
# a.foo()
#
# b = B()
# b.foo()
# b.bar()
#
# c = C()
#
# c.foo()
# c.bar()
# c.baz()
#
#
#