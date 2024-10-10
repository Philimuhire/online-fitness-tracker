from collections import deque

#stack for undoing work out entries
class WorkoutStack:
    def __init__(self):  #constructor to initialize the stack
        self.stack = []
    
    def add_workout(self, workout):  #add work out to the stack
        self.stack.append(workout)
        print(f"Workout '{workout}' added to stack.")
    
    def undo_workout(self): #remove work out from the stack
        if self.stack:
            workout = self.stack.pop()  # to remove the last item from the stack
            print(f"Workout '{workout}' undone.")
            return workout
        else:
            print("No workout to undo!")
            return None

class WorkoutQueue:   # for scheduling upcoming workout
    def __init__(self):
        self.queue = deque()
    
    def schedule_workout(self, workout):
        self.queue.append(workout)
        print(f"Workout '{workout}' scheduled.")
    
    def next_workout(self):
        if self.queue:
            workout = self.queue.popleft()
            print(f"Workout '{workout}' started.")
            return workout
        else:
            print("No upcoming workouts!")
            return None

class CompletedWorkouts: # to track complected exercises
    def __init__(self):
        self.completed_list = []
    
    def complete_workout(self, workout):
        self.completed_list.append(workout)
        print(f"Workout '{workout}' marked as complete.")
    
    def view_completed(self):
        if self.completed_list:
            print("Completed workouts:", self.completed_list)
        else:
            print("No workouts completed yet!")

def main():

    undo_stack = WorkoutStack()
    workout_queue = WorkoutQueue()
    completed_workouts = CompletedWorkouts()

    while True:
        print("\nOptions:")
        print("1. Add workout to undo stack")
        print("2. Undo last workout")
        print("3. Schedule a workout")
        print("4. Start the next workout")
        print("5. Complete a workout")
        print("6. View completed workouts")
        print("7. Exit")
        
        choice = input("\nChoose an option: ")

        if choice == "1":
            workout = input("Enter the workout to add to undo stack: ")
            undo_stack.add_workout(workout)
        elif choice == "2":
            undo_stack.undo_workout()
        elif choice == "3":
            workout = input("Enter the workout to schedule: ")
            workout_queue.schedule_workout(workout)
        elif choice == "4":
            workout_queue.next_workout()
        elif choice == "5":
            workout = input("Enter the workout to mark as complete: ")
            completed_workouts.complete_workout(workout)
        elif choice == "6":
            completed_workouts.view_completed()
        elif choice == "7":
            print("Exiting the fitness tracker...")
            break
        else:
            print("Invalid option! Please try again.")

if __name__ == "__main__":
    main()