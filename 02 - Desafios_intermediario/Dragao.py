
def nivel_energia(n):
    if n <= 8000:
        return "Inseto!"
    else:
        return "Mais de 8000!"
    
    
C = int(input()) 
for i in range (C): 
   
  n = int(input())
  resultado = nivel_energia(n)
  print(resultado)


              

