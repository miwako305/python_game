import random
import datetime
ALP=["A","B","C","D","E","F","G"]
r=random.choice(ALP)
alp=""
for i in ALP:
    if i!=r:
        alp=alp+i
print(alp)
st = datetime.datetime.now()
ans=input("nuketerueigo")
if ans==r:
    print("ok")
    now= datetime.datetime.now()
        print(str((now-st).seconds)） + "びょうかかりました")
else:
    print("ng")
