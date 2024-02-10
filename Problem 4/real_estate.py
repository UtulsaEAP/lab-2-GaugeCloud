
def real_estate():
    
    current_price = int(input())
    last_month_price = int(input())
    
    print("This house is", end=" $")
    print((current_price), end= ". ")
    print("The change is", end=" $")
    print((current_price)-(last_month_price), "since last month.")
    print("The estimated monthly mortgage is $" f'{(current_price * 0.051)/12:.2f}.')
if __name__ == "__main__":
    real_estate()
