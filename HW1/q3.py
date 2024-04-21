# 3.Stock Transaction Program
# Last month, Joe purchased some stock in Acme Software, Inc. Here are the details of the
# purchase:
# • The number of shares that Joe purchased was 2,000.
# • When Joe purchased the stock, he paid $40.00 per share.
# • Joe paid his stockbroker a commission that amounted to 3 percent of the amount he paid
# for the stock.
# Two weeks later, Joe sold the stock. Here are the details of the sale:
# • The number of shares that Joe sold was 2,000.
# • He sold the stock for $42.75 per share.
# • He paid his stockbroker another commission that amounted to 3 percent of the amount
# he received for the stock.
# Write a program that displays the following information:
# • The amount of money Joe paid for the stock.
# • The amount of commission Joe paid his broker when he bought the stock.
# • The amount for which Joe sold the stock.

# 116 Chapter 2 Input, Processing, and Output
# • The amount of commission Joe paid his broker when he sold the stock.
# • Display the amount of money that Joe had left when he sold the stock and paid his
# broker (both times). If this amount is positive, then Joe made a profit. If the amount is
# negative, then Joe lost money.

number_share = 2000
price_pay = 40.00
price_sold = 42.75
commision_percent = 0.03

amount_paid = number_share * price_pay
commision_paid = amount_paid * commision_percent
amount_sold = number_share * price_sold
commision_sold = amount_sold * commision_percent
remaining = (amount_sold - commision_sold) - (amount_paid - commision_paid)

print(f"The amount of money Joe paid for the stock:{amount_paid:^.2f}\n"
      f"The amount of commission Joe paid his broker when he bought the stock:{commision_paid:^.2f}\n"
      f"The amount for which Joe sold the stock:{amount_sold:^.2f}\n"
      f"The amount of commission Joe paid his broker when he sold the stock:{commision_sold:^.2f}\n"
      )

if (remaining > 0):
    print("Joe made a profit")
else:
    print("Joe lost money")
