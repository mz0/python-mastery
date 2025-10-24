#!/usr/bin/env python3
# https://realpython.com/python-async-features/

import queue

def task(name, work_queue):
    while not work_queue.empty():
        count = work_queue.get()
        total = 0
        print(f"Task {name} running")
        for x in range(count):
            total += 1
            yield
        print(f"Task {name} total: {total}")

def main():
    work_queue = queue.Queue()  # Create the queue of work

    # Put some work in the queue
    for work in [15, 10, 5, 2]:
        work_queue.put(work)

    # Create some tasks
    tasks = [task("One", work_queue), task("Two", work_queue)]

    # Run the tasks
    done = False
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
