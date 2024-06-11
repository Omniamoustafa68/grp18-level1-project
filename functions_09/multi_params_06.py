#tuples
def add_numbers(*numbers_tuples):

    total =0
    for item in numbers_tuples:
        total=total+item
    return total

#print(add_numbers( 10, 20, 30, 40, 50))
v_result= add_numbers(10, 20, 30, 40, 50)
print(v_result)

#dictionary
def shopping_cart(**shopping_kwargs):
    for key, value in shopping_kwargs.items():
        print(key, value)

shopping_cart(tea= 20, bread= 30, sugar=40)