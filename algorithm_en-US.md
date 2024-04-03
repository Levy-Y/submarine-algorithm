# The algorithm works as follows:

1. It selects all pearls whose value reaches the moho_min value.
2. It adds the starting point (origo) to the path.
3. While there are valuable pearls, it selects the nearest pearl and adds it to the route, provided that the available distance is sufficient to reach the pearl and return to the starting point.
4. If the available distance is not sufficient to reach the next pearl and return to the starting point, the submarine returns to the starting point.

# Smart MOHO:
1. It uses MOHO as a base.
2. It changes the value of moho_min and selects the path that provides the highest pearl value, then displays it.
