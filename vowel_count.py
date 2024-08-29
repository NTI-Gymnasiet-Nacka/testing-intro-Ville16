# Vokalräkning

def main():
    x=str(input(""))
    vowels= "aeiouyåäöAEIOUYÅÄÖ"
    z=0
    for i in x:
        if i in vowels:
            z+=1
    print(z)
if __name__ == "__main__":
    main()
