def make_bricks(small, big, goal):
  if(int(goal/5) >= big):goal-=5*big
  else:goal-=5*int(goal/5)
  return small>=goal
  
    

