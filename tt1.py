def cre_user(user,age):
    return f"Hello {user},Your {age+5} old 5 Years."
user = input()
age = int(input())
print(cre_user(user,age))