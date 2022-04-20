number=input("정수를 입력해주세요.")

sum=0

for i in range(len(number)):
    sum+=int(number)%10
    number=int(number)//10
    number=str(number)

print(sum)

# for n in number:
#     sum=sum+int(n)
# print(sum)