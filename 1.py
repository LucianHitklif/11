solution = []
for n in range(1, 13):
    for k in range(1, 13):
        m = 12 - n - k
        if m >= 1:
            if 28*n+30*k+31*m==365:
                solution.append((n, k, m))
                break
for solutions in solution:
    print(f"n = {solutions[0]}, k = {solutions[1]}, m = {solutions[2]}")
