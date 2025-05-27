from evaluate import evaluate

def initialize(start,cur,n,scoredict): #populates the dictionary with all combinations and scores
        for i in range(start,n+1):
            cur.append(i)
            scoredict[frozenset(cur)] = evaluate(cur)
            initialize(i+1,cur,n,scoredict)
            cur.pop()
        return scoredict

def forward(n):
    scores = initialize(1,[],n,{})
    
    cur = []
    unused = set(range(1,n+1))

    overallMax = 0
    overallScore = 0 
    curScore = 0 #defined outside so i can refer to it i there is an overall decreased score at end for the warning

    print(f"Using no features and “random” evaluation, I get an accuracy of {evaluate()}% Beginning search.")
   
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
        #print('\n')
        unused.remove(maxDigit)
        
    if overallScore > curScore:
            print("\n")
            print("(Warning: Decreased accuracy! )")
            print(f"Search finished! The best subset of features is {sorted(overallMax)}, which has an accuracy of {overallScore}%")
        
forward(4)
