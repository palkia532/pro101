import random
dice=str(input("Do you want to roll the dice"))
response="y"

while response=="y":
    print("The response should be y")

no=random.randint(1,6)

print()
print()
print()
print()
print()
print()

if response=="y":
    print(no)
else:
    print("you can exit")
