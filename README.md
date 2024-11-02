# Basic-Ticket-Selling-System

This code is a small program to calculate the price of a movie ticket based on a person's age and the time of the show. The program asks the user to input their age and the showtime. Depending on these inputs, it sets a ticket price and may apply a discount.

How it Works:
Input: The program first asks for the user's age and the time of the movie show (in a 24-hour format, e.g., 1400 for 2:00 PM).
Ticket Price:
Age 10 and under: The ticket costs 300 units of currency.
Ages 11 to 25: The ticket costs 500 units.
Ages 26 to 60: The ticket costs 800 units.
Over 60: The ticket costs 400 units.
Discount: If the showtime is before 5:00 PM (1700 in 24-hour format), the program applies a 10% discount to the ticket price.
Output: The program prints the original ticket price, the discount amount (if applicable), and the final price after applying the discount.
Example:
If a 9-year-old wants to see a movie at 3:00 PM (1500), the program sets the price at 300 units, applies a 10% discount (30 units), and shows a final discounted price of 270 units.
If a 30-year-old wants a ticket for a 6:00 PM (1800) show, the price is 800 units with no discount.
Error Handling:
The code includes a safety measure: if someone enters a value that isn't a number (e.g., letters instead of an age), the program will catch this mistake and prompt the user to enter the information again.
