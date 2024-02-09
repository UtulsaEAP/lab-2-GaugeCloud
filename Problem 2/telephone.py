def telephone():
    phone_number = int(input())
    
    print("(", end="")
    print((phone_number // 10000000), end= ") ")
    print(((phone_number % 10000000) // 10000), end= "-")
    print(phone_number % 10000)
if __name__ == "__main__":
    telephone()