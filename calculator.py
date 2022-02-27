import sys

print(sys.argv)

print(sys.argv[1])

operand = sys.argv[1]

print(operand)

booty = int(sys.argv[2])
print(booty)
goop = int(sys.argv[3])
print(goop)

if operand == "add":
    print(booty+goop)