# Palindrome

def main():
    x=str(input(""))
    y=list(x)
    if y == y[::-1]:
        print(True)
    else:
        print(False)
if __name__ == "__main__":
    main()
