a = [10, 20, 30, 40, 50, 60]

sum = 0
for i in a:
    print("Iteration val", i, "sum so far", sum)
    sum = sum + i
    print(sum)

prod = 1
for i in a:
    print("Iteration val", i, "prod so far", prod)
    prod = prod * i
    print(prod)

print("Final product", prod)
print("Final sum", sum)

print("Example to add elements in range")
prevsum = 0
for i in range(6, 12):
    print("Iteration val", i, "sum so far", sum)
    prevsum = prevsum + i

print("Sum of value from 0 to 9", prevsum)


print("Example to add elements in range")
prevsum = 0
for i in range(12):
    print("Iteration val", i, "sum so far", sum)
    prevsum = prevsum + i

print("Sum of value from 0 to 9", prevsum)

for i in a:
    print("For loop code block")
    if i > 10:
        print(i)


# #
# #
# # for
# # for each
# # while
# #
# # for i in range(6, 10):
# #
# # for i in range(6, 10):
# #     print(i)
# #
