TOTAL_TIME_FLYING = 2503

reindeer_stats = {}
with open('inputQ14.txt', 'r') as f:
    for line in f:
        liness = line.split()
        name = liness[0]
        speed_while_flying = int(liness[3])
        time_can_fly = int(liness[6])
        rest_time = int(liness[13])
        stats = []
        stats.append(speed_while_flying)
        stats.append(time_can_fly)
        stats.append(rest_time)
        reindeer_stats[name] = stats

distance_reindeer = {}

for reindeer in reindeer_stats:
    dist_at_every_second = []

    stats_list = reindeer_stats[reindeer]
    speed_while_flying = stats_list[0]
    time_can_fly = stats_list[1]
    rest_time = stats_list[2]
    time_flown = TOTAL_TIME_FLYING

    while time_flown > 0:
        if time_flown <= 0:
            break

        flying = time_can_fly
        resting = rest_time

        while flying:
            if time_flown <= 0:
                break

            if len(dist_at_every_second) > 0:
                dist_at_every_second.append(dist_at_every_second[len(dist_at_every_second)-1] + speed_while_flying)
            else:
                dist_at_every_second.append(speed_while_flying)
            flying -= 1
            time_flown -= 1

        while resting:
            if time_flown <= 0:
                break

            dist_at_every_second.append(dist_at_every_second[len(dist_at_every_second)-1])
            resting -= 1
            time_flown -= 1

    distance_reindeer[reindeer] = dist_at_every_second

x = iter(distance_reindeer)

r1 = next(x)
r2 = next(x)
r3 = next(x)
r4 = next(x)
r5 = next(x)
r6 = next(x)
r7 = next(x)
r8 = next(x)
r9 = next(x)
r1_points = 0
r2_points = 0
r3_points = 0
r4_points = 0
r5_points = 0
r6_points = 0
r7_points = 0
r8_points = 0
r9_points = 0

i = 0
while i < TOTAL_TIME_FLYING:
    max_dist_at_point = max(distance_reindeer[r1][i],
    distance_reindeer[r2][i],
    distance_reindeer[r3][i],
    distance_reindeer[r4][i],
    distance_reindeer[r5][i],
    distance_reindeer[r6][i],
    distance_reindeer[r7][i],
    distance_reindeer[r8][i],
    distance_reindeer[r9][i])

    if max_dist_at_point == distance_reindeer[r1][i]:
        r1_points += 1
    if max_dist_at_point == distance_reindeer[r2][i]:
        r2_points += 1
    if max_dist_at_point == distance_reindeer[r3][i]:
        r3_points += 1
    if max_dist_at_point == distance_reindeer[r4][i]:
        r4_points += 1
    if max_dist_at_point == distance_reindeer[r5][i]:
        r5_points += 1
    if max_dist_at_point == distance_reindeer[r6][i]:
        r6_points += 1
    if max_dist_at_point == distance_reindeer[r7][i]:
        r7_points += 1
    if max_dist_at_point == distance_reindeer[r8][i]:
        r8_points += 1
    if max_dist_at_point == distance_reindeer[r9][i]:
        r9_points += 1

    i += 1

print (max(r1_points,
    r2_points,
    r3_points,
    r4_points,
    r5_points,
    r6_points,
    r7_points,
    r8_points,
    r9_points))
