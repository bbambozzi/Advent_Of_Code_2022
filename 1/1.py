with open('input.txt', 'r') as f:
    nums = []   
    cur = []
    for line in f.readlines():
        if line == '\n':
            nums.append(cur)
            cur = []
            continue
        cur.append(int(line.strip()))
    sums = []
    for calories in nums:
        l_sum = sum(calories)
        sums.append(l_sum)
    sums.sort() ## n log n
    print(sums[-3:])
    ans = sums[-3:len(sums)]
    print(sum(ans))



