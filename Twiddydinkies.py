class items:#Powerful items!
    def __init__(self,name,cost,max_count):#Initialize what you can use
        self.name=name
        self.cost=cost
        self.max_count=max_count
        self.count=0
    def can_purchase(self):#If you can buy or not
        return self.count<self.max_count
    def purchase(self):#Buy item
        if self.can_purchase():
            self.count+=1
            return True
        return False
    def can_use(self):#If you can use the item or not
        return self.count>0
    def use(self):#To use the item
        if self.can_use():
            self.count-=1
            return True
        return False
#Items
bomb=items("Ktane",5,99)
boost=items("Gold Block",4,99)
bless=items("CHOW GOD'S BLESS",50,1)
AllItem=(bomb,boost,bless)
name_to_item={
    "bomb":bomb,
    "boost":boost,
    "bless":bless
}
def try_use(item_name):#Try to use the item
    item = name_to_item.get(item_name)
    return item.use() if item else False
def apply_purchase(item_name):#Try to purchase the item
    item = name_to_item.get(item_name)
    return item.purchase() if item else False
def get_inventory():#Items in your inventory
    return {
        "bomb": bomb.count,
        "boost": boost.count,
        "bless": bless.count > 0
    }