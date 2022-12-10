import datetime
today = datetime.date.today()
print(type(today))
print(today)

data1 = today.strftime("dzisiaj jest %d dzień ....%m miesiąca")
data2 = today.strftime('%d--%m--%y')
print(data2)

my_now = now.strftime('%H:%M:%S')
print(my_now)



