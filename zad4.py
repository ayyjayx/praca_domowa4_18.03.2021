class NaZakupy:
    def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
        self.nazwa_produktu = nazwa_produktu
        self.ilosc = ilosc
        self.jednostka_miary = jednostka_miary
        self.cena_jed = cena_jed
    def wyswietl_produkt(self):
        print(self.nazwa_produktu, self.ilosc, self.jednostka_miary, self.cena_jed)
    def ile_produktu(self):
        print(self.ilosc, self.jednostka_miary)
    def ile_kosztuje(self):
        print(self.ilosc * self.cena_jed)
zakupy = NaZakupy("chipsy lays strong ogniste skrzydelka parzy mocno fest masniutki smak", 0.3, "kg", 18)
zakupy.wyswietl_produkt()
zakupy.ile_produktu()
zakupy.ile_kosztuje()