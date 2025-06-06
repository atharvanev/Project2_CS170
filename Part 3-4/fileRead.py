import math
import statistics

def fileRead(file_path):
    # try:
        with open(file_path, 'r') as file:
            dataset = []
            for line in file:
                nums = line.split()
                dataset.append([])
                for num in nums:
                    dataset[-1].append(float(num))
            return dataset

    # except FileNotFoundError:
    #     print(f"Error: The file '{file_path}' was not found.")
    # except Exception as e:
    #     print(f"An unexpected error occurred: {e}")
    

def normalize(dataset, featureSet):
    for feature in featureSet:
        data = []
        for point in dataset:
            data.append(point[feature])
        std = statistics.stdev(data)
        mean = statistics.mean(data)
        for point in dataset:
            point[feature] = (point[feature] - mean) / std

def compressRange(dataset, featureset):
    for feature in featureset:
        minVal = math.inf
        maxVal = -math.inf
        for point in dataset:
            if point[feature] < minVal:
               minVal = point[feature]
            if point[feature] > maxVal:
               maxVal = point[feature]
        for point in dataset:
            point[feature] = (point[feature] - minVal) / (maxVal - minVal)
