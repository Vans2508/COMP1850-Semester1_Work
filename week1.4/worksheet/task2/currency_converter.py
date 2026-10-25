
"""
    Portfolio Task - Week 4

    By submitting this code you are declaring that all work in this file,
    other than any provided template code, was written and developed by
    you independently.

    Name:
"""

def currency_converter(amount, from_currency, to_currency):

    conversion_rate = {
        'GBP': {'CNY': 9.24, 'PHP': 75.00, 'INR': 109.06},
        'CNY': {'GBP': 0.11, 'PHP': 8.12, 'INR': 11.81},
        'PHP': {'CNY': 0.12, 'GBP': 0.01, 'INR': 1.45},
        'INR': {'PHP': 0.69, 'CNY': 0.09, 'GBP': 0.01}
    }
    if amount > 0:
        if from_currency == "GBP":
            converted_currency = float(conversion_rate[from_currency][to_currency]) * amount
        elif from_currency == "CNY":
            converted_currency = float(conversion_rate[from_currency][to_currency]) * amount
        elif from_currency == "PHP":
            converted_currency = float(conversion_rate[from_currency][to_currency]) * amount
        elif from_currency == "INR":
            converted_currency = float(conversion_rate[from_currency][to_currency]) * amount
    else:
        return 0.0
    # your code here

    return (f"{converted_currency} {to_currency}")

# Submit only this file currency_converter.py with the completed function.

# Remove any additional code you may have added during development and testing.
