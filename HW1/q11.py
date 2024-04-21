def total_path(n):
    return factorial(n + n) / (factorial(n) * factorial(n))

# ---------------------


def factorial(n):
    fact = 1
    i = 1
    while (i <= n):
        fact = fact * i
        i += 1
    return fact


while (True):
    try:
        network_size = int(input("Please enter the desire size of network: "))
        if (network_size < 0):
            print("Please enter a positive value!")
        else:
            break
    except ValueError:
        print("Please enter a valid number.")
    else:
        print("The execution continued.")

print(
    f"The total possible path on {network_size} x {network_size} network is {total_path(network_size)}")
