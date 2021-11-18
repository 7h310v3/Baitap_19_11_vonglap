def fibonaci(num):
    if(num == 1):
        return 0
    if(num == 2):
        return 1
    return fibonaci(num - 1) + fibonaci(num - 2)

lim = int(input("Nhập số số fibonaci cần in ra: "))

count = 1
print("fibonaci: ", end = "")
while(count <= lim):
    print(fibonaci(count), end = " ")
    count += 1