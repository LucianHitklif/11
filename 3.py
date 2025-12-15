for a in range(1, 151):
    for b in range(1, 151):
        for c in range(1, 151):
            for d in range(1, 151):
                    examp = a**5 + b**5 + c**5 + d**5
                    e = int(examp**(1/5))
                    if e**5 == examp and e<151:
                        print(f"Найдены: а = {a}, b = {b}, c = {c}, d = {d}, e = {e}")
                        print(f"Их сумма: {a+b+c+d+e}")
                        exit()
