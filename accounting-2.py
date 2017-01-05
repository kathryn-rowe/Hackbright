the_file = open("customer-orders.txt")
for line in the_file:
    line = line.rstrip()
    words = line.split('|')

    customer_name = words[1]
    customer_melons = float(words[2])
    customer_paid = float(words[3])
    melon_cost = 1.00

    customer_expected = customer_melons * melon_cost

    if customer_expected != customer_paid:
        print "%s paid $%.2f, but we expected $%.2f" % (customer_name, customer_paid, customer_expected)
