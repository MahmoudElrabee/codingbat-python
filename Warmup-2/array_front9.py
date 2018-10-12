def array_front9(nums):
  if(len(nums) <= 4):return nums.count(9)>0
  else: return nums[:4].count(9)>0

