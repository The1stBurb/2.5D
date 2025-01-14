#this is the area interpreter
#_ is normal grass,0
#-stone path,2
#~ water,4
#= is stone,6
#[space] is 8
#1 is wall grass
from main import pb,shift
class levelCrafter:
    def __init__(self):
        self.raw=[]
        self.area=[]
        self.shift={"_":0,"-":2,}
        self.pure=[]
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
        for i in self.raw:
            self.pure.append([])
            for j in i:
                self.pure[-1].append([])
                for k in j:
                    self.pure[-1][-1].append(self.shift[k])
    def combine(self):
        newImg=""
        for i in 
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