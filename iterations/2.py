n = input("Enter a number: ")
for i in range(2, int(n)):
     
        
     if   int(n) % i == 0: 
         print("is a composite number")
         break
else:     print("is a prime number")