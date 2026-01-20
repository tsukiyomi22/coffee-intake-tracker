# Coffee Intake Tracker
[![Python 3.9+](https://img.shields.io/pypi/v/coffee-intake-tracker.svg)](https://pypi.org/project/coffee-intake-tracker/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Description

A simple command-line application to track daily coffee intake. This project allows users to input their daily coffee consumption, calculates the total coffee intake, displays the average coffee per day, tracks the total days, and optionally calculates the total cost.

## Installation Instructions

To install the Coffee Intake Tracker, run the following command:

```bash
pip install coffee-intake-tracker
```

Alternatively, you can clone the repository using Git:

```bash
git clone https://github.com/your-username/coffee-intake-tracker.git
cd coffee-intake-tracker
pip install -r requirements.txt
```

## Usage Examples

Here are some examples of how to use the Coffee Intake Tracker:
```python
# Create a new tracker instance
tracker = CoffeeIntakeTracker()

# Set daily coffee consumption for today
tracker.set_coffee_consumption(200)

# Calculate total coffee intake
print(tracker.get_total_coffee_intake())

# Display average coffee per day
print(tracker.get_average_coffee_per_day())

# Track the total days
tracker.increment_days()
print(tracker.get_total_days())

# Optional calculation of total cost (not implemented yet)
```

## Features

*   **User input of daily coffee consumption**: Enter your daily coffee consumption in milliliters.
*   **Calculation of total coffee intake**: The tracker calculates and displays the total coffee intake for all days tracked.
*   **Display of average coffee per day**: The tracker displays the average coffee consumed per day.
*   **Tracking of total days**: The tracker tracks the number of days since the last input was made.
*   **Optional calculation of total cost**: Calculates the total cost based on an assumed price per milliliter (not implemented yet).

## License

The Coffee Intake Tracker is licensed under the [MIT License](https://opensource.org/licenses/MIT). This license allows for free use, modification, and distribution of the software.

## Contributing

Contributions to the Coffee Intake Tracker are welcome! If you'd like to contribute, please fork the repository and submit a pull request.