def greedy_algorithm(menu, budget):
    sorted_menu = sorted(
        menu.items(), key=lambda m: m[1]['calories'] / m[1]['cost'], reverse=True)
    # print(sorted_menu)
    selected_manu_items = []
    total_cost = 0
    total_calories = 0
    for menu_item, item_deteils in sorted_menu:
        if total_cost + item_deteils['cost'] <= budget:
            selected_manu_items.append(menu_item)
            total_cost += item_deteils['cost']
            total_calories += item_deteils['calories']
    return (selected_manu_items, total_cost, total_calories)


def dynamic_programming(menu, budget):
    item_table = [[0] * (budget + 1) for _ in range(len(menu) + 1)]
    # print(dp)
    selected_manu_items = []
    for i, (m, item_details) in enumerate(menu.items(), start=1):
        for j in range(budget + 1):
            if item_details['cost'] <= j:
                item_table[i][j] = max(item_table[i - 1][j],
                                       item_table[i - 1][j - item_details['cost']] + item_details['calories'])
            else:
                item_table[i][j] = item_table[i - 1][j]
    # print(item_table)
    j = budget
    for i in range(len(menu), 0, -1):
        if item_table[i][j] != item_table[i-1][j]:
            selected_manu_items.append(list(menu.keys())[i - 1])
            j -= menu[list(menu.keys())[i - 1]]['cost']

    return (selected_manu_items,
            sum(menu[m]['cost'] for m in selected_manu_items),
            item_table[len(menu)][budget])


if __name__ == "__main__":
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }
    print("Specify budget:")
    budget = int(input())
    # budget = 100
    result = greedy_algorithm(items, budget)
    print(" Greedy Algorithm ")
    print(result, "\n")
    result = dynamic_programming(items, budget)
    print("Dynamic Programming")
    print(result, "\n")
