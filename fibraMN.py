
class Celula:
    pass


class FibraMusculara(Celula):

    def __init__(self, nume, masa_musculara):
        self.__nume = nume
        self.__masa_musculara = masa_musculara

    def get_nume(self):
        return self.__nume

    def get_masa_musculara(self):
        return self.__masa_musculara


class FibraNervoasa(Celula):

    def __init__(self, nume, lungime):
        self.__nume = nume
        self.__lungime = lungime

    def get_nume(self):
        return self.__nume

    def get_lungime(self):
        return self.__lungime


class MuschiGeneric:

    def __init__(self, fibre, nume, scop):
        self.__fibre = fibre
        self.__nume = nume
        self.__scop = scop

    def get_nume(self):
        return self.__nume

    def get_scop(self):
        return self.__scop

    def get_masa_muscolara(self):
        masa_musculara = 0
        for fibra in self.__fibre:
            masa_musculara += fibra.get_masa_musculara()
        return masa_musculara

    def __str__(self):
        return str(self.__nume) + ", scop: " + str(self.__scop) + ", cu fibre de " + str(self.get_masa_muscolara())


class MuschiBiceps(MuschiGeneric):

    def __init__(self, fibre):
        super().__init__(fibre, "Biceps", {"locomotor", "incordare brat"})


class MuschiTriceps(MuschiGeneric):

    def __init__(self, fibre):
        super().__init__(fibre, "Triceps", {"extensor", "relaxare brat"})


class MuschiPicior(MuschiGeneric):

    def __init__(self, fibre):
        super().__init__(fibre, "Gamba", {"locomotor", "miscare glezna"})


class TrunchiNervos:

    def __init__(self, nervi, nume, specializare):
        self.__nervi = nervi
        self.__nume = nume
        self.__specializare = specializare

    def get_nume(self):
        return self.__nume

    def get_specializare(self):
        return self.__specializare

    def get_lungime(self):
        lungime = 0
        for nerv in self.__nervi:
            lungime += nerv.get_masa_musculara()
        return lungime


class TrunchiNervosDinColoana(TrunchiNervos):

    def __init__(self, nervi):
        super().__init__(nervi, "Trunchiu' nervos din coloana", "coordonare")


f1 = [FibraMusculara("fibraMusculara1", 21), FibraMusculara("fibraMusculara4", 3)]
f2 = [FibraMusculara("fibraMusculara2", 3), FibraMusculara("fibraMusculara5", 7)]
f3 = [FibraMusculara("fibraMusculara3", 1.1), FibraMusculara("fibraMusculara6", 0.25)]

m1 = MuschiPicior(f1)
m2 = MuschiBiceps(f2)
m3 = MuschiTriceps(f3)

muschi = [m1, m2, m3]

print("Toti muschii:")
for muscle in muschi:
    print(muscle)

print()
print("Muschi locomotori:")
for muscle in muschi:
    if "locomotor" in muscle.get_scop():
        print(muscle)
