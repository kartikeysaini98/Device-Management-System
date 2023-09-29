# AML2203: ASSIGNMENT 1 S2022

# Group Member:
# Kartikey Saini (c0838996)
# Simranpreet Kaur (c0849778)


# Part-2

def continue_new():
    print()
    usr_in = input("Do you want to continue??(y/n)")
    if usr_in == 'y':
        main()
    elif usr_in == 'n':
        last_option()
    else:
        print("This is an invalid selection, try again.")
        continue_new()

def last_option():
    print("Thanks for using the application !")



def view_data():
    with open('devices.txt') as file:
        lines = file.readlines()

    for i, j in enumerate(lines,start=1):
        print("Device",i,j)

def add_device():
    usr_input = input("Add the device: ")
    print(f"{usr_input} is added.")
    file.write(usr_input+"\n")


def remove():
    print("Delete Device")
    with open('devices.txt') as file:
        lines = file.readlines()
    try:
        n = int(input("Enter device no. :(example: 1,2,3 and so on.)"))
        lines.pop(n - 1)  # This removes the nth device from the list.

        with open("devices.txt", "w") as file_object:
            for line in lines:
                file_object.write(line)
    except IndexError:
        print("Enter correct input")


def update():
    print("Update Device")
    with open('devices.txt') as file:
        lines = file.readlines()

    try:
        n = int(input("Enter the device no. example(1,2,3 and so on) to be updated : "))
        device = input("Enter new device name :")
        device += '\n'
        lines[n - 1] = device  # removes the nth device from the list

        with open("devices.txt", "w") as file_object:
            # Append 'hello' at the end of file
            for line in lines:
                file_object.write(line)

    except IndexError:
        print("Enter correct Input.")
        continue_new()

def exit_function():
    print("Thanks for using the application !")

def main():
    global file
    file = open("devices.txt", "r+")

    print("Welcome to the Device Management System")
    print("\n1.)view all devices\n2.)add a device\n3.)delete a device\n4.)update a device\n5.)exit the program")
    print()


    try:
        usr_input = int(input("Select one option from the list ( 1, 2, 3, 4, or 5):"))

        if usr_input == 1:
            print()
            view_data()
            continue_new()

        elif usr_input == 2:
            file = open("devices.txt", "a")
            print()
            add_device()
            continue_new()

        elif usr_input == 3:
            remove()
            continue_new()

        elif usr_input == 4:
            update()
            continue_new()

        elif usr_input ==5:
            exit_function()

        else:
            print("This is an invalid selection, try again.")
            continue_new()
    except ValueError:
        print("Please, enter Correct input")
        continue_new()

if __name__ == "__main__":
    main()