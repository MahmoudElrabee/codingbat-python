def make_chocolate(small, big, goal):
  if(goal==0): return 0
  if(int(goal/5) <= big): goal-=int(goal/5)*5
  else: goal-=5*big
  if(small<goal): return -1
  return goal
