# Title       : Chapter : 1 - item : 2 - if-elif
# Question    : โจทย์: จงเขียนโปรแกรมรับความเร็วลมเฉลี่ยใน 10 นาที และแสดงผลระดับพายุที่เกิดขึ้น จากการจัดแบ่งความเร็วลมดังนี้

# 		Speed (km/h)		ระดับพายุ
# 			0-51.99			Breeze
# 			52.00-55.99		Depression
# 			56.00-101.99	Tropical Storm
# 			102.00-208.99	Typhoon
# 			>= 209			Super Typhoon

# โดยแสดงผลตามตัวอย่างการแสดงผล

print(" *** Wind classification ***")
speed = float(input('Enter wind speed (km/h) : '))

if speed    >= 209  : print("Wind classification is Super Typhoon.")
elif speed  >= 102  : print("Wind classification is Typhoon.")
elif speed  >= 56   : print("Wind classification is Tropical Storm.")
elif speed  >= 52   : print("Wind classification is Depression.")
elif speed  >= 0    : print("Wind classification is Breeze.")

'''
# ----------------------- TESTCASE ZONE -----------------------
# TESTCASE 1
 *** Wind classification ***
Enter wind speed (km/h) : 50
Wind classification is Breeze.

# TESTCASE 2
 *** Wind classification ***
Enter wind speed (km/h) : 56.2
Wind classification is Tropical Storm.

# TESTCASE 3
 *** Wind classification ***
Enter wind speed (km/h) : 99.89
Wind classification is Tropical Storm.

# TESTCASE 4
 *** Wind classification ***
Enter wind speed (km/h) : 212
Wind classification is Super Typhoon.

# TESTCASE 5
 *** Wind classification ***
Enter wind speed (km/h) : 254.23
Wind classification is Super Typhoon.

'''