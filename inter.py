#this is the area interpreter
#_ is normal grass,0
#-stone path,2
#~ water,4
#= is stone,6
#1 is wall grass
class levelCrafter:
    def __init__(self):
        self.raw=[]
        self.area=[]
        self.shift={"_":0,"-":2,}
    def get_raw(self):
        areas=""
        with open("areas\\area.data","r")as area:
            self.area=area.readlines().split("\n")
            areas=area.read()
        for i in range(len(self.area)):
            self.area[i]=list(self.area[i])
        self.raw=[]
        for i in areas:
            with open(f"areas\\{i}.lvl","r")as lvl:
                self.raw.append(lvl.readlines())
    def purify(self):
