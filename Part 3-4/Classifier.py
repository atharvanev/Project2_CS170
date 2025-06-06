import math
from fileRead import compressRange
from collections import Counter
class Classifier:

    def train(self, trainingSet, dataset):
        self.trainedData = []
        for id in trainingSet:
            self.trainedData.append(dataset[id])

    def test(self, testPoint, featureSet):
        if not featureSet: #handling 0 features
            count = Counter(point[0] for point in self.trainedData)
            mode = count.most_common(1)[0][0]
            return mode
        minDist = math.inf
        resClass = 0
        for point in self.trainedData:
            cur_dist = 0
            for feature in featureSet:
                cur_dist += pow(testPoint[feature] - point[feature],2)
            cur_dist = math.sqrt(cur_dist)

            if(cur_dist < minDist):
                minDist = cur_dist
                resClass =point[0]
        return resClass

        


    