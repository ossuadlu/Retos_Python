class Formula1:
    def __init__(self,nombre,motor,piloto,costoAnual):
        self.nombre=nombre
        self.motor=motor
        self.piloto=piloto
        self.costoAnual=costoAnual

    def  ingresarEscuderia(self,escuderia):
        escuderia=input('Digite escuderia de formula1: ')