d =[
    {"id": "10","ProductName": "iPhone Xs Max 512GB","Price": "39.990.000","Company": "Apple","Distributor": "The gioi di dong","image": "https://cdn.tgdd.vn/Products/Images/42/191482/iphone-xs-max-512gb-gold-600x600.jpg"},
    {"id": "2","ProductName": "iPhone Xs Max 256GB","Price": "35.990.000","Company": "Apple","Distributor": "The gioi di dong","image": "https://cdn.tgdd.vn/Products/Images/42/190322/iphone-xs-max-256gb-white-600x600.jpg"}
]
def sapxep(val):
    return val["id"]

d.sort(key=sapxep,reverse=False)
print(d)
