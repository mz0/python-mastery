from concurrent.futures import Future,  ThreadPoolExecutor
import math
import time
import threading
from typing import Tuple

def parse_line(s: str) -> Tuple[str, str] | None:
  # not checking empty/blank value: parse_line('email=') == ('email', '')
  ss = s.split('=')  # or s.split('=', 1) to allow e.g. url = https://example.com?id=123
  if not len(ss) == 2:
    return None
  ss0 = ss[0].strip()
  if len(ss0) == 0:
    return None
  else:
    return ss0, ss[1].lstrip()


def worker(x, y, sleep=20):
  print(f'About to work for {math.ceil(sleep)} seconds ', end='')
  while sleep > 0:
    time.sleep(1.0)
    print('.', end='', flush=True)
    sleep -= 1
  print(' Done')
  return x + y


def do_work(fut: Future, x, y, sleep: int = 20):
  fut.set_result(worker(x,y, sleep=sleep))


fut = Future()
t = threading.Thread(target=do_work, args=(fut, 22, 33, 5.5))
t.start()
result = fut.result()
print(result)

pool = ThreadPoolExecutor()
fut = pool.submit(worker, 7, 3, 5)
print(fut)
print(fut.result())
