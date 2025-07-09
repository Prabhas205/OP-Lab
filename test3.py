def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return 0
c,d = map(int,input().split())
print(divide(c,d))