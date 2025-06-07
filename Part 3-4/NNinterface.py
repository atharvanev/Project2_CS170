from Classifier import Classifier
from Validator import Validator
from fileRead import fileRead, compressRange, normalize
from forward import forward
from backward import backward
import time

def getfile():
    while True:
        try:
            file = input("Type in the name of the file to test: ")
            data = fileRead(f"ProjectFiles/{file}")
            return data
        except FileNotFoundError:
            print(f"Error: The file '{file}' was not found.")


def NNinterface():
    classifier = Classifier()
    quit = ""
    option = ""
    K = ""
    while(quit != "q"):
        print( "Welcome to Atharva Nevasekar(aneva018) and Rishi Dave (rdave009)\'s Feature Selection Algorithm")
        print()
        dataset = getfile()

        while True:
            print()
            print("Type the number of the algorithm you want to run")
            print("     1 Forward Selectionm\n     2 Backward Selection\n")
            option = input("Select your option: ")
            if option != "1" and option != "2":
                option = input("Please reselect a valid option: ")
            else:
                break
        while True:
            print()
            print()
            print("Please Select K for the KNN algorithim")
            print("     1 \n     3\n     5\n     7\n")
            K = int(input("Select your option: "))
            choices = [1,3,5,7]
            if K not in choices:
                K = input("Please reselect a valid option: ")
            else:
                break
        

        maxF = len(dataset[0]) - 1
        print()
        print(f"This dataset has {maxF} features (not including the class attribute), with {len(dataset)} instances.") 
        print()


        featureSet = set(i for i in range(1,maxF+1))
        print("Please wait while I normalize the data...",end="")
        normalize(dataset, featureSet)
        print("Done")
       
        if option == "1":
            forward(featureSet,dataset,classifier,K)
        else:
            backward(featureSet,dataset,classifier,K)

      

        quit = input("Press 'q' to quit or any other button to continue!\n")
        
  
NNinterface()