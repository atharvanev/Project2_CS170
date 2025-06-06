import math
from fileRead import compressRange
from collections import Counter
from queue import PriorityQueue
class Classifier:

    def train(self, trainingSet, dataset):
        self.trainedData = []
        for id in trainingSet:
            self.trainedData.append(dataset[id])

    def test(self, testPoint, featureSet,K):
        if not featureSet: #handling 0 features
            count = Counter(point[0] for point in self.trainedData)
            mode = count.most_common(1)[0][0]
            return mode
        
        q = PriorityQueue()
        #minDist = math.inf
        resClass = 0
        for point in self.trainedData:
            cur_dist = 0
            for feature in featureSet:
                cur_dist += pow(testPoint[feature] - point[feature],2)
            cur_dist = math.sqrt(cur_dist)

            # if(cur_dist < minDist):
            #     minDist = cur_dist
            #     resClass =point[0]

            q.put((cur_dist,point[0]))
        
        minK = []
        for i in range(K):
            minK.append(q.get())
        count = Counter(x[1] for x in minK)
        resClass = count.most_common(1)[0][0]

        return resClass

        


    