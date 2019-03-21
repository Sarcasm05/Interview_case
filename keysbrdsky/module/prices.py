import dataclasses

@dataclasses.dataclass
class BasePrices:
    b_92_ : int
    b_95_ : int
    b_98_ : int

    b_d__: int
    b_g__: int
    b_name__ : str

    def __init__(self, b_92, b_95, b_98, b_d_, b_g_, b_n):
        self.b_92__ = b_92
        self.b_95__ = b_95
        self.b_98__ = b_98
        self.b_d__ = b_d_
        self.b_g__ = b_g_
        self.b_name__ = b_n

    def __init__(self):
        self.__init__(-1,-1,-1,-1,-1,'test')

    def __init__(self, b_92, b_95, b_98,b_g, b_n):
        self.__init__(b_92, b_95,b_98, -1, b_n)

    def get_name(self):
        return self.b_name__


    def convert_rub_dol(self):
        return  ''

    def convert_dol_rub(self):
        return ''

