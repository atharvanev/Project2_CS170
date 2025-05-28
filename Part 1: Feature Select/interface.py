from forward import forward
from backward import backward
def Interface():
    print( "Welcome to Atharva Nevasekar(aneva018) and Rishi Dave (rdave009)\'s Feature Selection Algorithm.")
    print()
    n = 0
    while True:
        try:
            n = int(input("Please enter toal number of features: "))
            while n < 1:
                print("You need at least 1 feature")
                n = int(input("Please enter toal number of features:"))

            break
        except ValueError:
             print("Invalid input. Please enter a valid integer.")

   

   

    while True:
        print()
        print("Type the number of the algorithm you want to run")
        print("     1 Forward Selectionm\n     2 Backward Selection\n     3 exit\n")
        option = input("Select your option: ")
        while option != "1" and option != "2" and option !="3":
            option = input("Please reselect a valid option: ")
        if option == "1":
            forward(n)
        elif option == "2":
            backward(n)
        else:
            break


Interface()