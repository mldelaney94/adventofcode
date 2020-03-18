"""Finds the maximum number possible when all neighbouring numbers are not able
to be added to the sum, first and last elements are considered neighbours"""

def badneighbours (sequence):
    





assert badneighbours([10, 3, 2, 5, 7, 8]) == 19
assert badneighbours([11, 15]) == 19
assert badneighbours([7, 7, 7, 7, 7, 7, 7]) == 21
assert badneighbours([1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 16
assert badneighbours([94, 40, 49, 65, 21, 21, 106, 80, 92, 81, 679, 4, 61,  
  6, 237, 12, 72, 74, 29, 95, 265, 35, 47, 1, 61, 397,
  52, 72, 37, 51, 1, 81, 45, 435, 7, 36, 57, 86, 81, 72]) == 2926

