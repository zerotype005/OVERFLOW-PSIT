import matplotlib.pyplot as plt
import pandas as pd

def analyze_data(filename, sheetname):

    # Data preparation
    df_collect = pd.read_excel(filename, sheet_name = sheetname)
    List_x = df_collect['month'].tolist()
    List_y1 = df_collect['Gasohol 91'].tolist()
    List_y2 = df_collect['Gasohol 95'].tolist()
    List_y3 = df_collect['Gasohol E20'].tolist()
    List_y4 = df_collect['Gasohol E85'].tolist()
    List_y5 = df_collect['Ultra Force Diesel'].tolist()

    # Plot
    fig = plt.figure()
    ax = plt.subplot(111)
    ax.plot(List_x, List_y1, label='Gasohol 91')
    ax.plot(List_x, List_y2, label='Gasohol 95')
    ax.plot(List_x, List_y3, label='Gasohol E20')
    ax.plot(List_x, List_y4, label='Gasohol E85')
    ax.plot(List_x, List_y5, label='Ultra Force Diesel')
    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width * 0.75, box.height])
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.title("Average Prices of Different Types of Gasolines in " + filename[:7])
    plt.xlabel('month')
    plt.ylabel('price')
    plt.show()

if __name__ == "__main__":
    
    # This data contains
    #   {
    #       filename: sheet name
    #   }

    data = {
        "2554.xlsx": "ค่าเฉลี่ยราคาน้ำมันแต่ละเดือน",
        "2555.xlsx": "ราคาเฉลี่ย",
        "2556.xlsx": "ราคาเฉลี่ย",
        "2557.xlsx": "ราคาเฉลี่ย",
        "2558.xlsx": "ค่าเฉลี่ยราคาน้ำมันแต่ละเดือน",
        "2559.xlsx": "ค่าเฉลี่ยราคาน้ำมันแต่ละเดือน",
        "2560.xlsx": "ค่าเฉลี่ยราคาน้ำมันแต่ละเดือน"
    }

    for year in data:
        print("Data year:", year, "||", "Sheet name:", data[year])
        analyze_data(year, data[year])
