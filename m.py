class Base(object): pass
class A(Base): pass
class B(Base): pass
class C(Base): pass
class D(A, B, C): pass

if __name__ == '__main__':
  print(D.__mro__)
