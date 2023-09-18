MAX_LINES = 3 #constant variable, and won't change
MAX_BET=100
MIN_BET=1
def deposit():
    while True: #continue to ask the user for amount until they give a valid amount
        amount=input("How much would you like to deposit? $")
        if amount.isdigit(): #checks if the string has digits
            amount=int(amount)
            if amount > 0:
                break
            else:
                print("Amount cannot be less than 0")
        else:
            print("Please enter a number.")
    return amount

def get_number_of_lines():
    while True: #continue to ask the user for amount until they give a valid amount
        lines=input("Enter the number of lines to bet on (1-" + str(MAX_LINES)+")? ")
        if lines.isdigit(): #checks if the string has digits
            lines=int(lines)
            if 1 <= lines <=MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Please enter a number.")
    return lines
def get_bet():
    while True: #continue to ask the user for amount until they give a valid amount
        amount=input("How much would you like to bet on each line? $")
        if amount.isdigit(): #checks if the string has digits
            amount=int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")
    return amount
def main():
    balance = deposit()
    lines=get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You do not have enough to bet that amount, you current balance is ${balance}")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines.Total bet is equal to ${total_bet}")
    

main()