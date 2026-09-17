#programesanas valoda ir python


#1.1 uzdevums
class CSDD:
    def __init__(self, Zimols, Modelis, Registracijas_datums, Masa, Degviela):
        self.Zimols = Zimols
        self.Modelis = Modelis
        self.Registracijas_datums = Registracijas_datums
        self.Masa = Masa
        self.Degviela = Degviela

Auto_tests = CSDD
zimols="BMW"
modelis="E91"
Registracijas_datums="13.04.2007"
Masa="2100kg"
Degviela="DE"   

print(zimols, modelis, Registracijas_datums, Masa, Degviela)

#2.0
class Kubs:
    def __init__(self, Malas_garums, Krasas_nosaukums, Aprekinat_tilpumu):
        self.Malas_garums = Malas_garums
        self.Krasas_nosaukums = Krasas_nosaukums
        self. Aprekinat_tilpumu = Aprekinat_tilpumu

def Aprekinat_tilpumu(self, tilpums, mala):
    self.tilpums = tilpums
    self.mala = mala
    tilpums = mala*mala*mala

kubg = Kubs.Aprekinat_tilpumu()
Mala_garums="10cm"
Krasa="Zala"



print(Mala_garums, Krasa)

kubr = Kubs
Mala_garums="1cm"
Krasa="Sarkana"

print(Mala_garums, Krasa)


