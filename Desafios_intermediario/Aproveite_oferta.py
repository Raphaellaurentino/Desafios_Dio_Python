'''
T = int(input())
comprados=[]
vazias=[]
for i in range(T):
  
  n, k = map(int, input().split())
  
  comprados.append(n)
  vazias.append(k)
  resultado = (comprados[i]%vazias[i])+(comprados[i]//vazias[i])
  print(resultado)

  
 '''

T = int(input())
comprados = []
vazias = []

for i in range(T):
    n, k = map(int, input().split())  # Lê n e k em uma única linha
    comprados.append(n)
    vazias.append(k)
    resultado = (comprados[i] % vazias[i]) + (comprados[i] // vazias[i])
    print(resultado)