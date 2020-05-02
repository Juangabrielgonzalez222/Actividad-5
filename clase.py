class Alumno():
    __nombre=""
    __año=0
    __division=""
    __cantidad_inasistencias=0
    maximo_inasistencias=15
    total_de_clases=200
    def __init__(self,nombre="",año=0,division="",inasistencias=0):
        if(type(nombre)==str and type(año==int) and type(division)==str and type (inasistencias)==int):
            self.__nombre=nombre
            self.__año=año
            self.__division=division
            self.__cantidad_inasistencias=inasistencias
        else:
            print("Algún tipo de dato ingresado es incorrecto")
    def Retorna__Inasistencias(self):
        return self.__cantidad_inasistencias
    @classmethod 
    def RetornaMaximoInasistencias(cls):
        return cls.maximo_inasistencias
    def Retorna_Año(self):
        return self.__año
    def Retorna_Division(self):
        return self.__division
    def Retorna_nombre(self):
        return self.__nombre
    def Test(self):
        print("Funcion test:")
        self.__año=4
        self.__division="C"
        self.__nombre="Pruebas"
        self.__cantidad_inasistencias=3
        print(self.Retorna_Año())
        print(self.Retorna_Division())
        print(self.Retorna_nombre())
        print(self.RetornaMaximoInasistencias())