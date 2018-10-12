def count_code(str):
  ans = 0
  for i in range(len(str)):
    if(len(str)-i>=4):
      if(str[i]=='c' and str[i+1]=='o' and str[i+3]=='e'):
        ans+=1
  return ans

