
import random
""" elevator class  """
class elevator:
    def __init__(self, elevatorid, floor = 1, goal_floor = 1):
        self.elevatorid = elevatorid        #uniqueID
        self.floor = floor                  #current floor of elevator
        self.goal_floor = goal_floor
        self.goal_floors = []       
        self.direction = None
        self.update_bookeeping()                 #instatiates the direction

    """Returns void updates the goal floor of the elevator """
    def update_goalfloor(self, goal_floor):
        self.goal_floor = goal_floor
        self.update_bookeeping()

    def update_curr_floor(self, floor):
        self.floor = floor
        self.update_bookeeping()

    """Updates the current floor of the elevator according to its goal floor"""
    def step(self):
        if self.direction == "up":
            self.floor += 1
        elif self.direction == "down":
            self.floor -= 1
        self.update_bookeeping()
    
    """Helper function to updates the current direction of elevator movement"""
    def update_bookeeping(self):
        #reach goal floor
        if self.goal_floor > self.floor:
            self.direction = "up"
        elif self.goal_floor < self.floor:
            self.direction = "down"

        else: 
            #at the goal floor, so update to another goal floor
            if len(self.goal_floors) != 0:
                new_goal = self.goal_floors.pop(0)
                self.update_goalfloor(new_goal)
            else:
                self.direction = "nowhere"
        
    def add_pickup(self, goal_floor):
        self.goal_floors.append(goal_floor)
        self.update_bookeeping()           

    """rtype: string """
    def get_direction_of_movement(self):
        return self.direction

    """rtype: bool """
    def moving_up(self):
        return self.direction == "up"
    
    """rtype: bool """
    def moving_down(self):
        return self.direction == "down"

    """rtype: bool """
    def not_moving(self):
        return self.direction == "nowhere"

    """ rtype: void"""
    def get_status(self):
        print("the elevator {} is at floor {} going to floor {}. It is moving {}".
                format(self.elevatorid, self.floor, self.goal_floor, self.direction))


""" elevator control class """
class elevator_control:

    def __init__(self):
        self.num_ele = 0
        self.list_elevators = []

    def add_elevator(self):
        new_ele = elevator(self.num_ele)
        self.num_ele += 1
        self.list_elevators.append(new_ele)
    
    #update goal floor and current floor
    def update(self, elevatorid, goal_floor, floor = None):
        elevator = self.list_elevators[elevatorid]
        if floor != None:
            elevator.update_curr_floor(floor)
        elevator.update_goalfloor(goal_floor)
    
    """do first come first served of the Least Recently Used Elevator"""
    def pickup(self, floor, direction):
        if direction > 0:
            direction = "up"
        else:
            direction = "down"

        elevator_for_pickup = None
        #find the first elevator that is not moving
        for elevator in self.list_elevators:
            if elevator.not_moving():
                elevator_for_pickup = elevator
                break

        #find a random elevator from the list
        #TODO create an intelligent way to find the elevator 
        #TODO create method in elevator class to create a intermediate goal floor
        if elevator_for_pickup is None:
            rnd = random.randint(0,len(self.list_elevators)-1)

            print("picking up random elevator number {}".format(rnd))
            elevator_for_pickup = self.list_elevators[rnd]
                
        elevator_for_pickup.add_pickup(floor)

    def status(self):
        print()
        print("Moving one step for each elevator...")
        print()
        for elevator in self.list_elevators:
            elevator.get_status()

    def step(self):
        for elevator in self.list_elevators:
            elevator.step()

"""first Unit test of elevator going from 1 to ten and stopping at thirteen for 3 steps"""
def testElevatorClassMovingUpToTen():
    print()
    testEle = elevator(1, 1, 10)
    for i in range(13):
        testEle.get_status()
        testEle.step()

"""test of 2 elevators: one moving up and another moving down"""
def testElevatorClassTwoElevatorMovingUp():
    print()
    testEle = elevator(1, 1, 10)
    testEle2 = elevator(2, 12, 8)
    for i in range(13):
        testEle.get_status()
        testEle.step()
        testEle2.get_status()
        testEle2.step()    

"""testing the elevator control system"""
def testElevatorControlCreateAElevatorThatGoesNowhere():
    test = elevator_control()
    test.add_elevator()
    test.status()

def elevatorControlShouldAddAndUpdate2Elevators_OneElevatorGoesUpDownStop_AnotherMovesUpStop():
    test = elevator_control()
    test.add_elevator()
    test.add_elevator()
    test.update(0, 10)
    test.update(1, 5)

    for i in range(3):
        test.status()
        test.step()
    test.status()
    test.update(0, 1)
    test.update(1, 4)
    for i in range(3):
        test.status()
        test.step()
    test.status()

def pickUpRequestForOneElevatorShouldGoTo_10_9_4_7():
    test = elevator_control()
    test.add_elevator()
    test.update(0, 10)
    test.pickup(9, -1)
    test.pickup(4, 1)
    test.pickup(7, -1)

    for i in range(20):
        test.status()
        test.step()


def notMovingElevatorsShouldPickUp_AllElevatorShouldBeWorking():
    test = elevator_control()

    test.add_elevator()
    test.add_elevator()
    test.add_elevator()
    test.add_elevator()
    
    test.pickup(9, -1)
    test.pickup(4, 1)
    test.pickup(7, -1)
    
    for i in range(6):
        test.status()
        test.step()
    test.pickup(10, 1)

    for i in range(10):
        test.status()
        test.step()

def pickUpRequestForTwoElevatorsShouldChooseRandomlyButShouldGoTo_9_4_7_10():
    test = elevator_control()
    test.add_elevator()
    test.add_elevator()
    test.pickup(9, -1)
    test.pickup(4, 1)
    test.pickup(7, -1)

    for i in range(6):
        test.status()
        test.step()
    test.pickup(10, 1)

    for i in range(10):
        test.status()
        test.step()

def main():


if __name__ == '__main__':
    main()