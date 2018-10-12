def close_far(a, b, c):
  if((abs(b-a)<2 and abs(a-c)>1 and abs(b-c)>1) or (abs(a-c)<2 and abs(b-a)>1 and abs(b-c)>1)):return True
  return False

