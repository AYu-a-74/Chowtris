class Chowin:
    def __init__(self):
        self.total=0
    def calculate_earnings(self,lines_cleared,level):
        earned=lines_cleared*(2 if level==4 else 1)
        self.total=earned
        return
    def try_spend(self,amount):
        if amount>self.total:
            return False
        self.total-=amount
        return True
    def reset(self):
        self.total=0
        return self.total