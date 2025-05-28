from evaluate import evaluate

def forward(n):
    scores = {frozenset([i]):evaluate(i) for i in range(1,n+1)}
    #print(scores)
    cur = []
    unused = set(range(1,n+1))

    overallMax = []
    overallScore = evaluate()
    curScore = 0 #defined outside so i can refer to it i there is an overall decreased score at end for the warning

    print(f"Using no features and “random” evaluation, I get an accuracy of {overallScore}% Beginning search.")
   
    while unused:
        curScore = 0 #scores comparision only for iteration level not whole tree
        maxDigit = 0 #maxIndex only for iteration level 
        maxDigit = None

        for i in unused:
            cur.append(i)

            print(f"    Using feature(s) {sorted(cur)} accuracy is {scores[frozenset(cur)]}%")

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
        print(f"Feature set {sorted(cur)} was best, accuracy is {scores[frozenset(cur)]}%")

        unused.remove(maxDigit)

        for j in unused:
            next = cur.copy()
            next.append(j)
            scores[frozenset(next)] = evaluate(next)
        
    if overallScore > curScore:
            print("\n")
            print("(Warning: Decreased accuracy! )")
            print(f"Search finished! The best subset of features is {sorted(overallMax)}, which has an accuracy of {overallScore}%")
        
