from datetime import datetime

name=input("enter your name:")
# list of items
lists='''
Rice  Rs 20/kg
Sugar Rs 30/kg
Oil   Rs 80/liter
Maggi Rs 50/kg
'''
price=0
pricelist=[]
totalprice=0
finalprice=0
ilist=[]
qlist=[]
plist=[]
#rates per item
items={'rice':20,
       'sugar':50,
       'oil':80,
       'maggi':30}
option=int(input("for listof items press 1 "))
if option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("if you want buy press 1 and 2 for exit:"))
    if inp1==2:
        break
    if inp1==1:
        item=input("enter your items:")
        quantity=int(input("enter quantity:"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("sorry you enterd item is not avilable")
    else:
        print("you enterd wrong number")
    inp=input("can i bill the items yes or no:")
    if inp=='yes':
        pass
        if finalamount!=0:
            print(25*"=","kutty supermarket",25*"=")
            print(28*" ","kurnool")
            print("Name:",30*" ","Date:",datetime.now())
            print(75*"-")
            print("sno",8*" ",'items',8*" ",'quantity',3*" ",'price')
            for i in range(len(pricelist)):
                print(i,8*' ',5*' ',ilist[i],3*' ',qlist[i],8*' ',plist[i]) 
                print(75*"-")
                print(50*" ",'TotalAmount:','Rs',totalprice)
                print("gst amount",40*" ",'Rs',gst)
                print(75*"-")
                print(50*" ",'finalAmount:','Rs',finalamount)
                print(75*"-")
                print(20*"-","Thanks for visiting")
                print(75*"-")