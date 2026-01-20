class CoffeeIntakeTracker:
    """
    A class to track and analyze coffee intake.

    Attributes:
        total_coffee (float): Total coffee consumed in days.
        average_coffee_per_day (float): Average coffee consumed per day.
        total_days (int): Total number of days tracked.
        price_per_cup (float): Price per cup of coffee.
    """

    def __init__(self, price_per_cup: float = 2.0):
        """
        Initializes the CoffeeIntakeTracker.

        Args:
            price_per_cup (float, optional): Price per cup of coffee. Defaults to 2.0.
        """
        self.total_coffee = 0
        self.average_coffee_per_day = 0
        self.total_days = 0
        self.price_per_cup = price_per_cup

    def add_coffee(self, amount: float) -> None:
        """
        Adds coffee to the tracker.

        Args:
            amount (float): Amount of coffee consumed.
        """
        try:
            if amount <= 0:
                raise ValueError("Amount must be greater than zero.")
            self.total_coffee += amount
            self.total_days += 1
        except ValueError as e:
            print(f"Error: {e}")

    def calculate_average(self) -> float:
        """
        Calculates the average coffee consumed per day.

        Returns:
            float: Average coffee consumed per day.
        """
        if self.total_days == 0:
            return 0
        return self.total_coffee / self.total_days

    def calculate_total_cost(self) -> float:
        """
        Calculates the total cost of coffee.

        Returns:
            float: Total cost of coffee.
        """
        try:
            return self.total_coffee * self.price_per_cup
        except TypeError as e:
            print(f"Error: {e}")
            return 0

    def display_stats(self) -> None:
        """
        Displays the statistics.
        """
        average = self.calculate_average()
        total_cost = self.calculate_total_cost()
        print(f"Total Coffee Consumed: {self.total_coffee} cups")
        print(f"Average Coffee Consumed per Day: {average:.2f} cups")
        print(f"Total Days Tracked: {self.total_days}")
        if total_cost > 0:
            print(f"Total Cost of Coffee: ${total_cost:.2f}")


def main() -> None:
    """
    Main function.
    """
    tracker = CoffeeIntakeTracker()
    while True:
        try:
            action = input("Enter 'add' to add coffee, 'stats' to display stats, or 'exit' to quit: ")
            if action.lower() == "add":
                amount = float(input("Enter the amount of coffee consumed (in cups): "))
                tracker.add_coffee(amount)
            elif action.lower() == "stats":
                tracker.display_stats()
            elif action.lower() == "exit":
                break
            else:
                print("Invalid action. Please try again.")
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()