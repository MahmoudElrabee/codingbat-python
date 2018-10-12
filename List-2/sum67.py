def sum67(nums):
  six = False
  sum = 0
  for i in nums:
    if(six):
      if(i==7):
        six=False
    elif(i==6):
      six=True
    else:
      sum+=i
  return sum

