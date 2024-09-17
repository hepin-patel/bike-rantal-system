class Bike:
    stock = 100
    price = 100
    def showStock(self):
        print("avilable stock : ",self.stock)
        print(f"price : {self.price} per quantity")

    def rent(self,r):
        if r<=self.stock:
            print(f"you booked {r} bike")
            print(f"total amount {r*self.price}")
            self.stock -= r
        else:
            print("no stock available.")
    def retu(self,r):
        if (self.stock+r)<=100:
            self.stock+=r   
        else:
            print("you enter wrong quantity.")

class Identity(Bike):
    i=dict()
    def identity(self,r):   # store user detail in dictionary form
        self.name=str(input("enter customer name : "))
        self.id=int(input("enter id number : "))
        self.i.update({self.id:{'name':self.name,'quantity':r}})

    def check(self): # check user name,id and quantity
        id = int(input("int your id : "))
        if id in self.i:
            name=self.i[id]['name']
            r=self.i[id]['quantity']
            print("name : " , name)
            print("quantity : ", r)
            self.retu(r)
        else:
            print("no booling found.")
           

    
a = Identity()
while 1:
    choice = int(input("""
    1. available stock and price
    2. rent
    3. return     
    4. exit             
    """))
    match choice:
        case 1:
            a.showStock()
        case 2:
            r = int(input("quantity : "))
            if r==0:
                print("please enter valid quantity.")
            else:
                a.identity(r)
                a.rent(r)
        case 3:
            a.check()
        case 4:
            break