lst = [("Tom", 19, 80), ("John", 20, 90),
       ('Jony',17, 91), ("Jony", 17, 93), ("Json", 21, 85)]
s = sorted(lst, key=lambda x: (x[0], x[1]))
print(s)