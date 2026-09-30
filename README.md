# Number Analyzer

A Python script that takes any amount of numbers as input and analyzes them: total, average, largest, smallest, and counts of positive, negative, zero, even, and odd numbers.

## What it does

- Asks how many numbers you want to enter, then takes that many numbers as input
- Calculates the total of all numbers
- Calculates the average
- Finds the largest and smallest number
- Counts how many numbers are positive, negative, and zero
- Counts how many numbers are even and odd

## How to run

```bash
python number_analyzer.py
```

You'll first be asked how many numbers to enter, then prompted to enter each one.

## Example

```
How many numbers you want to enter: 5
Enter the number: 10
Enter the number: -3
Enter the number: 0
Enter the number: 7
Enter the number: 4
Total: 18
Average: 3.6
Largest number: 10
Smallest number: -3
Number of positive integers: 3
Number of negative integers: 1
Number of zeros: 1
Number of even numbers: 3
Number of odd numbers: 2
```

## Status

This is a small, growing learning project. It started as a fixed 5-marks analyzer and has been generalized to accept any amount of numbers and analyze them in more detail.

Planned improvements:
- Input validation (handle non-numeric input)
- Round the average to 2 decimal places
- Add median and mode calculation
- Let the user analyze decimal numbers too, not just integers

## Author

Built while learning Python fundamentals: functions, loops, and conditionals.
