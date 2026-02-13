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
        
        return f"sua taxa metabolica basal é {tmb:.1f}"
    
    def GET(self):
        
    
nutri = Nutri()

peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))
idade = int(input("Digite a sua idade: "))
genero = input("Seu Genero (F/M): ")

print(nutri.IMC(peso, altura))
print(nutri.TMB(peso, altura, idade, genero))


