print('Solve Program')
shopping_cart_dict = {'milk': 20.0, 'bread': 10.0, 'eggs': 145.0}
total = 0
for key, value in shopping_cart_dict.items():
    shopping_cart_dict[key] = shopping_cart_dict[key] * 10/ 100
    shopping_cart_dict[key] = shopping_cart_dict[key] + value

    total = total + shopping_cart_dict[key]

print('sum after raise = ', total)
vat = total * 14 / 100
net_value= total + vat
print('net_value=', net_value)