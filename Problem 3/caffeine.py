
def caffeine():
    caffeine_mg = float(input())
    caffeine_mg_after_6 = (caffeine_mg)/2
    caffeine_mg_after_12 = (caffeine_mg_after_6)/2
    caffeine_mg_after_18 = (caffeine_mg_after_12)/2
    caffeine_mg_after_24 = (caffeine_mg_after_18)/2

    print("After 6 hours:", end=" ")
    print(f'{caffeine_mg_after_6 :.2f}', " mg")
    print("After 12 hours:", end=" ")
    print(f'{caffeine_mg_after_12 :.2f}', " mg")
    print("After 24 hours", end=" ")
    print(f'{caffeine_mg_after_12 :.2f}', " mg")

    
if __name__ == "__main__":
    caffeine()