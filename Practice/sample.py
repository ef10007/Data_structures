import numpy as np
import pandas as pd

origin_x, origin_y = 75, 75
x_s = np.arange(-origin_x, origin_y+1, 1)
y_s = np.arange(-origin_x, origin_y+1, 1)

## Loop through each point and check if safe
coords = []
for y in y_s:
    x_coords = []
    for x in x_s:
        coords_digits_sum = sum([int(i) for i in str(abs(x))]) + sum([int(i) for i in str(abs(y))])
        if coords_digits_sum <= 23:
            safe = True
        else:
            safe = False
        x_coords.append(safe)
    coords.append(x_coords)

## Initialize the origin as `really_safe` point
coords[origin_y][origin_x] = 'really_safe' # Origin

## Iteratively check if a safe point is beside a `really_safe` point
changing = True
while changing == True:
    changing = False
    for y,x_coords in enumerate(coords[1:-1], start=1):
        print()
        for x,is_safe in enumerate(x_coords[1:-1], start=1): # Check each point defined as (x+1, y+1) due to the padding
            if is_safe == 'really_safe':
                continue
            elif is_safe and any([coords[y-1][x] == 'really_safe', coords[y+1][x] == 'really_safe', coords[y][x-1] == 'really_safe', coords[y][x+1] == 'really_safe']):
                coords[y][x] = 'really_safe'
                changing = True
exit()

## Count the number of "really safe" points only
really_safe_points = [[1 if safety == 'really_safe' else 0 for safety in x_coords[1:-1]] for x_coords in coords[1:-1]]
print(sum([sum(i) for i in really_safe_points]))