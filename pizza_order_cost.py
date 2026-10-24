small_pizza_cost = 8.00
large_pizza_cost = 12.00
topping_cost = 1.00
delivery_base_fee = 2.00
delivery_per_mile_fee = 1.00

pizza_size = input("Enter pizza size (small/large): ").strip().lower()
number_of_toppings = int(input("Enter number of toppings: "))
delivery_distance = float(input("Enter delivery distance in miles: "))




if pizza_size == "small":
    pizza_cost = small_pizza_cost
elif pizza_size == "large":
    pizza_cost = large_pizza_cost
else:
    print("Invalid pizza size entered. Please enter 'small' or 'large'.")
    exit()


toppings_total_cost = number_of_toppings * topping_cost
if delivery_distance == 0:
    delivery_fee = 0
else:
    delivery_fee = delivery_base_fee + (delivery_per_mile_fee * delivery_distance)

total_cost = pizza_cost + toppings_total_cost + delivery_fee

print(f"Total cost of the pizza order: ${total_cost:.2f}")
