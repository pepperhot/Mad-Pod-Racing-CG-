import sys
import math

surface_n = int(input())
target_x1, target_y1, target_x2, target_y2 = 0, 0, 0, 0
last_x, last_y = 0, 0

for _ in range(surface_n):
    land_x, land_y = map(int, input().split())
    if last_y == land_y:
        target_x1, target_y1, target_x2, target_y2 = last_x, last_y, land_x, land_y
    last_x, last_y = land_x, land_y

stage = 1
approach_from = ''
counter = 0

while True:
    counter += 1
    x, y, h_speed, v_speed, fuel, rotate, power = map(int, input().split())
    v_speed = -v_speed if v_speed > 0 else v_speed

    if h_speed != 0 and v_speed != 0:
        aoa = math.atan2(v_speed, h_speed)
        vector_mag = math.hypot(h_speed, v_speed)
        g = 3.711
        y0 = y - target_y1
        distance = (
            (vector_mag**2 / (2 * g)) *
            (1 + (1 + ((2 * g * y0) / (vector_mag**2 * math.sin(aoa)**2)))**0.5)
        ) * math.sin(2 * aoa)
        distance = int(distance) * -1

    angle = 0
    thrust = 4

    if stage == 1:
        if x < target_x1:
            approach_from = "left"
            angle = -40
            if abs(h_speed) > 40:
                stage = 2
        elif x > target_x2:
            approach_from = "right"
            angle = 40
            if abs(h_speed) > 40:
                stage = 2

    elif stage == 2:
        angle = 0
        thrust = 3 if counter % 20 == 0 else 4
        comp_dist = int((distance * 0.3) * abs(h_speed * 0.01))
        if (approach_from == "left" and x + comp_dist > target_x1) or \
           (approach_from == "right" and x + comp_dist < target_x2):
            stage = 3

    elif stage == 3:
        opp_aoa = max(min(int((math.degrees(aoa) - 90) % 360 - 180), 70), -70)
        angle = opp_aoa if abs(h_speed) > 1 else 0
        if angle == 0:
            stage = 4

    elif stage == 4:
        thrust = 4 if v_speed < -30 else 3

    print(f"{angle} {thrust}")
