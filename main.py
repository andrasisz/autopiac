import modul as m

autok=[]

for sor in open("autopiac.txt",encoding="utf-8"):
    autok.append(m.Auto(sor))

print(f"Az autók összértéke {m.osszertek(autok)} Ft.")
print(f"{m.opelek(autok)} darab Opel van az autók között.")
min=m.legidosebb(autok)
print("A legrégebbi autó")
print(f"\ttípusa: {autok[min].tipus}")
print(f"\tévjárata: {autok[min].ev}")
print(f"\tára: {autok[min].ar}")

print(f"A Skodák átlagos ára {m.skodak(autok)} Ft.")