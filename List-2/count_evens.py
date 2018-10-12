def count_evens(nums):
  ls = [x&1 for x in nums]
  return ls.count(0)

