import random
pl_pos=6
com_pos=3
def banmen():
    print("・" * (pl_pos-1) + "たか" + "・"*(30 - pl_pos))
    print("."*(com_pos-1) + "美和子" +"."*(30 - com_pos))
while True:
    input("enterたか")
    pl_pos= pl_pos+random.randint(1,6)
    if pl_pos > 30:
        pl_pos=30
    banmen()
    if pl_pos==30:
        print("あなたの勝ちです")
        break
    com_pos=com_pos +1
    if com_pos >30:
        com_pos=30
    banmen()
    if com_pos==30:
        print("あなたの負け")
        break
