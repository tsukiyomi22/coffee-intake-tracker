import pytest
from coffee_intake_tracker import CoffeeIntakeTracker

def test_coffee_intake_tracker_init():
    tracker = CoffeeIntakeTracker()
    assert tracker.total_coffee == 0
    assert tracker.average_coffee_per_day == 0
    assert tracker.total_days == 0
    assert tracker.price_per_cup == 2.0

def test_coffee_intake_tracker_add_coffee_positive_amount():
    tracker = CoffeeIntakeTracker()
    tracker.add_coffee(1)
    assert tracker.total_coffee == 1
    assert tracker.total_days == 1

def test_coffee_intake_tracker_add_coffee_zero_amount():
    tracker = CoffeeIntakeTracker()
    with pytest.raises(ValueError):
        tracker.add_coffee(0)

def test_coffee_intake_tracker_add_coffee_negative_amount():
    tracker = CoffeeIntakeTracker()
    with pytest.raises(ValueError):
        tracker.add_coffee(-1)

def test_coffee_intake_tracker_calculate_average_zero_days():
    tracker = CoffeeIntakeTracker()
    assert tracker.calculate_average() == 0

def test_coffee_intake_tracker_calculate_average_non_zero_days():
    tracker = CoffeeIntakeTracker()
    tracker.add_coffee(10)
    tracker.add_coffee(20)
    assert round(tracker.calculate_average(), 2) == 15.0

def test_coffee_intake_tracker_calculate_total_cost_positive_amount():
    tracker = CoffeeIntakeTracker()
    tracker.add_coffee(1)
    assert tracker.calculate_total_cost() > 0

def test_coffee_intake_tracker_calculate_total_cost_zero_amount():
    tracker = CoffeeIntakeTracker()
    assert tracker.calculate_total_cost() == 0

def test_coffee_intake_tracker_display_stats():
    tracker = CoffeeIntakeTracker()
    tracker.add_coffee(10)
    tracker.display_stats()

def test_coffee_intake_tracker_invalid_action():
    tracker = CoffeeIntakeTracker()
    with pytest.raises(ValueError):
        tracker.add_coffee("invalid")

def test_coffee_intake_tracker_non_numeric_input():
    tracker = CoffeeIntakeTracker()
    with pytest.raises(ValueError):
        tracker.add_coffee("hello")