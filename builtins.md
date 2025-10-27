```python
import sys

dir(sys.modules['builtins'])
['ArithmeticError', 'AssertionError', 'AttributeError',
 'BaseException', 'BaseExceptionGroup', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning',
 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError',
 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EncodingWarning', 'EnvironmentError', 'Exception', 'ExceptionGroup',
 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit',
 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError',
 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError',
 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError',
 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError',
 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning',
 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit',
 'TabError', 'TimeoutError', 'True', 'TypeError',
 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError',
 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'ZeroDivisionError',
 '_', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__',
 'abs', 'aiter', 'all', 'anext', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes',
 'callable', 'chr', 'compile', 'complex', 'copyright', 'credits', 'dict', 'dir', 'divmod',
 'classmethod', 'delattr', 'getattr', 'hasattr', 'setattr', 'staticmethod',
 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'globals',
 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter',
 'len', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord',
 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round',
 'set', 'slice', 'sorted', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip', 'license']
```
| Container | Method |
|:-------- |:----------------|
| len(x)   | `x.__len__()`        |
| x[a]     | `x.__getitem__(a)`   |
| x[a] = v | `x.__setitem__(a,v)` |
| del x[a] | `x.__delitem__(a)`   |
| a in x   | `x.__contains__(a)`  |

| Num op | Method              |
|:-------|:--------------------|
| a == b | `a.__eq__(b)`       |
| a + b  | `a.__add__(b)`      |
| a - b  | `a.__sub__(b)`      |
| a * b  | `a.__mul__(b)`      |
| a / b  | `a.__div__(b)`      |
| a // b | `a.__floordiv__(b)` |
| a % b  | `a.__mod__(b)`      |
| a << b | `a.__lshift__(b)`   |
| a >> b | `a.__rshift__(b)`   |
| a & b  | `a.__and__(b)`      |
| a \| b | `a.__or__(b)`       |
| a ^ b  | `a.__xor__(b)`      |
| a ** b | `a.__pow__(b)`      |
| -a     | `a.__neg__()`       |
| ~a     | `a.__invert__()`    |
| abs(a) | `a.__abs__()`       |

## Objects
```python
class Date:
  def __init__(self, year, month, day):
    self.year = year
    self.month = month
    self.day = day

d = Date(2012, 12, 21)
# Under the hood
d = Date.__new__(Date, 2012, 12, 21)
d.__init__(2012, 12, 21)
```

### Using `__new__`
```python
class Date:
  # ....
  @classmethod
  def today(cls):
    t = time.localtime()
    self = cls.__new__(cls)
    self.year = t.tm_year
    self.month = t.tm_mon
    self.day = t.tm_mday
    return self

d = Date.today()  # bypasses __init__()
```

### Defining `__new__`
Sometimes used when altering some tricky aspect of instance creation
* Instance caching
* Immutability
```python
class A:
  @staticmethod
  def __new__(cls, x, y):
    # ...
    return super().__new__(cls)

  def __init__(self, x, y):
    # ...
```

### `__del__` Method (Destructor)
Called when the reference count reaches 0
* Proper shutdown of system resources
* Releasing locks (e.g., threading)
```python
class Connection:
  # ...
  def __del__(self):
    # Cleanup statements

c = Connection()  # refcnt = 1
d = c             # refcnt = 2
del d             # refcnt = 1 - no call d.__del__()
c = None          # refcnt = 0 -> call c.__del__()
```

## Weak References (module `weakref`)
```python
import weakref

f = Foo()
fref = weakref.ref(f)
fref  # <weakref at 0x4203c0; to 'Foo' at 0x41dff0>

g = fref()  # Dereference (Getting the object being pointed at)
print(g)  # If no object -> None
```
Weak references are sometimes used where there are
reference cycles between objects e.g. graphs, trees, observers, caches.

Not something you should consider unless
dealing with really tricky memory problems.

More features in the `weakref` module

## Context Managers
For resources, consider the use of the 'with'
statement instead of relying on `__del__()`
```python
with obj as val:  # val = obj.__enter__()
  # do something with val
  # last statement -> obj.__exit__(ty, val, tb)

# val is no more!
class Manager:
  def __enter__(self):
    print('Entering')
    return self
  def __exit__(self, ty, val, tb):
    # ty, val, tb arguments have
    # information about pending exceptions (if any)
    print('Leaving')
    if ty:
      print('exception')

m = Manager()
with m:
  print('Hello World')


# tableformat stdout redirection
import sys
class redirect_stdout:
  def __init__(self, out_file):
    self.out_file = out_file

  def __enter__(self):
    self.stdout = sys.stdout
    sys.stdout = self.out_file
    return self.out_file

  def __exit__(self, ty, val, tb):
    sys.stdout = self.stdout
```

### Advanced Inheritance, Mixins
3-84..3-94 pp. 235-245
* Multiple Inheritance, Cooperative Inheritance
* Mixins
* [Exercise 3.8](Exercises/ex3_8.md)

## Inside Object
```python
from stock import Stock
goog = Stock("GOOG", 100, 490.10)
f'{goog.__module__}.{goog.__class__.__name__}'  # 'stock.Stock'

goog.__dict__
{'name': 'GOOG', '_shares': 100, 'price': 490.1}
Stock.__dict__
mappingproxy(
  {'__module__': 'stock',
   '_types':      (<class 'str'>, <class 'int'>, <class 'float'>),
   '__init__':    <function Stock.__init__ at 0x7..a>,
   'shares':      <property object at ..>,
   'cost':        <property object at ..>,
   'sell':        <function Stock.sell at ..>,
   'from_row':    <classmethod(<function Stock.from_row at ..>)>,
   '__repr__':    <function Stock.__repr__ at ..>,
   '__dict__':    <attribute '__dict__' of 'Stock' objects>,
   '__weakref__': <attribute '__weakref__' of 'Stock' objects>,
   '__doc__':     None
  }
)

del goog.price
goog.__dict__  # {'name': 'GOOG', '_shares': 100}
goog.price = 42.0
goog.__dict__['buy'] = 123.4
Stock.__dict__['cost'](goog)  # TypeError: 'property' object is not callable
Stock.__dict__['sell'](goog, 1)
repr(goog)
"Stock('GOOG', 99, 42.0)"
```
### Multiple Inheritance and MRO
* Attribute lookup: object (local) -> Class -> Base Class
* Method Resolution Order - walk down `__mro__` - first match wins
```python
class S1(Stock): pass
class S2(S1): pass
s2o = S2("SOUP", 100, 42.42)
S2.__mro__
(<class '__main__.S2'>, <class '__main__.S1'>, <class 'stock.Stock'>, <class 'object'>)
Stock.__mro__
(<class 'stock.Stock'>, <class 'object'>)
object.__mro__
(<class 'object'>,)
```
* Ordering rules
  * _Children_ before _parents_
  * _Parents_ go in order (first listed parent wins if there's a "tie")
* Multiple Inheritance hierarchy is flattened using C3 Linearization algorithm
```python
class A(object): pass
class B(object): pass
class C(A,B): pass
class D(B): pass
class E(C,D): pass
E.__mro__
(<class '__main__.E'>, <class '__main__.C'>,
 <class '__main__.A'>, <class '__main__.D'>,
 <class '__main__.B'>, <class 'object'>)
```
* All children of a common parent go first
```python
# m.py
class Base(object): pass
class A(Base): pass
class B(Base): pass
class C(Base): pass
class D(A, B, C): pass

from m import *
D.__mro__
(<class 'm.D'>,
 <class 'm.A'>, <class 'm.B'>, <class 'm.C'>,
 <class 'm.Base'>, <class 'object'>)
```
* `super()` delegates to the next class on the MRO
* These classes are _not_ the same! `super()` binds to the next implementation
  that is defined in the instance's MRO.  It's _not_ necessarily the immediate parent
  ```python
  class A(Base):
    def spam(self):
      Base.spam(self)

  class A(Base):
    def spam(self):
      super().spam()
  ```
* Class A is **anti-pattern**: If multiple inheritance is used,
  a direct parent call will probably violate the MRO

## Attribute binding and *descriptor protocol*

### Locate object *attribute* in two steps
1. *local* `o.__dict__` (if not found goto 2.)
2. Lookup `o.__class__.__dict__`

There's extra _magic_ (probably for subclasses)
```python
class Child(Parent): pass

c = Child()
c.__class__.__dict__
mappingproxy({'__module__': '__main__', '__doc__': None})
```

### Magic?
* Access to attributes of classes involves one extra processing step,
  called *descriptor protocol*
* Whenever an attribute is accessed on a class, the attribute is checked to see
  if it is an object that looks like a *descriptor*
* A *descriptor* is an object with one or more of the following methods
  `d.__get__(obj, cls)`, `d.__set__(obj, value)`, `d.__delete__(obj)`
* If a *descriptor* is detected, one of the above methods gets triggered on access

## Closures
* Essential feature (hangs on "first-class" functions, i.e. a function may be returned)
* Common applications:
  * Alternate evaluation (e.g., "delayed evaluation)
  * Callback functions
  * Code creation ("macros")

### Data encapsulation
```python
def counter(value):
  def incr():
    nonlocal value
    value += 1
    return value

  def decr():
    nonlocal value
    value -= 1
    return value

  def val():
    nonlocal value
    return value

  return incr, decr, val

up, down, val = counter(0)
up()
down()
down()
val()
```
