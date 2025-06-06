from Validator import Validator
def evaluate(featureSet, dataset,classifier):
        validator = Validator(featureSet, dataset, classifier)
        return validator.validate()