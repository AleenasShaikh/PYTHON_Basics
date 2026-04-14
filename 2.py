import random

n1 = random.randint(1, 100)


while True:
        n2 = input("Enter a number between 1 and 100: ") # get the users guess 
        if n2.lower() == "exit":
            print("Exiting the game. Goodbye aleena!")
            break
        n2 = int(n2) 

        if n1 > n2:
            print(f"The hidden number is greater than {n2}")
        elif n1 < n2:
            print(f"The hidden number is less than {n2}")
        elif n1 == n2:
            print(f"{n1} is equal to {n2} 🏆You won!🏆")
            n1 = random.randint(1, 100)
    