import math

while True:
    try: 
        i = int(input("På en skala 1-10 hur lätt är Mac att använda?").strip())
        if i > 0 and i < 11:
            break
    except ValueError:
        pass
    print("skalan var 1-10")

if i > 5:
    print("Kul att höra")
else: 
    print("Tråkigt att höra")

