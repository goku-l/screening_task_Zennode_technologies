import math
print("Product Name     Price")
print("Product A        $20")
print("Product B        $40")
print("Product C        $50")

quantities=[]
gift=[]
discountname=""
finaldiscount=0
flat10=0
bulk5=0
bulk10=0
tiered50=0
giftfee=0
shippingfee=0

quantities.append(int(input("Enter the quantity of product A    ")))
gift.append(int(input("Press 1 for gift wrapping , otherwise press 0    ")))

quantities.append(int(input("Enter the quantity of product B    ")))
gift.append(int(input("Press 1 for gift wrapping , otherwise press 0    ")))

quantities.append(int(input("Enter the quantity of product C    ")))
gift.append(int(input("Press 1 for gift wrapping , otherwise press 0    ")))

subtotal=quantities[0]*20+quantities[1]*40+quantities[2]*50

if subtotal>200:
    flat10=10

if quantities[0]>10 or quantities[1]>10 or quantities[2]>10:
    bulk5=0
    if quantities[0]>10:
        bulk5+=quantities[0]*20*0.05
    if quantities[1]>10:
        bulk5+=quantities[1]*40*0.05
    if quantities[2]>10:
        bulk5+=quantities[2]*50*0.05
    
if (quantities[0]+quantities[1]+quantities[2])>20:
    bulk10=0.1*subtotal

if ((quantities[0]+quantities[1]+quantities[2])>30) and (quantities[0]>15 or quantities[1]>15 or quantities[2]>15):
    tiered50=0
    if quantities[0]>15:
        tiered50+=(0.5*(quantities[0]-15)*20)
    if quantities[1]>15:
        tiered50+=(0.5*(quantities[1]-15)*40)
    if quantities[2]>15:
        tiered50+=(0.5*(quantities[2]-15)*50)

finaldiscount=max(flat10,bulk5,bulk10,tiered50)

if finaldiscount==flat10:
    discountname="flat_10_discount"
elif finaldiscount==bulk5:
    discountname="bulk_5_discount"
elif finaldiscount==bulk10:
    discountname="bulk_10_discount"
elif finaldiscount==tiered50:
    discountname="tiered_50_discount"

if gift[0]==1:
    giftfee+=quantities[0]
if gift[1]==1:
    giftfee+=quantities[1]
if gift[2]==1:
    giftfee+=quantities[2]

shippingfee=math.ceil((quantities[0]+quantities[1]+quantities[2])/10)*5

print("Product A    quantity :",quantities[0],"     total amount of Product A : $",20*quantities[0])

print("Product B    quantity :",quantities[1],"     total amount of Product B : $",40*quantities[1])

print("Product C    quantity :",quantities[2],"     total amount of Product C : $",50*quantities[2])

print("Subtotal : $",subtotal)

print("discount name :",discountname,"      discount amount : $",finaldiscount)

print("Shipping fee : $",shippingfee,"       gift wrapping fee : $",giftfee,"      shipping and gift wrapping fee : $",giftfee+shippingfee)

print("Total : $",subtotal+shippingfee+giftfee-finaldiscount)
