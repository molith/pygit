fruits = ['banana', 'apple', 'grape']
print(fruits)

add_fruits = input("add something: \n")
fruits.append(add_fruits)  # add input data to fruits
print(fruits)

def remove(): # use function for avoiding invalid input
    remove_fruits = input("remove something: \n")
    if remove_fruits in fruits: # make output True or False
        fruits.remove(remove_fruits)
    else:
        print("fruit not found")
        print(fruits)
        retry = input("try again? [y/n]\n")
        if retry == "y":
            print(fruits)
            remove()  # restart function
        else:
            pass  # do nothing

remove()
print(fruits)
