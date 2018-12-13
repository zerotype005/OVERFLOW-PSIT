import matplotlib.pyplot as plt
import pandas as pd
df_collect = pd.read_excel('2554.xlsx', sheet_name = 'ค่าเฉลี่ยราคาน้ำมันแต่ละเดือน')
List_x = df_collect['month'].tolist()
List_y = df_collect['Gasohol 91'].tolist()
plt.plot(List_x, List_y)
plt.xlabel('month')
plt.ylabel('price')
