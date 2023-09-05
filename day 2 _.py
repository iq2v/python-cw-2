my_name=input("what is your name?")
my_age=input("how old are you ?")
print(f"my name is {my_name} and im {my_age} years old")
first_number=int(input("first_number"))
secound_number=int(input("secound_number"))
operation=input("what is the operation(+-*/)")
if operation == '+' :

    print(first_number + secound_number)

elif operation== "-" :
    print(first_number - secound_number)

elif operation == '*' :
    print(first_number * secound_number)

elif operation == "/" :
    print(first_number / secound_number)

else : 
    print('error')

#part 3 
bus_capacity = 20
people_on_the_bus = int(input('How many people are on the bus ?'))
want_to_ride = int(input("How many people want to take the bus ?"))
empty_seats = bus_capacity - people_on_the_bus
if empty_seats >= people_on_the_bus : 
    print(f'there are {empty_seats} empty seats') 
else :
    print('The bus is full')


