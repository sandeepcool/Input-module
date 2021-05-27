#input module
print("Tell me anything")
anything = input()
print("hmm", anything, "...Really")
print()

#2

anything =int( input ("Enter a number:"))
something = anything ** 2
print(anything, "to the power of 2 is", something)
print()

#3

leg_a = float(input("input first leg length:"))
leg_b = float(input("input second leg length:"))
hypo = (leg_a **2 + leg_b **2) **2
print("Hypotenuse length is:", hypo)
print()

#4

a = float(input("enter a number:"))
b = float(input("enter b number:"))
sum1 = a + b
sum2 = a - b
sum3 = a * b
sum4 = a / b
sum5 = a % b
sum6 =a **2

print("the sum of a and b is:", sum1,sum2,sum3,sum4,sum5,sum6)
print("\nThat's all, folks")
print()

#5

name = input(" Enter your name: ")
print(" Hello, " + name +  ". Nice to meet you! ")
print()

#6

x = int(input())
y = int(input())
z = y = x =1
x = x % y
x = x % y
y = y % x
x = x // y
y = y // x

print(x, y, z, sep=' * ')

x = 1 / 2 + 3 // 3 + 4 ** 2
print(x)
print()

#7

x = 1
y = 2
z = x
x = y
y = z

print(x, y)
