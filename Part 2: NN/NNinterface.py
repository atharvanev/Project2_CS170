from Classifier import Classifier
from Validator import Validator
from fileRead import fileRead, compressRange, normalize
import time
def NNinterface():
    classifier = Classifier()
    quit = ""
    SMdataset = fileRead("ProjectFiles/small-test-dataset.txt")
    LGdataset = fileRead("ProjectFiles/large-test-dataset.txt")
    while(quit != "q"):
        print( "Welcome to Atharva Nevasekar(aneva018) and Rishi Dave (rdave009)\'s Nearest Neighbor Algorithm.")
        print()
        
        file = ""
        file = input("Please enter 'sm' to use the small dataset or 'lg' to use the large dataset. You will be reprompted if you do not input a proper value.\n")
        while(file != "sm" and file != "lg"):
            file = input("Please enter 'sm' to use the small dataset or 'lg' to use the large dataset.\n")
        if(file == "sm"):
            dataset = SMdataset
        elif(file == "lg"):
            dataset = LGdataset
        maxF = len(dataset[0]) - 1
        featureCountString = ""
        print()
        while True:
            featureCountString = input("Enter how many features you want to use to classify the dataset between 1 to " + str(maxF) +": ")
            try:
                featureCount = int(featureCountString)
                if(featureCount >0 and featureCount < maxF):
                    break
                else:
                    print("Invalid input. Please enter a number in range.")
                
            except ValueError:
                print("Invalid input. Please enter a whole number.")

        featureSet = set()

        while(len(featureSet) < featureCount):
            featureString = input("Which feature do you want to use to classify the dataset(1 to " + str(maxF) +"): ")
            try:
                feature = int(featureString)
                if(feature >0 and feature < maxF and feature not in featureSet):
                    featureSet.add(feature)
                    continue
                elif(feature in featureSet):
                    print("Invalid input. Feature already selected.")
                else:
                    print("Invalid input. Please enter a number in range.")
                
            except ValueError:
                print("Invalid input. Please enter a whole number.")
        print()
        starttime = time.time()
        normalize(dataset, featureSet)
        endtime = time.time()
        timeElapsed = endtime - starttime
        validator = Validator(featureSet, dataset, classifier)
        accuracy, trainingTime, testingTime = validator.validate()
        print("Dataset Normalize Time: " + str(timeElapsed) + " seconds.")
        print("Training Time: " + str(trainingTime) + " seconds.")
        print("Testing Time: " + str(testingTime) + " seconds.")
        print()

        res = "Using features {"
        res += ", ".join(str(fe) for fe in featureSet)

        res+="}, we can validate test data with "
        res+= str(accuracy)
        res += " accuracy."
        
        print(res)
        print()

        quit = input("Press 'q' to quit or any other button to continue!\n")
        

NNinterface()