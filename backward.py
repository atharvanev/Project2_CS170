from evaluate import evaluate

def backward(n):
    i = [x for x in range(1,n+1)]
    scores = {frozenset(i):evaluate(i)}

    cur = i.copy()
    unremoved = set(range(1,n+1))

    for j in unremoved:
            next = cur.copy()
            next.remove(j)
            scores[frozenset(next)] = evaluate(next)

    overallMax = 0
    overallScore = 0 
    curScore = 0 #defined outside so i can refer to it i there is an overall decreased score at end for the warning

    print(f"Using All features and “random” evaluation, I get an accuracy of {evaluate(i)}% Beginning search.")
   
    while unremoved:
        curScore = 0 #scores comparision only for iteration level not whole tree
        maxDigit = 0 #maxIndex only for iteration level 
        maxDigit = None

        for i in unremoved:
            cur.remove(i)

            print(f"    Using feature(s) {sorted(cur)} accuracy is {scores[frozenset(cur)]}%")

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

        for j in unremoved:
            next = cur.copy()
            next.remove(j)
            scores[frozenset(next)] = evaluate(next)
        
    if overallScore > curScore:
            print("\n")
            print("(Warning: Decreased accuracy! )")
            print(f"Search finished! The best subset of features is {sorted(overallMax)}, which has an accuracy of {overallScore}%")
        
