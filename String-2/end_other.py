def end_other(a, b):
  a,b=a.lower(),b.lower()
  if(len(a) >= len(b)):return a[len(a)-len(b):].count(b)>=1
  else:return b[len(b)-len(a):].count(a)>=1
