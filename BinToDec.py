def bin_to_dec(num):
    result = 0
    for i in range(0, len(num)):
        digit = num[0-i-1]
        print("digit:"+digit)
        result = result + (int(digit) * 2**i)
        print("result::"+str(result))
    return result


def main():  # Wrapper function
    print(bin_to_dec(input('Please enter a binary Number?')))


if __name__ == '__main__':
    main()
