class Airplane:
    def __init__(self):
        # 20 seats (False = available, True = taken)
        self.seats = [False] * 20

        # Define seat types
        self.first_class = [0, 1, 2, 3, 4]  # Seats 1–5
        self.emergency_rows = [10, 11, 12, 13]  # Seats 11–14

        self.first_class_fee = 50.0

    def display_seats(self):
        print("\nSeat Map (O = Available, X = Taken):")
        for i in range(20):
            status = "X" if self.seats[i] else "O"
            print(f"{i + 1}:{status}", end="  ")
            if (i + 1) % 5 == 0:
                print()

    def purchase_seat(self, seat_number):
        index = seat_number - 1

        # Check valid range
        if index < 0 or index >= 20:
            print("Invalid seat number.")
            return

        # Check if taken
        if self.seats[index]:
            print("Seat already taken.")
            return

        # Emergency seat check
        if index in self.emergency_rows:
            response = input("This is an emergency row seat. Accept responsibility? (yes/no): ")
            if response.lower() != "yes":
                print("Seat not assigned.")
                return

        # First class fee
        if index in self.first_class:
            print(f"This is a first-class seat. Additional fee: ${self.first_class_fee:.2f}")
            money = float(input("Enter payment: "))
            if money < self.first_class_fee:
                print("Not enough payment. Seat not assigned.")
                return
            elif money > self.first_class_fee:
                change = money - self.first_class_fee
                print(f"Change returned: ${change:.2f}")

        # Assign seat
        self.seats[index] = True
        print(f"Seat {seat_number} successfully purchased.")

    def run(self):
        while True:
            self.display_seats()

            user_input = input("\nEnter seat number to purchase (or 0 to exit): ")

            if not user_input.isdigit():
                print("Invalid input.")
                continue

            seat_number = int(user_input)

            if seat_number == 0:
                print("Exiting program.")
                break

            self.purchase_seat(seat_number)


# Run program
plane = Airplane()
plane.run()