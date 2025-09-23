class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # iterate to get freqs
        # after that we need a sort, then grab top k
        # n log n

        # x --> freq
        # during iter we do x + 1 ...
        # when we do this, we want to double check that the freq is greater than or equal to our current set of top nums
        # [a, b + 1, c]

        # how to keep the top k sorted? do one pairwise comparison if something in the curr top k is selected
        # how to check if curr top k is selected

        # init sorted array of len k for top k
        # iterate over nums
        # update top k array if not filled
        # elif 

        # so maybe we can use a heap data stucture? max heap
        # iterate through, then add vals to a max heap / pq. pop top k for answer
        # total complexity then is O(n + klogn)

        # O(n + klogn) heap approach
        # freq = {}

        # for num in nums:
        #     freq[num] = freq.get(num, 0) - 1 # max heap
        
        # vals = [(value, key) for key, value in freq.items()]
        # heapq.heapify(vals)
        # ret = []

        # for i in range(k):
        #     ret.append(heapq.heappop(vals)[1])
        
        # return ret

        # O(n) bucket sort approach
        # still count using hash map
        # also init an array of len n+1 (we use idx 1 thru n+1)
        # here the index is the count, and the element is a list of elements from input
        # load array using hashmap
        # to get result, iterate from the end of the array until k elements are collected

        counts = {}
        freq = [[] for i in range(len(nums)+1)]

        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        # ex. 1 --> 3
        for key, value in counts.items():
            freq[value].append(key)
        # 0 1 2 3 4 5 6
        # . 3 2 1 . . .
        ret = []
        for i in range(len(freq) - 1, 0, -1):
            for y in freq[i]:
                ret.append(y)
                if len(ret) == k:
                    return ret