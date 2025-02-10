import os


# Constants for revenue calculations
subscription_rates = {
    "daily": 300,  # ₦ per day
    "monthly": 2000,  # ₦ per month
    "annual": 30000,  # ₦ per year
}
subscription_uptake = {
    "daily": 0.08,  # 8% of new users
    "monthly": 0.20,  # 20% of total users
    "annual": 0.02,  # 2% of new users
}
advertisement_rates = {
    "CPM": 365,  # ₦ per 1,000 impressions
    "CPC": 110,  # ₦ per click
    "CPA": 545,  # ₦ per action
    "push": 70000,  # ₦ per notification
}
advertisement_activity = {
    "CPM": 3,  # impressions per user per month
    "CPC": 1.5,  # clicks per user per month
    "CPA": 0.2,  # actions per user per month
    "push": 1,  # notifications per month
}

# Monthly user numbers for each year
full_monthly_user_growth = {
    2025: [0, 0, 0, 0, 833, 2144, 3455, 4766, 6077, 7388, 8699, 10000],
    2026: [13333, 16667, 20000, 23333, 26667, 30000, 33333, 36667, 40000, 43333, 46667, 50000],
    2027: [54167, 58333, 62500, 66667, 70833, 75000, 79167, 83333, 87500, 91667, 95833, 100000],
    2028: [108333, 116667, 125000, 133333, 141667, 150000, 158333, 166667, 175000, 183333, 191667, 200000],
    2029: [223583, 247167, 270750, 294333, 317917, 341500, 365083, 388667, 412250, 435833, 459417, 483000],
}

# Function to calculate revenues
def calculate_revenues():
    annual_results = {}
    previous_year_end_users = 0  # Initialize the previous year end users

    for year, user_growth in full_monthly_user_growth.items():
        total_sporadic_users = 0
        total_annual_users = 0
        total_ad_users = 0
        total_CPM = 0
        total_CPC = 0
        total_CPA = 0
        total_push = 0
        total_daily_subscribers = 0
        total_annual_subscribers = 0
        total_monthly_subscribers = 0

        monthly_revenues = []

        for i in range(12):
            # Determine new users for the current month
            current_users = user_growth[i]
            if i == 0:
                previous_users = previous_year_end_users  # Use the previous year end users for the first month
            else:
                previous_users = user_growth[i - 1]
            new_users = max(current_users - previous_users, 0)

            # Calculate subscriber uptakes
            annual_subscribers = new_users * subscription_uptake["annual"]
            sporadic_subscribers = new_users * subscription_uptake["daily"]
            monthly_subscribers = new_users * subscription_uptake["monthly"]

            # Accumulate annual and sporadic subscribers
            total_annual_users += annual_subscribers
            total_sporadic_users += sporadic_subscribers

            # Adjust ad users
            ad_users = current_users - total_annual_users - total_monthly_subscribers

            # Exclude sporadic subscribers from ads for the last 10 days of December
            if i == 11:
                ad_users -= total_sporadic_users * (10 / 365)

            total_ad_users += ad_users

            # Calculate revenues
            subscription_revenue = (
                annual_subscribers * subscription_rates["annual"] +
                sporadic_subscribers * subscription_rates["daily"] * 10 +
                monthly_subscribers * subscription_rates["monthly"]
            )

            if current_users > 0:
                push_revenue = advertisement_rates["push"]
                total_push += 1
            else:
                push_revenue = 0

            monthly_CPM = (ad_users/1000 * advertisement_rates["CPM"]) * advertisement_activity["CPM"] if ad_users > 1000 else 0
            monthly_CPC = (ad_users * advertisement_rates["CPC"]) * advertisement_activity["CPC"]
            monthly_CPA = (ad_users * advertisement_activity["CPA"]) * advertisement_rates["CPA"]

            ad_revenue = (
                monthly_CPM + monthly_CPA + monthly_CPC + push_revenue
            )

            total_CPM += monthly_CPM
            total_CPC += monthly_CPC
            total_CPA += monthly_CPA
            total_daily_subscribers += sporadic_subscribers
            total_annual_subscribers += annual_subscribers
            total_monthly_subscribers += monthly_subscribers

            monthly_revenues.append({
                "month": i + 1,
                "subscription_revenue": subscription_revenue,
                "ad_revenue": ad_revenue,
                "total_revenue": subscription_revenue + ad_revenue,
                "CPM": monthly_CPM,
                "CPC": monthly_CPC,
                "CPA": monthly_CPA,
                "push": total_push,
            })

        # Store results for the year
        annual_results[year] = {
            "monthly_revenues": monthly_revenues,
            "total_subscription_revenue": sum(m["subscription_revenue"] for m in monthly_revenues),
            "total_ad_revenue": sum(m["ad_revenue"] for m in monthly_revenues),
            "total_revenue": sum(m["total_revenue"] for m in monthly_revenues),
            "total_CPM": total_CPM,
            "total_CPC": total_CPC,
            "total_CPA": total_CPA,
            "total_push": total_push,
            "total_daily_subscribers": total_daily_subscribers,
            "total_annual_subscribers": total_annual_subscribers,
            "total_monthly_subscribers": total_monthly_subscribers,
        }

        # Update the previous year end users for the next year's calculation
        previous_year_end_users = user_growth[-1]

    return annual_results

# Open file to write output
file_path = os.path.join(os.path.dirname(__file__), "revenue_projections.txt")
with open(file_path, 'w', encoding="utf-8") as file:
    # Write header
    file.write("Revenue Projections Report\n")
    file.write("=" * 50 + "\n\n")

    # Run the calculation and print results
    results = calculate_revenues()
    for year, data in results.items():
        file.write(f"Year: {year}\n")
        for month_data in data["monthly_revenues"]:
            file.write(
                f"Month {month_data['month']}:\n Subscription: ₦{month_data['subscription_revenue']:,.2f}, \n"
                f"Ads: ₦{month_data['ad_revenue']:,.2f}, Total: ₦{month_data['total_revenue']:,.2f}, \n"
                f"CPM: {month_data['CPM']:,.2f}, CPC: {month_data['CPC']:,.2f}, CPA: {month_data['CPA']:,.2f}, Push: {month_data['push']} \n\n"
            )
        file.write(
            f"Total Subscription Revenue: ₦{data['total_subscription_revenue']:,.2f}, \n"
            f"Total Ad Revenue: ₦{data['total_ad_revenue']:,.2f}, \n"
            f"Total Revenue: ₦{data['total_revenue']:,.2f}, \n"
            f"Total CPM Impressions: {data['total_CPM']:,.2f}, \n"
            f"Total CPC Clicks: {data['total_CPC']:,.2f}, \n"
            f"Total CPA Actions: {data['total_CPA']:,.2f}, \n"
            f"Total Push Notifications: ₦{data['total_push']*70000:,.2f}, \n"
            f"Total Daily Subscribers: {data['total_daily_subscribers']:,.2f}, \n"
            f"Total Annual Subscribers: {data['total_annual_subscribers']:,.2f}, \n"
            f"Total Monthly Subscribers: {data['total_monthly_subscribers']:,.2f} \n"
            f"Revenue from Daily Subscriptions: ₦{data['total_daily_subscribers'] * subscription_rates['daily']:,.2f}, \n"
            f"Revenue from Annual Subscriptions: ₦{data['total_annual_subscribers'] * subscription_rates['annual']:,.2f}, \n"
            f"Revenue from Monthly Subscriptions: ₦{data['total_monthly_subscribers'] * subscription_rates['monthly']:,.2f} \n\n"
        )