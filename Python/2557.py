import csv
import pygal
data55 = csv.reader(open('2557.txt'))
oil1 = []
price = []
oil2 = []
for i in data55:
    oil1.append(i)
for i in oil1:
    oil2.append(i[0])
for i in oil1:
    price.append(i[1])
print(oil2)
print(price)
line = pygal.Pie()
line.title = "ราคาน้ำมันเฉลี่ยของปี 2557"
line.x_labels = ("")
line.x_title = ('Price')
line.add(oil2[0], float(price[0]))
line.add(oil2[1], float(price[1]))
line.add(oil2[2], float(price[2]))
line.add(oil2[3], float(price[3]))
line.add(oil2[4], float(price[4]))
line.render_to_file('2557.svg')