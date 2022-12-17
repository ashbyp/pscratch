def dupe(l: list[int]) -> list[int]:
  if not l:
    return []
  l.sort()
  m = l[0]
  output = [l[0]]
  for i in l[1:]:
    if i != m:
      m = i
      output.append(i)
  return l

print(dupe([1,2,3,3,4,4,4,5, 6]))




