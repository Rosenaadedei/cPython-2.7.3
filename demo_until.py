import dis

def myfoo(num):
    until num == 0:
        print(num)
        num -= 1

dis.dis(myfoo)
myfoo(3)
