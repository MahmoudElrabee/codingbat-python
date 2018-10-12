def max_end3(nums):
  lst = []  
  if(nums[0]>=nums[len(nums)-1]):
    for i in range(len(nums)):
      lst.append(nums[0])
  else:
    for i in range(len(nums)):
      lst.append(nums[len(nums)-1])
  return lst
