class FlightProcess:
    def __init__(self, pid, process_name, start_time, priority):
        self.pid = pid
        self.process_name = process_name
        self.start_time = start_time
        self.priority = priority

class FlightTable:
    def __init__(self):
        self.processes = []

    def add_process(self, process):
        self.processes.append(process)

    def sort_by_pid(self):
        self.processes.sort(key=lambda process: process.pid)

    def sort_by_start_time(self):
        self.processes.sort(key=lambda process: process.start_time)

    def sort_by_priority(self):
        self.processes.sort(key=lambda process: process.priority, reverse=True)

    def print_table(self):
        print("P_ID\tProcess\tStart Time\tPriority")
        for process in self.processes:
            print(f"{process.pid}\t{process.process_name}\t{process.start_time}\t\t{process.priority}")

def main():
    flight_table = FlightTable()

    flight_table.add_process(FlightProcess("P1", "VSCode", 100, "MID"))
    flight_table.add_process(FlightProcess("P23", "Eclipse", 234, "MID"))
    flight_table.add_process(FlightProcess("P93", "Chrome", 189, "High"))
    flight_table.add_process(FlightProcess("P42", "JDK", 9, "High"))
    flight_table.add_process(FlightProcess("P9", "CMD", 7, "High"))
    flight_table.add_process(FlightProcess("P87", "NotePad", 23, "Low"))

    while True:
        print("\nSorting Options:")
        print("1. Sort by P_ID")
        print("2. Sort by Start Time")
        print("3. Sort by Priority")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            flight_table.sort_by_pid()
        elif choice == 2:
            flight_table.sort_by_start_time()
        elif choice == 3:
            flight_table.sort_by_priority()
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please enter a valid option.")

        flight_table.print_table()

if __name__ == "__main__":
    main()
#comment