c = int(input()) #define a quantidade de inserçao
for i in range(c):
    n = int(input())
    if n <= 8000:
        print("Inseto!")
    else:
        print("Mais de 8000!")
