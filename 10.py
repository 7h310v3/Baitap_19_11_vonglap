import math

lim = int(input("Nhập giới hạn: "))
num = 1

while (lim < 0):
  if (lim < 0):
    print("Nhập sai, xin nhập lại !(> 0)")
    lim = int(input("Nhập giới hạn: "))

print("Prime number: ", end = " ")

while (num <= lim):
    count = 0
    tmp = 2
    while (tmp <= math.sqrt(num)):
        if ((num % tmp) == 0):
            count = count + 1
        tmp = tmp + 1
    if (count == 0 and num != 1):
        print(num, end = " ")
    num = num + 1