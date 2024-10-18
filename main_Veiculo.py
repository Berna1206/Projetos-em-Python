from class_Veiculo import *

if __name__ == '__main__':
    carro1 = Carro("Corolla", 150000,120000, 4)
    carro2 = Carro("Onix", 40000, 110000)
    carro3 = Carro("Fox", 50000)
    print(carro1.mostra_dados())
    print(carro2.mostra_dados())
    print(carro3.mostra_dados())

    moto1 = Moto("Xj6", 59700, 40000, 600)
    moto2 = Moto("F800", 64000, 45000)
    moto1.aumenta_valor(2000)
    print(moto1.mostra_dados())
    print(moto2.mostra_dados())