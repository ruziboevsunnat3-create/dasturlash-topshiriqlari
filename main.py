class Avtobus:
    def __init__(self, raqami, marshrut, sigim):
        self.raqami = raqami
        self.marshrut = marshrut
        self.sigim = sigim
        self.yo_lovchilar = 0

    def chiqqanlar(self, soni):
        if self.yo_lovchilar + soni <= self.sigim:
            self.yo_lovchilar += soni
            return f"{soni} kishi chiqdi. Jami: {self.yo_lovchilar} ta."
        else:
            return "Joy yetarli emas!"

    def malumot(self):
        return f"Avtobus №{self.raqami}, Yo'nalish: {self.marshrut}, Sig'imi: {self.sigim} kishi."
avtobus1 = Avtobus(72, "Chorsu - Yunusobod", 50)
print(avtobus1.malumot())
print(avtobus1.chiqqanlar(10))
