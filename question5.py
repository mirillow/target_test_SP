
def reverse_str(string):
    result = ""
    for char in string:
        result = char + result
    return result


# Entrada pelo STDIN
def main():
    result = reverse_str(input())
    print(f"String reversa: {result}")


if __name__ == '__main__':
    main()