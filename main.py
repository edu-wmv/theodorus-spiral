import math
vertices = [[1, 0] for j in range(10)]

for i in range(1, 10):
  vY = vertices[i-1][1] + (vertices[i-1][0] / math.sqrt(i+1))
  vX = vertices[i-1][0] - (vY / math.sqrt(i+1))

  vertices[i][0] = vX
  vertices[i][1] = vY

print(*vertices)