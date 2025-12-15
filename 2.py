print("У вас есть 100 руб. Сколько вы можете купить быков/коров/телят.")

cattle = []

for bull in range(11):
    for cow in range(21):
        calf = (100 - bull * 10 - cow * 5) * 2
        if calf >= 0 and calf%1==0:
            cattle.append((bull, cow, int(calf)))

print(f"Сколько вариантов покупки: {len(cattle)}")
print(f"Варианты покупки: {cattle}")
