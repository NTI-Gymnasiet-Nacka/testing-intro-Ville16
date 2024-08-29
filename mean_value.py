# Medelvärde

def main():
    x=(input("").split(","))
    y=list(x)
    y=[int(i) for i in y]
    mean_value=sum(y)/len(y)
    print(mean_value)
if __name__ == "__main__":
    main()
