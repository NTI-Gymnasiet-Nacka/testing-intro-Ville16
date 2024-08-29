# Största skillnad

def main():
    x=(input("").split(","))
    y=list(x)
    y=[int(i) for i in y]
    y.sort()
    max_diff=y[0]-y[-1]
    print(max_diff)
if __name__ == "__main__":
    main()
