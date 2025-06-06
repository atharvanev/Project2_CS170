from Validator import Validator
def evaluate(featureSet, dataset,classifier,K):
        validator = Validator(featureSet, dataset, classifier,K)
        return validator.validate()