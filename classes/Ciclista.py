class Ciclista:

    def __init__(self):
        self.__nombre=None
        self.__edad=None
        self.__pais=None
        self.__tiempo=None

    @property
    def nombre(self):
        return(self.__nombre)

    @property
    def edad(self):
        return(self.__edad) 

    @property
    def pais(self):
        return(self.__pais)

    @property
    def tiempo(self):
        return(self.__tiempo) 

    @nombre.setter
    def nombre(self,nombre):
        self.__nombre=nombre
    @edad.setter
    def edad(self,edad):
        self.__edad=edad
    @pais.setter
    def pais(self,pais):
        self.__pais=pais
    @tiempo.setter
    def tiempo(self,tiempo):
        if(tiempo<0):
            print("el tiempo no puede ser negativo")
        else:
            self.__tiempo=tiempo

    def calcularMenorTiempo(self):
        menor=10
        if(menor>self.tiempo):
            menor=self.tiempo

            datosCiclista={
              self.nombre,
              self.edad,
              self.pais,
              self.tiempo
            }

            return datosCiclista
        return 'el tiempo debe ser mayor a 0'

    def mostrarTiempo(self,datosCiclista):
        print(datosCiclista)