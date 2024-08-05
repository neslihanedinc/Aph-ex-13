def is_leap_year(year):
    if year % 400 == 0: # Yıl 400 ile bölünebiliyorsa, artık yıldır.
        return True
    elif year % 100 == 0:# Yıl 100 ile bölünebilir ama 400 ile bölünemezse, artık yıl değildir.
        return False
    elif year % 4 == 0:# Yıl 4 ile bölünebiliyorsa ve 100 ile bölünmüyorsa, artık yıldır.
        return True
    else: # Yukarıdaki koşullar sağlanmıyorsa, artık yıl değildir.
        return False
user_input = input("Enter a year: ")
try:
    year = int(user_input)
    if is_leap_year(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap error..")
except ValueError:
    print("Invalid input. Please enter a number: ")
