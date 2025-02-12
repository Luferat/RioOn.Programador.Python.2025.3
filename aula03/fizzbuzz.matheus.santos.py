numero  = int(input("Digite um número entre 1 e 50: "))
 
if 1<= numero <=50:
   
    if numero % 3 == 0 and numero % 5 == 0:
         print(f"FizzBuzz")
 
    elif numero % 5 == 0:
        print("Buzz")
   
    elif numero % 3 == 0:
        print("Fizz")
 
    else:    
        print(f"Tente de novo seguindo os critério pedido")
 
else :
        print(f"não é divisivel nem por 3 e 5")