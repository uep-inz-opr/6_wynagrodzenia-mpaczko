
class Pracownik:
    def __init__(self,name,brutto):
        self.name = str(name)
        self.brutto = int(brutto)

    def oblicz(self):
        emr = round(self.brutto * 0.0976, 2)
        rent = round(self.brutto * 0.015, 2)
        chor = round(self.brutto * 0.0245, 2)
        pom=round(self.brutto - (emr+rent+chor),2)
        zdrow = round(pom *0.09 , 2)
        pdst_pod=round(((pom-111.25)*0.18 -46.33),2)
        zdrow_do_od=round(pom*0.0775,2)
        tax_doch=round((pdst_pod-zdrow_do_od),0)
        netto=round(pom-zdrow-tax_doch,2)
        x=round(self.brutto*0.065,2)
        fgsp=round(self.brutto*0.001,2)
        wypad=round(self.brutto*0.0193,2)

        skl_prac=round(emr+x+wypad+chor+fgsp,2)
        koszt_prac=round(skl_prac+self.brutto,2)
        self.laczny_koszt=round(float(self.brutto)+skl_prac,2)
        result = self.name+' ' + '{:.2f}'.format(netto) + ' ' + '{:.2f}'.format(skl_prac) + ' ' + '{:.2f}'.format(koszt_prac)
        return result

    def return_koszt_calk(self):
        return int(self.laczny_koszt)


pracownicyArr=int(input())
arr=[]
laczny_koszt=0

for i in range(pracownicyArr):
    pracownikData=input().split(" ")
    name = pracownikData[0]
    brutto = pracownikData[1]
    pracownik=Pracownik(name, brutto)
    arr.append(pracownik.oblicz())
    laczny_koszt+=pracownik.return_koszt_calk()
for wynik in arr:
    print(wynik)

print(('{:.2f}').format(laczny_koszt))     

