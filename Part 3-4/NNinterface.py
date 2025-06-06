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
            
        

        maxF = len(dataset[0]) - 1
        print()
        print(f"This dataset has {maxF} features (not including the class attribute), with {len(dataset)} instances.") 
        featureCountString = ""
        print()


        featureSet = set(i for i in range(1,maxF+1))
        print("Please wait while I normalize the data...",end="")
        normalize(dataset, featureSet)
        print("Done")
       
        if option == "1":
            forward(featureSet,dataset,classifier)
        else:
            backward(featureSet,dataset,classifier)

        # print()
        # starttime = time.time()
        # endtime = time.time()
        # timeElapsed = endtime - starttime
        # validator = Validator(featureSet, dataset, classifier)
        # accuracy, trainingTime, testingTime = validator.validate()
        # print("Dataset Normalize Time: " + str(timeElapsed) + " seconds.")
        # print("Training Time: " + str(trainingTime) + " seconds.")
        # print("Testing Time: " + str(testingTime) + " seconds.")
        # print()

        # res = "Using features {"
        # res += ", ".join(str(fe) for fe in featureSet)

        # res+="}, we can validate test data with "
        # res+= str(accuracy)
        # res += " accuracy."
        
        # print(res)
        # print()

        quit = input("Press 'q' to quit or any other button to continue!\n")
        
  
NNinterface()