  # TODO: optimize task_1
  # task_1
  rect = [[1,2],
          [2,3],
          [3,4],
          [4,5]]
  new_rect = []
  for point in rect:
      point[0] = point[0] + x
      point[1] = point[1] + y
      new_rect.append([point[0], point[1]])

# Destination
