class Database_createion():
    def Information(self):
        self.id=id
        print("Create Account for ",self.id)
        self.name=str(input(f"Enter the name:"))
        self.age=int(input(f"Enter the age:"))
        self.address=str(input(f"Address:"))
        self.phn=str(input(f"Phone Number:"))
        self.balance=float(input("Enter your starting balance:"))
    def Withdraw(self):
        w_balance=float(input("Amount:"))
        if(self.balance<w_balance):
            print("Sorry!You do not have sufficiant balance.")
            self.w1_balance = float(input(f"Input again\nYour current balance is:{self.balance}\n-"))
            assert self.w1_balance >= self.balance, "Your process is terminated."
        else:
            self.balance = self.balance - w_balance
    def addMoney(self):
        a_balance = float(input("Amount:"))
        self.balance=self.balance+a_balance
    def Transfer_add(self,amount):
        self.balance=self.balance+amount
    def Transfer_draw(self,amount):
        self.balance=self.balance-amount
    def Display(self):
        print("Id=",self.id)
        print("Name=",self.name)
        print("Age=",self.age)
        print("Address=",self.address)
        print("Phone number:",self.phn)
        print("Current Balance:",self.balance)
Data=list()
id=1250
n=int(input("Enter the number of Accounts Holder:"))
File=open("Database.txt","a")
for i in range(0,n):
    id=id+1
    Data.append(0)
    Data[i]=Database_createion()
    Data[i].Information()
    print("The Account is created.Press Enter to continue:")
    str(input())
while(True):
    choice=int(input("Do you want more operation:\n1.Yes\t2.No\n-"))
    if(choice==1):
        id_n=int(input("Enter your id:"))
        choice=int(input("Which operation you want to perform:\n1.Add Money\t2.Withdraw\t3.Display\t4.Transfer\n-"))
        id_n=id_n-1251
        if(choice==1):
            Data[id_n].addMoney()
        elif(choice==2):
            Data[id_n].Withdraw();
        elif(choice==3):
            Data[id_n].Display()
        elif(choice==4):
            money=float(input("Enter amount:"))
            if(money>Data[id_n].balance):
                print("Sorry!You do not have sufficiant balance.")
                money = float(input(f"Input again\nYour current balance is:{Data[id_n].balance}\n-"))
            id_d=int(input("Where you want to send:"))
            id_d=id_d-1251
            Data[id_d].Transfer_add(money)
            Data[id_n].Transfer_draw(money)
        else:
            print("Invalid Choice.")
    else:
        break;
print("Processing\n")
for i in range(0,n):
    File.write(f"Name:{Data[i].name}\n")
    File.write(f"ID:{Data[i].id}\n")
    File.write(f"Age:{Data[i].age}\n")
    File.write(f"Address:{Data[i].address}\n")
    File.write(f"Phone number:{Data[i].phn}\n")
    File.write(f"Balance:{Data[i].balance}\n\n\n")
print("Processing is finished.\n")
File.close()
