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
