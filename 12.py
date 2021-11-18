num = int(input("Nhập số cần tính: "))

while (num < 0):
    if (num < 0):
        print("Nhập sai, xin nhập lại!(> 0)")
        num = int(input("Nhập số cần tính: "))

fac = 1
tmp = 1

while (tmp <= num):
    fac = fac * tmp
    tmp = tmp + 1

print(num, "! =", fac)