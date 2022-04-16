N = int(input())

def star_pick(LEN):
  if LEN == 1:
    return['*']
  
  Stars = star_pick(LEN//3)
  L = []


  for S in Stars:
    L.append(S*3)
  for S in Stars:
    L.append(S+' '*(LEN//3)+S)
  for S in Stars:
    L.append(S*3)
  return L

print('\n'.join(star_pick(N)))
