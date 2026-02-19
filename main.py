class Nutri:
    def __init__(self):
        pass
    
    def IMC(self, peso, altura):
        imc = float(peso/(altura**2))

        if imc < 18.5:
            classificacao = "Magreza extrema"
        elif imc < 24.9 and imc > 18.5:
            classificacao = "Normal"
        elif imc < 29.9 and imc > 25:
            classificacao = "Sobrepeso"
        elif imc < 39.9 and imc > 30:
            classificacao = "Obesidade"
        else:
            classificacao = "Obesidade Grave"
        
        return f"seu IMC é {imc:.1f} e sua classificação é {classificacao}"
    
    def TMB(self, peso, altura, idade, genero):

        altura = altura*100

        if genero.upper() == 'M':
            tmb = 88.36 + (13.4 * peso) + (4.8 * altura) - (5.7 * idade)
        else:
            tmb = 447.60 + (9.2 * peso) + (3.1 * altura) - (4.3 * idade)
        
        return tmb
    
    def GET(self, tmb, exercicio):
        tabela_fator = [1.2, 1.375, 1.375, 1.55, 1.55, 1.55, 1.725, 1.725] # 0, 1, 2, 3... dias

        if 0 <= exercicio <= 7:
            get = tmb * tabela_fator[exercicio]
            return f"seu gasto energético total diário é {get:.1f}"
        else:
            get = tmb * tabela_fator[0]
            return f"Como não existe um valor negativo ou acima de 7 dias na semana, assumi o resultado como uma pessoa sedentária \n o resultado do seu gasto energético total diário é {get:.1f}"

    def AGUA(self, peso):
        agua = (peso*35)/1000

        return f"Você precisa de no minimo {agua:.1f}L de água por dia"

nutri = Nutri()

print("vamos começar pedindo algumas informações para os nossos calculos \n")
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))
idade = int(input("Digite a sua idade: "))
genero = input("Seu Genero (F/M): ")
exercicio = int(input("Quantas vezes por semana você se exercita? "))
print(nutri.IMC(peso, altura))
print(nutri.TMB(peso, altura, idade, genero))
tmb = nutri.TMB(peso, altura, idade, genero)
print(nutri.GET(tmb, exercicio))
print(nutri.AGUA(peso))


