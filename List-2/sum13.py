def sum13(nums):
  sum = 0
  for i in range(len(nums)):
    if(nums[i]!=13):
      if(i!=0):
        if(nums[i-1]!=13):
          sum+=nums[i]
      else:
        sum+=nums[i]
  return sum
