from colorama import Fore, init, Style

init(autoreset=True)

def cross_product(v1, v2):
    result = [0, 0, 0]
    result[0] = v1[1] * v2[2] - v1[2] * v2[1]
    result[1] = v1[2] * v2[0] - v1[0] * v2[2]
    result[2] = v1[0] * v2[1] - v1[1] * v2[0]
    return result

def dot_product(v1, v2):
    result = 0
    for i in range(3):
        result += v1[i] * v2[i]
    return result

def vector_addition(v1, v2):
    result = [0, 0, 0]
    for i in range(3):
        result[i] = v1[i] + v2[i]
    return result

def vector_subtraction(v1, v2):
    result = [0, 0, 0]
    for i in range(3):
        result[i] = v1[i] - v2[i]
    return result

def get_vector(prompt):
    while True:
        try:
            print(Fore.YELLOW + prompt + Style.RESET_ALL)
            x = float(input("Enter component along x-axis: "))
            y = float(input("Enter component along y-axis: "))
            z = float(input("Enter component along z-axis: "))
            return [x, y, z]
        except ValueError:
            print(Fore.RED + "Invalid input! Please enter numeric values." + Style.RESET_ALL)

def main():
    v1 = get_vector("Enter the components of the first vector:")
    v2 = get_vector("Enter the components of the second vector:")

    cross_vector = cross_product(v1, v2)
    dot_vector = dot_product(v1, v2)
    add_vector = vector_addition(v1, v2)
    sub_vector = vector_subtraction(v1, v2)

    print(Fore.YELLOW + f"\nThe cross product of the two vectors is: {cross_vector}" + Style.RESET_ALL)
    print(Fore.YELLOW + f"The dot product of the two vectors is: {dot_vector}" + Style.RESET_ALL)
    print(Fore.YELLOW + f"The addition of the two vectors is: {add_vector}" + Style.RESET_ALL)
    print(Fore.YELLOW + f"The subtraction of the two vectors is: {sub_vector}" + Style.RESET_ALL)

if __name__ == "__main__":
    main()
