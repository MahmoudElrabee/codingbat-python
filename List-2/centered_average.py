def centered_average(nums):
  mn,mx=1e9,-1e9
  for i in nums:
    mn=min(i,mn)
    mx=max(mx,i)
    sum =0
  if(mn!=mx):
    if(nums.count(mn)>1):
      sum+=mn*(nums.count(mn)-1)
    if(nums.count(mx)>1):
      sum+=mx*(nums.count(mx)-1)
  else:
    sum+=mn*(len(nums)-2)
  for i in nums:
    if(i!=mn and i!=mx):
      sum+=i
  l = len(nums)
  if(nums.count(mn)>=1):l-=1
  if(nums.count(mx)>=1):l-=1
  return sum//l

