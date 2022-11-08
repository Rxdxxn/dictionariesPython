def dict():
    key_value={}

    key_value[2] = 56
    key_value[1] = 2
    key_value[5] = 12
    key_value[4] = 24
    key_value[6] = 18
    key_value[3] = 323

    print("...key_value...", "\n" , key_value)
    

    x = sorted(key_value.items(), key=lambda x:x[1])
    print("...key_value_sorted...","\n" ,x) 

def main():
    dict()

if __name__ == "__main__":
    main()