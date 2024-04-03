class A:
    def foo(self) -> None:
        print("A.foo")

class B(A):
    def foo(self) -> None:
        print("B.foo")

class C(A):
    def foo(self) -> None:
        print("C.foo")

class D(B, C):
    pass

d = D()
d.foo()  # prints "B.foo"