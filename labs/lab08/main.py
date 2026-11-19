# CS 31 - Lab
# Exercises 8-1 and 8-2
# Date: November 15, 2026
# Philip R.


from decimal import Decimal
from decimal import ROUND_HALF_UP
import locale as lc

# display a title
print("The Invoice program")
print()

choice = "y"
while choice == "y":

    # get the user entry
    order_total = Decimal(input("Enter order total: "))
    order_total = order_total.quantize(Decimal("1.00"), ROUND_HALF_UP)
    print()

    # determine the discount percent
    if order_total > 0 and order_total < 100:
        discount_percent = Decimal("0")
    elif order_total >= 100 and order_total < 250:
        discount_percent = Decimal(".1")
    elif order_total >= 250:
        discount_percent = Decimal(".2")
    else:
        discount_percent = Decimal("0")

    # calculate the results
    discount = order_total * discount_percent
    discount = discount.quantize(Decimal("1.00"), ROUND_HALF_UP)
    subtotal = order_total - discount

    # add shipping costs
    shipping_percent = Decimal(".085")
    shipping_cost = subtotal * shipping_percent
    shipping_cost = shipping_cost.quantize(Decimal("1.00"), ROUND_HALF_UP)

    tax_percent = Decimal(".05")
    sales_tax = subtotal * tax_percent
    sales_tax = sales_tax.quantize(Decimal("1.00"), ROUND_HALF_UP)
    invoice_total = subtotal + sales_tax + shipping_cost

    # add the spec format values
    spec = "10.2f"
    spec_currency = ">10"
    spec_literal = 20

    # work with locale to include a $ in the decimal value
    lc.setlocale(lc.LC_ALL, "en_US.UTF-8")
    order_total_display = lc.currency(order_total, grouping=True)
    invoice_total_display = lc.currency(invoice_total, grouping=True)

    # display the results
    print(f"{'Order total:':{spec_literal}}{order_total_display:{spec_currency}}")
    print(f"{'Discount amount:':{spec_literal}}{discount:{spec}}")
    print(f"{'Subtotal:':{spec_literal}}{subtotal:{spec}}")
    print(f"{'Shipping cost:':{spec_literal}}{shipping_cost:{spec}}")
    print(f"{'Sales tax:':{spec_literal}}{sales_tax:{spec}}")
    print(f"{'Invoice total:':{spec_literal}}{invoice_total_display:{spec_currency}}")
    print()

    choice = input("Continue? (y/n): ")
    print()

print("Bye!")
