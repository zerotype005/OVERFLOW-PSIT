# Oil Service Rate Price(OSRP)
  เราศึกษาและวิเคราะห์ข้อมูลเกี่ยวกับอัตราราคาน้ำมันของปั๊ม ปตท. ตั้งแต่ปี 2554 ถึง 2560 เพื่อหาแนวโน้มของราคาน้ำมันที่อาจเกิดขึ้นในอนาคต และช่วงเดือนที่มีอัตราการเพิ่มลดของราคาน้ำมันเป็นจำนวนมากในแต่ละปี
## เราทำอะไร
เรานำอัตราราคาน้ำมันของปั๊ม ปตท.มาเพื่อหาแนวโน้มของราคานำ้มันที่อาจจะเกิดขึ้นในอนาคต โดยจะสรุปออกมาดังนี้
  1. Oil brand: 5 ชนิดของน้ำมันที่เป็นที่นิยม ได้แก่
      - Gasohol 91
      - Gasohol 95
      - Gasohol E20
      - Gasohol E85
      - UltraForceDiesel
  2. Oil pricing brand behavior: วิเคราะห์พฤติกรรมของราคาน้ำมันทั้ง 5 ชนิด
     - ราคาสูงหรือต่ำ
  3. Oil Price each years : กราฟราคาน้ำมันแต่ล่ะปีของทั้ง 5 ชนิด ตั้งแต่ปี พ.ศ.2554 ถึง พ.ศ.2560

## ข้อมูลที่นำมาวิจัย
 - ข้อมูลราคาน้ำมันจากเว็บกลางปตท. ตั้งแต่วันที่ 1 มกราคม พ.ศ.2554 ถึงวันที่ 31 ธันวาคม พ.ศ.2560
 - ข้อมูลมีขนาด 209 KB

## 3rd Party Libraries และ modules
 - matplotlip 2.2.2
 - pandas 0.23.0
 - pygal 

## Output
ข้อมูลที่ผ่านการประมวลผลแล้วจะถูกจัดเก็บเป็น Dictionary และถูกบันทึกลงบน Local Storage ด้วย Pickle หลังจากนั้นข้อมูลถูกนำมาแสดงผลเป็นกราฟผ่าน graph.py

## ผลลัพธ์
ผลลัพธ์งานวิจัยได้ถูกแสดงไว้บนเว็บไซต์ของเรา
https://www.it.kmitl.ac.th/~it61070177/psit/index.html#introduction

Made with love
OVERFLOW Team
