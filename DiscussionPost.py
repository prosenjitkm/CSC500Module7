

"""
Is It Already Available?
> Predefined Function: Use if the functionality you need (e.g., len(), math.sqrt()) already exists.
> User-Defined Function: Create your own if the task is unique or requires customization.
>> Example: Use len() for the length of a list but write your own function for a custom filtering rule.

Will You Reuse It?
> Predefined Function: Use for common, one-time tasks (e.g., sorting with sorted()).
> User-Defined Function: Write your own if you need to reuse custom logic across multiple parts of your program.
>> Example: A function to calculate BMI can be reused in different health-related programs.

How Complex Is the Task?
> Predefined Function: Use for simple, generic operations.
> User-Defined Function: Write your own for tasks with multiple steps or custom logic.
>> Example: Write a custom function to generate a loan payment schedule, as no predefined function exists for this.
"""

# Examples:
#Predefined Function
import math
number = 16
print(f"The square root of {number} is {math.sqrt(number)}")

#User-Defined Function
def calculate_bmi(weight, height):

    if height <= 0:
        raise ValueError("Height must be greater than zero.")
    return weight / (height ** 2)

bmi = calculate_bmi(70, 1.75)
print(f"Your BMI is {bmi:.2f}")

"""
Rule of Thumb:
> Use predefined functions for simple, common tasks.
> Write user-defined functions for custom or reusable logic.
> Balancing both makes your code efficient and clear!
"""