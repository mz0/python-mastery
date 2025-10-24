#!/usr/bin/env python3
# https://realpython.com/python-async-features/

import asyncio
from aiohttp import ClientSession, ClientError
from codetiming import Timer


async def task(name, work_queue):
  timer = Timer(text=f"Task {name} elapsed time: {{:.1f}}")
  # max_field_size solves
  # Got more than 8190 bytes (10627) when reading Header value is too long.', url='https://twitter.com'
  async with ClientSession(max_field_size=16380) as session:
    while not work_queue.empty():
      url = await work_queue.get()
      print(f"Task {name} GET {url}")
      timer.start()
      try:
        async with session.get(url) as response:
          await response.text()
      except ClientError as e:
        print(f"Task {name} failed: {e}")
      finally:
        timer.stop()


async def main():
  work_queue = asyncio.Queue()  # Create the queue of work

  # Put some work in the queue
  for url in [
    "https://google.com",
    "https://yahoo.com",
    "https://linkedin.com",
    "https://apple.com",
    "https://microsoft.com",
    "https://facebook.com",
    "https://twitter.com",
  ]:
    await work_queue.put(url)

  # Create and Run the tasks
  with Timer(text="\nTotal elapsed time: {:.1f}"):
    await asyncio.gather(
      asyncio.create_task(task("One", work_queue)),
      asyncio.create_task(task("Two", work_queue)),
    )


if __name__ == "__main__":
  asyncio.run(main())
