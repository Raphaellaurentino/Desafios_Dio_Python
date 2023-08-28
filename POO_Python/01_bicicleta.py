class Bicicleta:
    def __init__(self, marca, modelo, cor, ano, valor):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.valor = valor
    
    def buzinar(self):
        print("Plim Plim...")

    def parar(self):
        print("Freiando...")
        print("Parando...")
        print("Parada")

    def correr(self):
        print("Vrummmm...")

    def __str__(self):
        return f"{self.__class__.__name__}:{', '.join([f'{chave}={valor}'for chave, valor in self.__dict__.items()])}"


b1 = Bicicleta ("caloi", "street", "amarela", 2022, 1200)
print(b1.marca, b1.modelo, b1.ano, "R$:", b1.valor)

b1.buzinar()
b1.correr()
b1.parar()

print(b1)


    
