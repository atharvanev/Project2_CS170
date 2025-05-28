from Classifier import Classifier
import time
class Validator:

    def __init__(self, featureSet, dataset, classifier):
        self.features = featureSet
        self.data = dataset
        self.classifier = classifier

    def validate(self):
        trainingSet = set([i for i in range(0,len(self.data))])
        correct = 0
        trainingTime = 0
        testingTime = 0
        for i in range(0,len(self.data)):
            
            trainingSet.remove(i)
            starttime = time.time()
            self.classifier.train(trainingSet, self.data)
            endtime = time.time()
            trainingTime+= (endtime-starttime)
            starttime = time.time()
            classFound = self.classifier.test(self.data[i], self.features)
            endtime = time.time()
            testingTime+= (endtime-starttime)
            if(classFound == self.data[i][0]):
                correct+=1
            trainingSet.add(i)
        return (correct / len(self.data)), trainingTime, testingTime