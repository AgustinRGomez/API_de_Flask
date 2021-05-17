# llamo a las librerias de python que necesito
import pandas as pd
from flask import Flask,request
import json

app = Flask(__name__)

@app.route("/",methods = ['GET'])
def getDataJson():

    #creo los objetos
    Core = CountryFinder()
    Panda = PandaModel()
    PandaD = PandaDic()
       
    #asigno cada objeto con su respectiva ubicacion
       
    Core.PandaModel = Panda
    Core.PandaModel.PandaDic = PandaD
    
    #asigno las variables  
    V1 = request.args.get("V1")
    V2 = request.args.get("V2")
    # verifico los valores de V1 y V2
    if (float(V1) > float(V2)):
        return "V1 no debe ser mayor a V2"
        
    return json.dumps(Core.getCountriesBy(float(V1),float(V2)))
       
    
class CountryFinder:
    
    def _init_(self,PandaModel):
        self.PandaModel = PandaModel
        
    def getCountriesBy(self,condicion1,condicion2):
        panda = self.PandaModel.getAllCountries(condicion1,condicion2) 

        return panda


class PandaModel:
    def _init_(self,PandaDic):
        self.PandaDic = PandaDic
        
    def getAllCountries(self,condicion1,condicion2):
        
        #lee el archivo csv por medio de panda
        datos = pd.read_csv("C:\\Users\Liliana\\Downloads\\BLI_28032019144925238.csv",header = 0 )
        
        list_country = []
        df = pd.DataFrame(datos)
        alto = df.loc[0,"Value"]
        for i in range (1,len(df)):
            if df.loc[i,"Value"] >= condicion1 and df.loc[i,"Value"] <= condicion2:

                #asigno las variables para el diccionario
                self.PandaDic.country = df.loc[i,"Country"]
                self.PandaDic.value = df.loc[i,"Value"]
                #armo los diccionarios y los agrego una lista 
                self.PandaDic.getDiccionary(list_country)

        self.PandaDic.SortList(list_country)
        
        
        return list_country # me devolveria {"Country": country, "Value": value } ordenado


class PandaDic:
    #arma el diccionario con los datos obtenidos de la clase PandaModel
    def _init_(self,country,value):
        self.country = country
        self.value = value
        
    #agrega los diccionarios en la lista
    def getDiccionary(self,list_country):
        list_country.append({"Country": self.country, "Value": self.value })
        
    #ordena la lista de menor a mayor dependiendo de la variable Value
    def SortList(self,list_country):
        list_country.sort(key = lambda p: p["Value"])
        

        
if __name__ == "__main__":
    
    app.run(host = "localhost")
    
    
    
    
