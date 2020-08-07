# Asks for user input until it receives a valid one
while True:
    height = input("Please enter the pyramid height:\n")
    try:
        value = int(height)
    except:
        value = -1

    if value > 0 and value < 9:
        break
    else:
        continue
    

# prints a pyramid of hashes
for i in range(1, value + 1):
    print(" " * (value-i), end="")
    print("#" * (i) + " " * 2 + "#" * (i))


