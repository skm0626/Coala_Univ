print("4 자리 정수 계산기 입니다.")
number = int(input("정수를 입력해 주세요."))

sum = 0

digit1=number//1000
number=number%1000
digit2=number//100
number=number%100
digit3=number//10
number=number%10
digit4=number
sum=digit1+digit2+digit3+digit4

print(sum)