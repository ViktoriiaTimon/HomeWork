# 1. Even Numbers Generator

def even_numbers_generator(k):
  for i in range(0, k, 2):
      yield i
m = 60
for even_num in even_numbers_generator(m):
    print(even_num)

# 2. Fibonacci Generator
def fibonacci_generator(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b

num = 300
for fib in fibonacci_generator(num):
    print(fib)