a = 10
b = 20
c = 4
ans1 = ((a + b) * c) - a
print("Expression ((a + b) * c) - a  - with values", a, b, c, "resulted in ",  ans1)

a = 40
b = 50
c = 6
ans1 = ((a + b) * c ) - a

print("Expression ((a + b) * c) - a  - with values", a, b, c, "resulted in ",  ans1)

a = 27

r = a % 2
if r == 0:
    print("=====================")
    print(a, "is even")
    print("----------------------")
elif a > 11 and a < 20:
    print("***********************")
    print(a, "is odd and b/w 11 and 20")
    print("----------------------")
else:
    print("-----------------------")
    print(a, "is odd and not b/w 11 and 20")
    print("----------------------")
