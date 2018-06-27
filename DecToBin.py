def dec_to_bin(num):
    result = ""
    while True:
        digit = num % 2
        result = result +str(digit)
        num = int(num/2)
        if num == 0:
            break
    return result[::-1]


def main():  # Wrapper function
    print(dec_to_bin(int(input('Please enter a Decimal Number?'))))


if __name__ == '__main__':
    main()
