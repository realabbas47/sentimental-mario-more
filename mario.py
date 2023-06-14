hight = -1
while hight <= 0 or hight > 8:
    try:
        hight = int(input("Hight: "))
    except ValueError:
        hight = 0

for n in range(hight):
    temp1 = (' ' * (hight - (n + 1))) + ('#' * (n + 1))
    temp2 = ('#' * (n + 1))
    print(f"{temp1}  {temp2}")
