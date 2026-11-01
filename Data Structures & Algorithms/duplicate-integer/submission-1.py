class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mydict = {}
        for i in nums:
            if i in mydict:
                mydict[i] += 1
            else:
                mydict[i] = 1
        for count in mydict.values():
            if count > 1:
                return True
        return False