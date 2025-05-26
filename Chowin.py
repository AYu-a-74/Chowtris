class Chowin:#The shop currency
    def __init__(self):
        self.total=0
    def calculate_earnings(self,lines_cleared,level,boost_active=False):#How much Chowins do you earn?
        if level==4:
            multiplier=4
        else:
            multiplier=1
        if boost_active:
            multiplier*=2
        self.total=lines_cleared*multiplier
        return
    def try_spend(self,amount):#If you try to use your Chowins
        if amount>self.total:
            return False
        self.total-=amount
        return True
    def reset(self):#Resetting Choins once you leave shop.
        #The reason why your Chowins reset is beacuse the zombie NPC really dislike wasting money, so he helps you to keep your Chowins, but he never really give them back. Haha.
        self.total=0
        return self.total