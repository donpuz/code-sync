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

        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) - 1 # max heap
        
        vals = [(value, key) for key, value in freq.items()]
        heapq.heapify(vals)
        ret = []

        for i in range(k):
            ret.append(heapq.heappop(vals)[1])
        
        return ret