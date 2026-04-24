products=[
    {'name':'laptop','price':1200,'in_stock':True},
    {'name':'mouse','price':50,'in_stock':True},
    {'name':'monitor','price':650,'in_stock':False},
    {'name':'gaming_pc','price':2500,'in_stock':True},
]
for p in products:
    if p["price"]>500 and p["in_stock"] and p["name"]:
        print(p["name"])