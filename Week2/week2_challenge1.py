print("BMI 계산기 입니다.")
height= int(input("신장 : "))
weight= int(input("몸무게 : "))

bmi=weight/(height*height)*10000
print("BMI : ", bmi)