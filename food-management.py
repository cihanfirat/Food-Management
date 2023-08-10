#simple food management program
def add_food(pantry):
    name=input("Enter the food name: ")
    calories=int(input("Enter the calories of the food : "))
    pantry[name] = calories

def remove_food(pantry):
    name=input("Enter the food you want to delete: ")
    if name in pantry:
        del pantry[name]
    else:
        print("No such a food!")


def show_food(pantry):

    for i in pantry:
        print(i, " -> " , pantry[i])


def main():
    pantry_items = {}
    command = ''
    while command != 'done':
        command = input('Type add, remove, show, or done: ')
        if command == 'add':
            add_food(pantry_items)
        elif command == 'remove':
            remove_food(pantry_items)
        elif command == 'show':
            if len(pantry_items)==0:
                print("It looks empty.")
            show_food(pantry_items)
main()