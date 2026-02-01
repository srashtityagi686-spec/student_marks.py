class college:
    def student(self):
        name=input("enter the name")
        phone=int(input("enter your phone number"))
        email=input("enter your email")
    def marks(self):
        math=eval(input("enter the math marks"))
        physics=eval(input("enter the physics marks"))
        chemistry=eval(input("enter the chemistry marks"))
        hindi=eval(input("enter the hindi marks")) 
        english=eval(input("enter the english marks"))
        total=math+physics+chemistry+hindi+english
        print(total)
        percentage=(total/500)*100
        print(percentage)
c1=college()
choice=eval(input("enter your choice:"))
if choice==1:
    c1.student()
elif choice==2:
    c1.marks() 
else:
    print("invalid choice")       
