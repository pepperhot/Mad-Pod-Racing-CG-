boost = 1

while True:
    thrust = 100
    x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [int(i) for i in input().split()]
    opponent_x, opponent_y = [int(i) for i in input().split()]

    if abs(next_checkpoint_angle) > 90:
        thrust = 20
    elif abs(next_checkpoint_angle) < 30:
        thrust = 100
    elif next_checkpoint_dist < 1000:
        thrust = 50

    if boost and next_checkpoint_dist < 5000 and abs(next_checkpoint_angle) < 20:
        thrust = "BOOST"
        boost = 0

    if opponent_x > x and opponent_y > y and next_checkpoint_dist < 5000 and not boost:
        thrust = 80

    print(f"{next_checkpoint_x} {next_checkpoint_y} {thrust}")
