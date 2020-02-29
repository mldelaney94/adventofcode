TOTAL_TIME_FLYING = 2503
MAX_DIST = 0

with open('inputQ14.txt', 'r') as f:
    for line in f:
        liness = line.split()
        name = liness[0]
        speed_while_flying = liness[3]
        time_can_fly = liness[6]
        rest_time = liness[13]

        fly = TOTAL_TIME_FLYING
        total_dist = 0
        while fly > int(time_can_fly):
            total_dist += int(time_can_fly) * int(speed_while_flying)
            fly -= int(time_can_fly)
            fly -= int(rest_time)

        if fly > 0:
            total_dist += fly * int(speed_while_flying)
    
        if total_dist > MAX_DIST:
            MAX_DIST = total_dist

print(MAX_DIST)
