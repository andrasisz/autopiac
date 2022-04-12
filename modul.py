class Auto:
    def __init__(self,sor):
        s=sor.strip().split(';')
        self.rsz=s[0]
        self.tipus=s[1]
        self.ev=int(s[2])
        self.ar=int(s[3])

def osszertek(autok_listaja):
    osszeg=0
    for i in autok_listaja:
        osszeg+=i.ar
    return osszeg

def opelek(autok_listaja):
    db=0
    for i in autok_listaja:
        if i.tipus=="Opel":
            db+=1
    return db

def legidosebb(autok_listaja):
    min=0
    for i in range(1,len(autok_listaja)):
        if autok_listaja[i].ev<autok_listaja[min].ev:
            min=i
    return min

def skodak(autok_listaja):
    osszeg=0
    db=0
    for i in autok_listaja:
        if i.tipus=="Skoda":
            osszeg+=i.ar
            db+=1
    return round(osszeg/db)