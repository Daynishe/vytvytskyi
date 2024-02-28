import math

var_int = 10
var_float = 8.4
var_str = "No"
big_int = var_int * 3.5
var_float -= 1
print(f"var_int/var_float = {var_int / var_float}\n"
      f"big_int/var_float = {big_int / var_float}")
var_str = "No" * 2 + "Yes" * 3
print(f"var_int {var_int}\n"
      f"var_float {var_float}\n"
      f"var_str {var_str}\n"
      f"big_int {big_int}\n")
a, b, x = 1, 2, 3
Z = (math.sqrt(x ** 2 + b)) / (math.sqrt(x ** 2 + (a * x)))
print(f"Z = {Z} ")
