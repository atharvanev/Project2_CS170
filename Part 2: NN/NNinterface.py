from Classifier import Classifier
from Validator import Validator
from fileRead import fileRead
def NNinterface():
    classifier = Classifier()
    quit = ""
    while(quit != "q"):
        print( "Welcome to Atharva Nevasekar(aneva018) and Rishi Dave (rdave009)\'s Nearest Neighbor Algorithm.")
        print()
        
        file = ""
        file = input("Please enter 'sm' to use the small dataset or 'lg' to use the large dataset. You will be reprompted if you do not input a proper value.\n")
        while(file != "sm" and file != "lg"):
            file = input("Please enter 'sm' to use the small dataset or 'lg' to use the large dataset.\n")
        maxF = 0
        if(file == "sm"):
            maxF = 10
            dataset = fileRead("ProjectFiles/small-test-dataset.txt")
        elif(file == "lg"):
            maxF = 40
            dataset = fileRead("ProjectFiles/large-test-dataset.txt")
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

        validator = Validator(featureSet, dataset, classifier)
        accuracy = validator.validate()
        res = "Using features {"
        res += ", ".join(str(fe) for fe in featureSet)

        res+="}, we can validate test data with "
        res+= str(accuracy)
        res += " accuracy."

        print(res)
        print()

        quit = input("Press 'q' to quit or any other button to continue!\n")
        

NNinterface()