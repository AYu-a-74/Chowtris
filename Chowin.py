class Chowin:
    def __init__(self):
        self.total=0
    def calculate_earnings(self,lines_cleared,level,boost_active=False):
        if level==4:
            multiplier=2
        else:
            multiplier=1
        if boost_active:
            multiplier*=2
        self.total=lines_cleared*multiplier
        return
    def try_spend(self,amount):
        if amount>self.total:
            return False
        self.total-=amount
        return True
    def reset(self):
        self.total=0
        return self.total