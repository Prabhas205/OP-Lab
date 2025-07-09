def cala_sun_av(li):
    li.reverse()
    print(li)
    su = sum(li)
    av = su/len(li)
    return f"{su} , {av}"
li = list(map(int,input().split()))
print(cala_sun_av(li))