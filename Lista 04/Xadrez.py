L = int(input())
C = int(input())

if L % 2 == 0 and C % 2 != 0:
    print("0")
if L % 2 == 0 and C % 2 == 0:
    print("1")
if L % 2 != 0 and C % 2 == 0:
    print("0")
if L % 2 != 0 and C % 2 != 0:
    print("1")
