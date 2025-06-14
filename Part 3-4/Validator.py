from Classifier import Classifier
class Validator:

    def __init__(self, featureSet, dataset, classifier,K):
        self.features = featureSet
        self.data = dataset
        self.classifier = classifier
        self.K = K

    def validate(self):
        trainingSet = set([i for i in range(0,len(self.data))])
        correct = 0
      
        for i in range(0,len(self.data)):
            
            trainingSet.remove(i)

            self.classifier.train(trainingSet, self.data)
           
          
           
            classFound = self.classifier.test(self.data[i], self.features,self.K)
           
        
            if(classFound == self.data[i][0]):
                correct+=1
            trainingSet.add(i)
        return (correct / len(self.data))