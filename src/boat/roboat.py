import random

print("Welcome to RoboController 1.0")

 
robot_name = input("Enter robot name: ")

try:
    distance = int(input("Enter distance to target (in meters): "))
except ValueError:
    print("Invalid distance. Program terminated.")
    exit()

 
current_position = 0
speed = "Medium"
action = "Moving"
checkpoints = ["Start Point"]
obstacle_found = False    

def save_checkpoint(label):
    if len(checkpoints) < 5:   
        checkpoints.append(label)

 
while current_position < distance:

    move = random.randint(10, 25)
    current_position += move

    if current_position >= distance:
        current_position = distance
        speed = "Stop"
        action = "Destination reached → Robot stopped"
        save_checkpoint(f"{current_position}m → Destination reached")
        break

    print(f"\nRobot reached {current_position} meters")

    
    obstacle = input("Is there an obstacle ahead? (yes/no): ").lower()
    if obstacle not in ["yes", "no"]:
        print("Invalid input. Program terminated.")
        exit()

    if obstacle == "yes":
        obstacle_found = True

        obstacle_type = input(
            "Enter obstacle type (wall / pit / human / object): "
        ).lower()

        if obstacle_type not in ["wall", "pit", "human", "object"]:
            print("Invalid obstacle type. Program terminated.")
            exit()

        if obstacle_type == "wall":
            speed = "Slow"
            action = random.choice(
                ["Turn Right", "Turn Left", "Move Backward", "Move Forward"]
            )
            print("Wall detected →", action)
            save_checkpoint(f"{current_position}m → Wall handled")

        elif obstacle_type == "pit":
            speed = "Slow"
            action = random.choice(["Turn Right", "Turn Left"])
            print("Pit detected →", action)
            save_checkpoint(f"{current_position}m → Pit avoided")

        elif obstacle_type == "human":
            speed = "Stop"
            print("A human is detected wait for them to move.")
            print(".....")
            print(".....")

            moved = input("Has the human moved? (yes/no): ").lower()
            if moved not in ["yes", "no"]:
                print("Invalid input. Program terminated.")
                exit()

            if moved == "yes":
                speed = "Slow"
                action = "Human moved → Moving forward"
            else:
                action = random.choice(
                    ["Human still present → Turn Right",
                     "Human still present → Turn Left"]
                )

            print(action)
            save_checkpoint(f"{current_position}m → Human handled")

        else:
            speed = "Slow"
            action = "Avoiding object carefully"
            print(action)
            save_checkpoint(f"{current_position}m → Object avoided")

    else:
        speed = "Fast"
        action = "Moving forward"

 
checkpoints.append("Destination")

print("\nTrip Summary")
print("-" * 30)
print(f"Robot Name     : {robot_name}")
print(f"Total Distance : {distance} meters")
print(f"Final Speed    : {speed}")
print(f"Last Action    : {action}")

print("\nCheckpoints Visited:")
for point in checkpoints:
    print("•", point)

 
if not obstacle_found:
    print(f"\nNo obstacles were found. {robot_name} reached destination.")
else:
    print(f"\n{robot_name} reached destination successfully.")

print("\nRoboController 1.0 stopped at destination.")