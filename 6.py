count = int(input("Nhập số: "))

tnod = 0
while (count > 0):
    tnod += 1
    count = count // 10

print("Số chữ số là:", tnod)