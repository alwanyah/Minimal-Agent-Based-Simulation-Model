# Initialisierung des Roboters
robot = Robot()

# Initialisierung der Motoren
left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')

# Einstellen der maximalen Geschwindigkeit
max_speed = 6.28
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))
left_motor.setVelocity(max_speed)
right_motor.setVelocity(max_speed)

# Hauptsteuerungsschleife
while robot.step(64) != -1:
    pass