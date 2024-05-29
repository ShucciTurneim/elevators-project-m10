import Elevator
import Floor

def elevators_builder(elevators_num):
        for elevator_num in range(1,elevators_num+1):
            elevator = f"elevator_{elevator_num}"
            elevator = Elevator
            elevator.build_elevator(elevator_num)

def floors_builder(floors_num):
    for elevator_num in range(1,floors_num+1):
        floor = f"floor_{elevator_num}"
        floor = Floor
        floor.build_floor(floors_num)

def new_building_architect(floors_num,elevators_num):
    elevators_builder(elevators_num)
    floors_builder(floors_num)
    
        