import math
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
    
    def GET(self, tmb, dias):
        tabela_fator = [1.2, 1.375, 1.375, 1.55, 1.55, 1.55, 1.725, 1.725] # 0, 1, 2, 3... dias

        if 0 <= dias <= 7:
            get = tmb * tabela_fator[dias]
            return get
        else:
            get = tmb * tabela_fator[0]
            return get
        
    def AGUA(self, peso):
        agua = (peso*35)/1000

        return f"Você precisa de no minimo {agua:.1f}L de água por dia"
    
    def MACRONU(self, get):

        gcarbo = (get*0,5)/4
        gpro = (get*0,25)/4
        ggord = (get*0,25)/6

        return f"Com base em uma dieta PADRÃO, o seu consumo de:\nCarboidratos = {gcarbo:.1f}\nProteina = {gpro:.1f}\nGorduras Totais = {ggord:.1f}"
    
    def GCE(self, tempo, peso):
        
        exercicios = ["Musculação", "Corrida", "Caminhada"]
        mets = [6, 8.3, 3.5] # musculação, corrida e caminhada
        concatena = ""
        for i in range(len(mets)):
            met = mets[i]
            exercicio = exercicios[i]
            kcal = met * peso * (tempo/60)

            concatena += f"\n{exercicio}: {kcal:.1} kcal gasta\n"

        return concatena

    def PORGORD(self, cintura, pescoco, altura, quadril, genero):

        altura = altura*100

        if genero.upper() == 'M':
            porcentual = 86.010*math.log10(cintura-pescoco)-70.041*math.log10(altura)+36.76
            
        else:
            porcentual = 163.205*math.log10(cintura+quadril-pescoco)-97.684*math.log10(altura)-78.387

        return porcentual
    
    def MASSCORP(self, peso, porcentual):
        mgorda = peso * (porcentual/100)
        mmagra = peso - mgorda

        return  f"Seu corpo é composto por {mgorda:.1}% de Massa Gorda e {mmagra:.1}% de Massa Magra"
    
    def DIETA(self, get):

        superavit = (get*0,15)+get
        deficit = get-(get*0,15)

        gcarbos = (superavit*0,5)/4
        gpros = (superavit*0,25)/4
        ggords = (superavit*0,25)/6

        gcarbod = (deficit*0,5)/4
        gprod = (deficit*0,25)/4
        ggordd = (deficit*0,25)/6
        

        return f"Para uma emagrecer ou ter um superávit calórico de forma saúdavel você deve ingerir respectivamente: \n{deficit:.1}Kcal \
            e as macros com base em uma dieta PADRÃO, o seu consumo de:\nCarboidratos = {gcarbod:.1f}\nProteina = {gprod:.1f}\nGorduras Totais = {ggordd:.1f} \
                \n{superavit:.1}Kcal e as macros com base em uma dieta PADRÃO, o seu consumo de:\nCarboidratos = {gcarbos:.1f}\n \
                Proteina = {gpros:.1f}\nGorduras Totais = {ggords:.1f}"

nutri = Nutri()

print("Vamos começar pedindo algumas informações para os nossos calculos \n")
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))
idade = int(input("Digite a sua idade: "))
genero = input("Seu Genero (F/M): ")
dias = int(input("Quantas vezes por semana você se exercita? "))
tempo = int(input("Geralmente por quantos minitos? "))


