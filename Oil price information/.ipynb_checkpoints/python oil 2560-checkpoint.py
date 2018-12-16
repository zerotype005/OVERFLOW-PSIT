import matplotlib.pyplot as plt
import pandas as pd
df_collect = pd.read_excel('/Users/User/Documents/GitHub/OVERFLOW-PSIT/Oil price information/2560.xlsx', sheet_name = 'ค่าเฉลี่ยราคาน้ำมันแต่ละเดือน')
List_x = df_collect['month'].tolist()
List_y1 = df_collect['Gasohol 91'].tolist()
List_y2 = df_collect['Gasohol 95'].tolist()
List_y3 = df_collect['Gasohol E20'].tolist()
List_y4 = df_collect['Gasohol E85'].tolist()
List_y5 = df_collect['Ultra Force Diesel'].tolist()
plt.plot(List_x, List_y1, label='Gasohol 91')
plt.plot(List_x, List_y2, label='Gasohol 95')
plt.plot(List_x, List_y3, label='Gasohol E20')
plt.plot(List_x, List_y4, label='Gasohol E85')
plt.plot(List_x, List_y5, label='Ultra Force Diesel')
plt.title('Oil Service Rate Price in 2560')
plt.xlabel('month')
plt.ylabel('price')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.show()
