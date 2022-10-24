# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$


import math
from math import pi

n = pi
print(n)

n = 100
my_pi = sum(1/16**x*(4/(8*x + 1) - 2/(8*x + 4) - 1 /
            (8*x + 5) - 1/(8*x + 6)) for x in range(n))

print(my_pi)
