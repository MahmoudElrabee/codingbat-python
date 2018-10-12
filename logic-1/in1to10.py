def in1to10(n, outside_mode):
  if(outside_mode):
    if(n > 1 and n < 10):return False
    return True
  if(n>=1 and n <=10):return True
  return False

