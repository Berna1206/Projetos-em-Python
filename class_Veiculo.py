class Veiculo:
    def __init__(self, modelo, quilometragem=0, valor=0):
        self.modelo = modelo
        self.quilometragem = quilometragem
        self.valor = valor

    def get_modelo(self):
        return self.modelo
    def set_modelo(self, novo_modelo):
        self.modelo = novo_modelo

    def get_quilometragem(self):
        return self.quilometragem
    def set_quilometragem(self, nova_quilometragem):
        self.quilometragem = nova_quilometragem

    def get_valor(self):
        return self.valor
    def set_valor(self, novo_valor):
        self.valor = novo_valor

    def aumenta_valor(self, aumento):
        self.valor += aumento

class Carro(Veiculo):
    def __init__(self, modelo, quilometragem=0, valor=0, qtd_portas=0):
        super().__init__(modelo, quilometragem, valor)
        self.qtd_portas = qtd_portas

    def get_qtd_portas(self):
        return self.qtd_portas
    def set_qtd_portas(self, nova_qtd):
        self.qtd_portas = nova_qtd

    def mostra_dados(self):
        return (f"Modelo do Carro: {self.modelo}"
                f"\nQuilometragem (Km): {self.quilometragem}"
                f"\nValor: R${self.valor:.2f}"
                f"\nQuantidade de Portas: {self.qtd_portas}\n")

class Moto(Veiculo):
    def __init__(self, modelo, quilometragem=0, valor=0, cilindradas=0):
        super().__init__(modelo, quilometragem, valor)
        self.cilindradas = cilindradas

    def get_cilindradas(self):
        return self.cilindradas
    def set_cilindradas(self, nova_cilindrada):
        self.cilindradas = nova_cilindrada
def situação
    def mostra_dados(self):
        return (f"Modelo da Moto: {self.modelo}"
                f"\nQuilometragem (Km): {self.quilometragem}"
                f"\nValor: R${self.valor:.2f}"
                f"\nCilindradas: {self.cilindradas}\n")
