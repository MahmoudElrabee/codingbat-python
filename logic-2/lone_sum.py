def lone_sum(a, b, c):
  ls = [a,b,c]
  ans = a+b+c
  if(ls.count(a)>1):ans-=a
  if(ls.count(b)>1):ans-=b
  if(ls.count(c)>1):ans-=c
  return ans
