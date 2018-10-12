def last2(str):
  if(len(str)<=2): return 0
  ans = 0
  for i in range(len(str)):
    if(len(str)-i > 2):
      if(str[i] == str[-2:-1] and str[i+1]==str[-1:]):
        ans+=1;
  return ans

