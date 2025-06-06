from evaluate import evaluate
def forward(featureset, dataset,classifier):
    n = len(featureset)
    intial = evaluate([],dataset,classifier)
    scores = {frozenset([]):intial}
    #print(scores)
    cur = []
    unused = set(range(1,n+1))

    overallMax = []
    overallScore =  intial
    curScore = 0 #defined outside so i can refer to it i there is an overall decreased score at end for the warning

    print(f"Running nearest neighbor with no features (default rate), using “leaving-one-out” evaluation, I  get an accuracy of {overallScore}% Beginning search.")
   
    while unused:
        curScore = 0 #scores comparision only for iteration level not whole tree 
        maxDigit = None

        for j in unused:
            next = cur.copy()
            next.append(j)
            scores[frozenset(next)] = evaluate(next,dataset,classifier)

        for i in unused:
            cur.append(i)
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
            
            cur.pop()

        cur.append(maxDigit)

        print('\n')
        print(f"Feature set {display} was best, accuracy is {scores[frozenset(cur)]}%")

        unused.remove(maxDigit)

        
        
    if overallScore > curScore:
            print("\n")
            print("(Warning: Decreased accuracy! )")
            print(f"Search finished! The best subset of features is {sorted(overallMax)}, which has an accuracy of {overallScore}%")
        
