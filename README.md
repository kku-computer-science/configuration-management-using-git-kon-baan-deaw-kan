โปรเจกต์นี้เป็นส่วนหนึ่งของวิชา CP353004 Software Engineering  
กิจกรรม Lab 3.3: Working with Collaborators  
ภาคการศึกษา 2/2568

โครงการนี้มีวัตถุประสงค์ให้สมาชิกในทีมร่วมกันพัฒนาโปรแกรมสำหรับเรียงลำดับข้อมูล (Sorting)  
โดยใช้โครงสร้างและขั้นตอนการทำงานผ่าน Git / GitHub / GitHub Classroom ตามหลักการของ Configuration Management

---

## สมาชิกทีม
- ธงชัย สีสาร (663380595-6) – พัฒนา Quick Sort + Test และ merge รวมทั้งหมดเข้าสู่ main
- ธนัชชา คำไล้ (663380386-5) – พัฒนา Bubble Sort + Test
- ธรานนท์ สุขตัว (663380387-3) – พัฒนา Main Program และ Input Handler

---

## โครงสร้างโปรเจกต์
```
Project/
│── quick_sort.py          # อัลกอริทึม Quick Sort
│── bubble_sort.py         # อัลกอริทึม Bubble Sort
│── input_handler.py       # จัดการรับข้อมูลจากผู้ใช้
│── main.py                # โปรแกรมหลัก แสดงผลและเลือกอัลกอริทึม
│── test_quick_sort.py     # ทดสอบ Quick Sort
└── test_bubble_sort.py    # ทดสอบ Bubble Sort
```

---

# วิธีใช้งานโปรแกรม
## 1) Run แบบปกติ (Interactive Mode)
รัน:
โปรแกรมจะให้เลือกโหมด: <br>
==== Sorting Program ==== <br>
1.Quick Sort <br>
2.Bubble Sort <br>
3.Exit <br>
<br> 
จากนั้นกรอกตัวเลข เช่น: <br>
Enter numbers: 5 1 9 2

### ตัวอย่างผลลัพธ์
Algorithm: Quick Sort  <br> 
Input : [5, 1, 9, 2]  <br>
Sorted: [1, 2, 5, 9]  <br>

---

## 2) Run แบบ CLI arguments (Non-Interactive)
สามารถส่งค่าผ่าน command line ได้ เช่น: <br>
python main.py "5, 2, 9, 1" quick
หรือ <br>
python main.py "10 3 7 1" bubble <br>

### ผลลัพธ์
[1, 3, 7, 10]

### รูปแบบ argument
python main.py "<ตัวเลขคั่นด้วย space หรือ comma>" <algorithm>

algorithm ที่รองรับ:
- quick, quicksort, q
- bubble, bubblesort, b

## การ Run Test  
โปรเจกต์นี้มีไฟล์เทส เช่น `test_quick_sort.py` อยู่ในโฟลเดอร์โปรเจกต์
สามารถรันเทสได้ดังนี้:
1) ติดตั้ง pytest (ครั้งแรกเท่านั้น) <br>
   python -m pip install pytest <br>

2) ไปที่โฟลเดอร์โปรเจกต์ <br>
   "E:\Study\T3\Software Engineer\configuration-management-using-git-kon-baan-deaw-kan\Project" <br>

3) ใช้ pytest <br>
   python -m pytest -q
   
---




