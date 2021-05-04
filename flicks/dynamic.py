start_strat = input('Which strategy would you like to start with [regular, reverse]: ')
change_points = input('When should the bot change stratgies: ').split()
for i in range(0, len(change_points)):
    change_points[i] = int(change_points[i])

print(change_points[-1])
