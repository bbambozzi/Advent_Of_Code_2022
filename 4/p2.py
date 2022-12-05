with open('input.txt', 'r') as f:
    count = 0 
    for line in f.readlines():
        l , r = line.strip().split(',')[0] , line.strip().split(',')[1]
        l1, l2 = int(l.split('-')[0]) , int(l.split('-')[1])
        r1, r2 = int(r.split('-')[0]) , int(r.split('-')[1])
        if (l1>=r1 and l2 <= r2) or (l1 <=r1 and l2>= r2) or (l1<= r1 and l2 >= r1) or (l1 <= r2 and l2 >= r2):
            count += 1
    ## [------------] 1
    ## ------[----------] 2
    ## ---------[------]--- 1
    ## -------------[------] 2
    print(count)
            
