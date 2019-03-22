import dataclasses

@dataclasses.dataclass
class BaseDriver:
    viewgase__ : int
    pathvert__ : list
    money__  : int
    name__ : str
    prioritygase : str

    def __init__(self,name,viewgase, pathvert, money, prioritygase):
        self.viewgase__ = viewgase
        self.name__ = name
        self.money__ = money
        self.pathvert__ = pathvert
        self.prioritygase = prioritygase

    def get_money(self):
        return self.money__

    def get_paths(self):
        return self.pathvert__

    def get_viewgase(self):
        return self.viewgase__

    def get_priority(self):
        return  self.prioritygase