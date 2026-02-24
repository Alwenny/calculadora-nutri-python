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
        
        return {
            "imc": imc,
            "classificação": classificacao
        }
    
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

        return agua
    
 #   def MACRONU(self, get):

 #       gcarbo = (get*0,5)/4
#        gpro = (get*0,25)/4
#        ggord = (get*0,25)/6

#      return f"Com base em uma dieta PADRÃO, o seu consumo de:\nCarboidratos = {gcarbo:.1f}\nProteina = {gpro:.1f}\nGorduras Totais = {ggord:.1f}"
    
    def GCE(self, tempo, peso):
        
        exercicios = ["Musculação", "Corrida", "Caminhada"]
        mets = [6, 8.3, 3.5] # musculação, corrida e caminhada
        resultados_gce = {}
        for i in range(len(mets)):
            met = mets[i]
            exercicio = exercicios[i]
            kcal = met * peso * (tempo/60)

            resultados_gce[exercicio] = kcal

        return resultados_gce

    def PORGORD(self, cintura, pescoco, altura, quadril, genero):

        cintura_in = cintura / 2.54
        pescoco_in = pescoco / 2.54
        quadril_in = quadril / 2.54
        altura_in = (altura * 100) / 2.54
        
        if genero.upper() == 'M':
            porcentual = 86.010 * math.log10(cintura_in - pescoco_in) - 70.041 * math.log10(altura_in) + 36.76
            
        else:
            porcentual = 163.205 * math.log10(cintura_in + quadril_in - pescoco_in) - 97.684 * math.log10(altura_in) - 78.387

        return porcentual
    
    def MASSCORP(self, peso, porcentual):
        mgorda = peso * (porcentual/100)
        mmagra = peso - mgorda

        return  {
            "massa_magra": mmagra,
            "massa_gorda": mgorda
        }
    
    def DIETA(self, get):

        superavit = (get*0.15)+get
        deficit = get-(get*0.15)

        gcarbos = (superavit*0.5)/4
        gpros = (superavit*0.25)/4
        ggords = (superavit*0.25)/6

        gcarbod = (deficit*0.5)/4
        gprod = (deficit*0.25)/4
        ggordd = (deficit*0.25)/6
        

        return {
            "kcal_deficit": deficit,
            "carbo_deficit": gcarbod,
            "pro_deficit": gprod,
            "gord_deficit": ggordd,
            
            "kcal_superavit": superavit,
            "carbo_superavit": gcarbos,
            "pro_superavit": gpros,
            "gord_superavit": ggords
        }
    


