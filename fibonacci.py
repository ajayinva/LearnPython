def fibonacci1(num):
    if num <= 0:
        return 0
    if num <= 2:
        return 1
    a = 1
    b = 1
    next_value = 0
    for i in range(2, num):
        next_value = a + b
        a = b
        b = next_value
    return next_value


def fibonacci2(num):
    if num <= 2:
        return 1
    return fibonacci2(num-1) + fibonacci2(num-2)


def main():  # Wrapper function
    print(fibonacci2(int(input('How many numbers do you need? '))))


if __name__ == '__main__':
    main()
