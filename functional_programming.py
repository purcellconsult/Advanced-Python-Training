# Functional Programming in Python
# --------------------------------
# Python is NOT a purely functional programming language like
# Haskell, Erlang, or Lisp. However, it does have functional prog aspects.
#
# lambda

from math import pi

add = lambda x: x + 2
print(add(5)) # 7

# the above lambda is equivalent to the following


def add_regular(x):
    return x + 2


print(add_regular(5))

double = lambda x: x * 2
print(double(10)) # 20


def area_of_circle(radius):
    return pi * radius ** 2

# the above translated to a lambda expression is as follows


area_of_cir_lambda = lambda radius:pi * radius ** 2


# map

def f(x):
    i = 0
    size = len(x)
    while i < size:
        x[i] += 2
        i += 1
    return x


result = f([1, 2, 3])
print(result)

mapping = list(map(lambda x: x + 2, [1, 2, 3]))
print(mapping)


# filter

# reduce