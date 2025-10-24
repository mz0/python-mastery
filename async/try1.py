#!/usr/bin/env python3
# https://realpython.com/python-async-features/

import queue
import time
from codetiming import Timer


def task(name, work_queue):
  timer = Timer(text=f"Task {name} elapsed time: {{:.1f}}")
  while not work_queue.empty():
    delay = work_queue.get()
    print(f"Task {name} running")
    timer.start()
    time.sleep(delay/10)
    timer.stop()
    yield


def main():
  work_queue = queue.Queue()  # Create the queue of work

  # Put some work in the queue
  for work in [15, 10, 5, 2]:
    work_queue.put(work)

  # Create some tasks
  tasks = [task("One", work_queue), task("Two", work_queue)]

  # Run the tasks
  done = False
  with Timer(text="\nTotal elapsed time: {:.1f}"):
    while not done:
      for t in tasks:
        try:
          next(t)
        except StopIteration:
          tasks.remove(t)
        if len(tasks) == 0:
          done = True


if __name__ == "__main__":
  main()
