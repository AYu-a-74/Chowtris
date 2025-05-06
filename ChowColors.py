class Colors:
    ChowRay=(0,0,0)
    OrigChow=(150,150,150)
    BaldChow=(0,255,200)
    OldChow=(200,0,0)
    ThiefChow=(100,0,200)
    PoliceChow=(255,225,0)
    YoungChow=(0,200,0)
    Tam=(0,100,225)
    @classmethod
    def get_cell_colors(cls):
        return [cls.ChowRay,cls.OrigChow,cls.BaldChow,cls.OldChow,cls.ThiefChow,cls.PoliceChow,cls.YoungChow,cls.Tam]