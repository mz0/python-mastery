class D1:
  def __init__(self, name):
    self.name = name

  def __get__(self, instance, cls):
    print('%s:__get__' % self.name)

  def __set__(self, instance, value):
    print('%s:__set__ %s' % (self.name, value))

  def __delete__(self, instance):
    print('%s:__delete__' % self.name)


class Foo:
  a = D1('a')
  b = D1('b')


if __name__ == '__main__':
    f = Foo()
    print(f.a)
    f.a = 42
    del f.a
