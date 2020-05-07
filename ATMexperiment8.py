class atm:
    def _init_(self,name):
        self.name=name
        
    def bal_inquiry(self):
        print("Balance in account number",data[name][0],"is",data[name][3])
    
    def pin_change(self):
        p=int(input("enter 4 digit pin:"))
        s=int(input("re-enter new pin:"))
        if(p==s):
            data[name][1]=p
            print("Your new pin is",data[name][1])
        else:
            print("You failed to change pin")
            
    def deposit(self):
        d_amount=int(input("enter the amount for deposit:"))
        data[name][3]=data[name][3]+d_amount
        print("You successfully deposit amount",d_amount)
        print("total amount",data[name][3])
        
    def withdraw(self):
        w_amount=int(input("enter the amount for withdraw:"))
        if data[name][3]<w_amount:
            print("You don't have required amount to withdraw:")
        elif w_amount<100:
            print("amount should be greater than RS.100")
        else:
            data[name][3]=data[name][3]-w_amount
            print("You successfully withdraw amount",w_amount)
            print("total amount is",data[name][3])
    
    def info(self):
        print("Name:",name)
        print("Account number:",data[name][0])
        print("Mobile number:",data[name][2])
        print("Account balance:",data[name][3])
            
    
data={"Madhura":[66763456,1223,9359827298,7000],

        "Apurva":[66798436,6787,9345627698,1000],

        "Radhika":[77823452,8795,9352365318,5000], 

        "Janvi":[76674563,2231,9327839210,6700],

        "Veera":[66637282,7829,9382718282,9000]}

name=input("enter the name:")

if name in data:
    obj=atm()
    count=3
    flag=0
    while count>0:
        p=int(input("enter the pin:"))
        if p==data[name][1]:
            flag=1
            break
        else:
            count=count-1
            print("wrong pin enter")
    if flag==1:
        x=int(input("1:Account Information,2:Pin change,3:Deposit,4:Withdraw,5:Balance Inquiry,6:Exit"))
        print()
        if x==1:
            obj.info()
        elif x==2:     
            obj.pin_change()
            
        elif x==3:
            obj.deposit()
            
        elif x==4:
            obj.withdraw()
            
        elif x==5:
            obj.bal_inquiry()
            
        elif x>6:
            print("enter values between 1 to 6:")
            
        elif x==6:
            print("exit")
    if count==0:
        print("account is blocked")
            
else:
    print("Data is not fount")
