import accounts 
import transactions

accounts.createAccount(1001,"John",1500)

transactions.deposit(1001,800)

transactions.withdraw(1001,100)

print("balance:",accounts.getBalance(201))