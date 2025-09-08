print("This is ProblemSolving Excersizes for Nested Functions and Closures.......\n---------------------------------------------------------------------")





print("Q1: write a function make_multiplier(n) that returns another function multiplies any number by (n)")
def make_multiplier(n):
    def multiplier_num(m):
        nonlocal n
        return n * m
    return multiplier_num
num1 = make_multiplier(3)
print(num1(10))
num2 = make_multiplier(5)
print(num2(10))





print("Q2: write a function that makes counter")
def counter():
    count = 0
    def increament():
        nonlocal count
        count+=1
        return count
    return increament
increament = counter()
print(increament())
print(increament())
print(increament())






print("Q3: write a function that powers any number to power (n)")
def power_base(n):
    def power_raiser(m):
        nonlocal n
        return n**m
    return power_raiser
power = power_base(5)
print(power(3))
print(power(2))