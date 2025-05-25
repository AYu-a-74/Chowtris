class items:
    def __init__(self,name,cost,max_count):
        self.name=name
        self.cost=cost
        self.max_count=max_count
        self.count=0
    def can_purchase(self):
        return self.count<self.max_count
    def purchase(self):
        if self.can_purchase():
            self.count+=1
            return True
        return False
    def can_use(self):
        return self.count>0
    def use(self):
        if self.can_use():
            self.count-=1
            return True
        return False
bomb=items("Ktane",5,99)
boost=items("Gold Block",4,99)
bless=items("CHOW GOD'S BLESS",50,1)
AllItem=(bomb,boost,bless)
name_to_item={
    "bomb":bomb,
    "boost":boost,
    "bless":bless
}
def try_use(item_name):
    item = name_to_item.get(item_name)
    return item.use() if item else False
def apply_purchase(item_name):
    item = name_to_item.get(item_name)
    return item.purchase() if item else False
def get_inventory():
    return {
        "bomb": bomb.count,
        "boost": boost.count,
        "bless": bless.count > 0
    }