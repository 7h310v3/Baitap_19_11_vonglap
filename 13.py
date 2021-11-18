num = int(input("Nhập số cần đảo: "))
change = 0

while (num > 0):
    tmp = num % 10
    change = (change * 10) + tmp
    num = num // 10

print("Số sau khi đổi:", change)