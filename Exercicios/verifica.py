class Verifica:

    def verificaMenorIdade(self):
        idade = int(input("Digite sua idade"))

        if idade < 18:
            print("Vocé menor de Idade")
        else:
            print("Vocé maior de Idade")
            