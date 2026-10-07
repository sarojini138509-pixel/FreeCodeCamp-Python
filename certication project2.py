def create_spend_chart(categories):
    spending = []

    for category in categories:
        total = 0
        for item in category.ledger:
            if item["amount"] < 0:
                total += -item["amount"]
        spending.append(total)

    total_spending = sum(spending)

    percentages = []
    for amount in spending:
        percentage = int((amount / total_spending) * 100)
        percentage = (percentage // 10) * 10
        percentages.append(percentage)

    chart = "Percentage spent by category\n"

    # Bar chart
    for level in range(100, -1, -10):
        chart += f"{level:>3}|"

        for percentage in percentages:
            if percentage >= level:
                chart += " o "
            else:
                chart += "   "

        chart += " \n"

    # Horizontal line
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Category names vertically
    max_length = max(len(category.name) for category in categories)

    for i in range(max_length):
        chart += "     "

        for category in categories:
            if i < len(category.name):
                chart += category.name[i]
            else:
                chart += " "

            chart += "  "

        chart += "\n"

    return chart.rstrip("\n")
