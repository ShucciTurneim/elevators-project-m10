import elevator

elevators = set()

def dst_arrival_time(dst,elevator):
       return abs(elevator.absolute_stop - dst)/2                           #
    

def get_priority_elevator(dst):
    min_possible_time = 0
    for elevator in elevators:    
                          #from eli class
        arrival_time = elevator.operation_duration + dst_arrival_time(dst,elevator) - elevator.elapsed_time
        if min_possible_time > arrival_time: 
            min_possible_time = arrival_time
            property__elevator = elevator
    return property__elevator
                              
def send_new_mission_algorithm(floor):
    priority_elevator = get_priority_elevator(floor)
    priority_elevator.send_order(floor) 