## README - Python Vending Machine Simulator

This Python code simulates a simple vending machine with minimal change dispensing functionality.

**Features:**

* Supports various drink options with prices
* Accepts whole notes of denominations: RM1, RM5, RM10, RM20, RM50, and RM100
* Dispenses change using the least amount of notes possible

**Running the Script:**

```bash
python main.py
```

**How to Use:**

1. The program will display a list of available drinks with their codes and prices.
2. Enter the code of the drink you want to purchase (e.g., A1, B2, etc.).
3. Insert cash (whole notes only) one at a time until the inserted amount reaches or exceeds the drink price. Valid denominations are RM1, RM5, RM10, RM20, RM50, and RM100.
4. If the inserted amount is sufficient, the program will dispense the chosen drink and provide any remaining change using the least amount of notes possible.

**Example:**

```
Available drinks:
A1: Coke (RM3)
B2: Sprite (RM5)
C3: 100 Plus (RM2)
D4: Water (RM1)
Enter drink code: B2

You chose Sprite (RM5).
Insert amount (whole notes only): 1
Insert amount (whole notes only): 1
Insert amount (whole notes only): 1
Insert amount (whole notes only): 10

Dispensing your Sprite.
Change:
1 x RM5 notes
3 x RM1 notes
```


**Further Enhancements:**

* Add support for coins
* Implement stock management for drinks
* Create a UI
* Add error catching
