class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}
        for i in nums:
            if i not in my_dict:
                my_dict[i] = 1
            else:
                my_dict[i] += 1
        sorted_items = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)
        res = [item[0] for item in sorted_items[:k]]
        return res