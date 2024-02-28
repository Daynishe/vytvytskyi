a, b = 25, 30

print(f"EX2\n"
      f"1.a <= b and b != a -> {a <= b and b != a}\n"
      f"2.a ==25 and b == 30 -> {a == 25 and b == 30}\n"
      f"3.a == 26 and b == 31 -> {a == 26 and b == 31}\n"
      f"4. a >= b and b == a -> {a >= b and b == a}\n")

print(f"EX4"
      f"1.a <= b or b == a -> {a <= b or b == a}\n"
      f"2.b == 330 or a == 251 -> {b == 330 or a == 251}\n"
      f"3.a == 26 or b == 31 -> {a == 26 or b == 31}\n"
      f"4. a >= b or b == a -> {a == b or b != a}\n")

print(f"EX5\n")
if a > 0:
    print("Capybara negative")
if a > 0:
    print("Capypara positive")
a = -1
if a > 0:
    print("Capybara negative")
if a > 0:
    print("Capypara positive")

print(f"EX6\n")
if a > 0:
    print(1)
else:
    print(-1)
