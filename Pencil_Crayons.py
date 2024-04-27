a,b = map(int,input().split())
diff=0
for i in range(a):
  lst=input().split()
  lst=list(dict.fromkeys(lst))
  diff+=b-len(lst)
print(diff)