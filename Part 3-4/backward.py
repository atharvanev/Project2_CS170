from evaluate import evaluate

def backward(featureset, dataset,classifier,K):
    n =len(featureset)
    i = [x for x in range(1,n+1)]
    intial = evaluate(i,dataset,classifier,K)
    scores = {frozenset(i):intial}

    cur = i.copy()
    unremoved = set(range(1,n+1))

   
    overallMax = cur.copy()
    overallScore = intial
    curScore = 0 #defined outside so i can refer to it i there is an overall decreased score at end for the warning

    print(f"Using All features and “leaving-one-out” evaluation, I get an accuracy of {overallScore}% Beginning search.")
   
    while unremoved:
        curScore = 0 #scores comparision only for iteration level not whole tree
        maxDigit = 0 #maxIndex only for iteration level 
        maxDigit = None

        for j in unremoved:
            next = cur.copy()
            next.remove(j)
            scores[frozenset(next)] = evaluate(next, dataset, classifier,K)

        for i in unremoved:
            cur.remove(i)
            display = sorted(cur)

            print(f"    Using feature(s) {display} accuracy is {scores[frozenset(cur)]}%")

            if scores[frozenset(cur)] > overallScore: #check the overall max
                overallMax = cur.copy()
                overallScore = scores[frozenset(cur)]
                curScore = scores[frozenset(cur)]
                maxDigit = i
            elif scores[frozenset(cur)] > curScore: #check for this iteration otherwise
                curScore = scores[frozenset(cur)]
                maxDigit = i
            
            cur.append(i)

        cur.remove(maxDigit)

        print('\n')
        print(f"Feature set {sorted(cur)} was best, accuracy is {scores[frozenset(cur)]}%")

        unremoved.remove(maxDigit)

       
        
    if overallScore > curScore:
            print("\n")
            print("(Warning: Decreased accuracy! )")
            print(f"Search finished! The best subset of features is {sorted(overallMax)}, which has an accuracy of {overallScore}%")
        
