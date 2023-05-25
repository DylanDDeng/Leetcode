class Solution: 
    def twoSum(self, nums: list[int], target:int) -> list[int]:  

        records = dict() 

        for idx, val in enumerate(nums): 
            if target - val not in records: 
                records[val] = idx 
            else: 
                return [records[target-val], idx] 