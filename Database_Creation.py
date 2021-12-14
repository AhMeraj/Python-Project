class Database_createion():
    def Information(self):
        self.id=id
        print("Create Database for ",self.id)
        File.write(f"\n\nDatabase for ID-{self.id}\n")
        self.name=str(input(f"Enter the name:"))
        File.write(f"Name:{self.name}\n")
        self.age=int(input(f"Enter the age:"))
        File.write(f"Age:{self.age}\n")
        self.edu=str(input(f"Educational Qualification:"))
        File.write(f"Educational Background:{self.edu}\n")
        self.skills=str(input(f"Skills:"))
        File.write(f"Skills:{self.skills}\n")
        self.exp=str(input(f"Experience:"))
        File.write(f"Experiences:{self.exp}\n")
    def Display(self):
        print("Id=",self.id)
        print("Name=",self.name)
        print("Age=",self.age)
        print("Educational Background=",self.edu)
        print("Skills:",self.skills)
        print("Experience:",self.exp)
Data=list()
id=1250
n=int(input("Enter the number of Information:"))
File=open("Database.txt","a")
for i in range(0,n):
    id=id+1
    Data.append(0)
    Data[i]=Database_createion()
    Data[i].Information()
    print("Your Information is created.Press Enter to continue:")
    str(input())
File.close()
# id_n=int(input("Enter Your ID:"))
# for i in range(0,n):
#     if(id_n==Data[i].id):
#         Data[i].Display()
#         break;
#     elif(i==n-1):
#         print("Sorry")
