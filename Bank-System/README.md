# 🏦 Banking System (Python CLI Project)



A simple yet fully interactive Command-Line Banking System written in Python.  

This project allows users to create multiple accounts, deposit and withdraw money, view all accounts, and check which accounts have balances above the average.



## 🚀 Features



- ✔️ Create multiple bank accounts  

- ✔️ Validate user inputs (no negative values, no invalid numbers)  

- ✔️ Deposit into any account  

- ✔️ Withdraw with balance checking  

- ✔️ Display all accounts and balances  

- ✔️ Calculate and show accounts with above-average balance  

- ✔️ User-controlled loop to continue or exit  

- ✔️ Fully interactive terminal experience  



## 📌 How It Works



1. User enters the number of accounts  

2. For each account:  

  - Enter account owner’s name  

  - Enter initial balance (validated)  

3. The main menu provides 5 options:  

  - `1` → Show all account balances  

  - `2` → Deposit into a specific account  

  - `3` → Withdraw from a specific account  

  - `4` → Show accounts above average balance  

  - `5` → Exit  

4. After each operation (1–4), the user chooses whether to return to the menu or exit.



## 🧠 Example Account Structure



Each account is stored as a dictionary:



```python

{"name": "younes", "balance": 1500}
```

All accounts are stored in a list:
```python
accounts = []
```
📂 Project Structure
```text
Bank-System/

├── Bank-System.py   # Main program file

└── README.md        # Project documentation
```
🛠 Requirements



- Python 3.x

- No external libraries needed



▶️ How to Run
```bash
python Bank-System.py
```
🤝 Contributions

Pull requests and improvements are welcome!

Feel free to fork the repo and submit enhancements ✨

