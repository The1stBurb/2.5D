#this is the area interpreter
#_ is normal grass,0
#-stone path,2
#~ water,4
#= is stone,6
#[space] is 8
#1 is wall grass
from main import pb,shift,block,pygame
from random import randint,seed
def noise(x, y, seed=0):
    # seed(seed)
    return ((x * 1234567 + y * 7654321 + seed * 9876543) & 0xFFFFFF) / 0xFFFFFF
class levelCrafter:
    def __init__(self):
        self.raw=[]
        self.area=[]
        self.shift={"_":0,"-":2,"~":4,"=":6," ":8}
        self.pure=[]
        self.get_raw()
        print(self.raw,self.area)
        self.purify()
        print(self.pure)
    def get_raw(self):
        areas=""
        with open("areas\\area.data","r")as area:
            self.area=area.readlines()
            areas="".join(self.area[0])
        for i in range(len(self.area)):
            self.area[i]=list(self.area[i])
        self.raw=[]
        # print(areas)
        for i in areas:
            with open(f"areas\\{i}.lvl","r")as lvl:
                # print(lvl.read())
                self.raw.append(lvl.read().split("\n"))
    def purify(self):
        for i in self.raw:
            self.pure.append([])
            for j in i:
                self.pure[-1].append([])
                for k in j:
                    if k in self.shift:
                        self.pure[-1][-1].append(self.shift[k])
                    else:
                        self.pure[-1][-1].append(-1)
    def combine(self):
        newImg=""
        for compute in range(len(self.pure)):
            newSrfce=pygame.Surface((block.sz*len(self.pure[compute][0]),block.sz*len(self.pure[compute])))
            for y,i in enumerate(self.pure[compute]):
                # comboSrfce=pygame.Surface((block.sz*len(self.pure[0][y]),block.sz))
                for x,j in enumerate(self.pure[compute][y]):
                    # print(j)
                    newSrfce.blit(pb.blur(shift[j],noise(x,y)),(x*block.sz,y*block.sz))
                # newSrfce.blit(comboSrfce,(0,y*block.sz))
                # break
            pygame.image.save(newSrfce,f"images\\levels\\level{compute+1}.png")
        # if side_by_side:
        #     combined_width = image1.get_width() + image2.get_width()
        #     combined_height = max(image1.get_height(), image2.get_height())
        # else:
        #     combined_width = max(image1.get_width(), image2.get_width())
        #     combined_height = image1.get_height() + image2.get_height()

        # # Create a new surface for the combined image
        # combined_surface = pygame.Surface((combined_width, combined_height))

        # # Blit the images onto the new surface
        # if side_by_side:
        #     combined_surface.blit(image1, (0, 0))
        #     combined_surface.blit(image2, (image1.get_width(), 0))
        # else:
        #     combined_surface.blit(image1, (0, 0))
        #     combined_surface.blit(image2, (0, image1.get_height()))

        # # Save the combined image
        # try:
        #     pygame.image.save(combined_surface, output_path)
        #     print(f"Combined image saved as {output_path}")
        # except pygame.error as e:
        #     print(f"Error saving image: {e}")
lvl=levelCrafter()
lvl.combine()