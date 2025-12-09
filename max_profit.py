def max_profit_all(n):
    buildings = {"T": (5,1500), "P": (4,1000), "C": (10,2000)}
    best_profit = 0
    best_list = []

    for T in range(n // 5 + 1):
        for P in range(n // 4 + 1):
            for C in range(n // 10 + 1):
                total_time = T*5 + P*4 + C*10
                if total_time > n:
                    continue

                profit = 0
                current_time = 0
                for _ in range(T):
                    current_time += 5
                    profit += (n - current_time) * 1500
                for _ in range(P):
                    current_time += 4
                    profit += (n - current_time) * 1000
                for _ in range(C):
                    current_time += 10
                    profit += (n - current_time) * 2000

                if profit > best_profit:
                    best_profit = profit
                    best_list = [(T, P, C)]
                elif profit == best_profit:
                    best_list.append((T, P, C))

    return best_profit, best_list

if __name__ == "__main__":
    for n in [7, 8, 13]:
        profit, combos = max_profit_all(n)
        print("Time =", n, "Earnings: $", profit)
        print("Optimal combinations:", combos)
        print()
