import time

class Timer:
       def __enter__(self):
           self.start = time.time()
           return self

       def __exit__(self, exc_type, exc_value, traceback):
           self.ende = time.time()
           print(f"Dauer: {self.ende - self.start} Sekunden")

with Timer() as t:
       sum(range(10_000_000))