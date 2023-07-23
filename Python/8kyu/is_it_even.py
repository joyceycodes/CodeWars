def topKFrequent(nums,k):
    count = {}
    bucket = [[] for i in range(len(nums)+1)]
    
    for i in nums:
        # adds 1 to the value at count[n], also sets count[n] to 0 if count[n] does not exist yet
        count[i] = 1 + count.get(i,0)

    for k,v in count.items():
        bucket[v].append(k)

    result = []
    for i in range(len(bucket)-1, 0, -1):
        for n in bucket[i]:
            result.append(n)
            if len(result) == k:
                return result
            
print(topKFrequent([1,1,1,2,2,3],2))
