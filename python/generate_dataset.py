import pandas as pd
import random
from faker import Faker

# Indian Fake Data
fake = Faker("en_IN")

# Products
products = [
    ("Gold Ring", "Gold"),
    ("Gold Chain", "Gold"),
    ("Gold Earrings", "Gold"),
    ("Gold Necklace", "Gold"),
    ("Silver Ring", "Silver"),
    ("Silver Payal", "Silver"),
    ("Silver Chain", "Silver"),
    ("Silver Coin", "Silver")
]

# Payment Modes
payment_modes = [
    "Cash",
    "UPI",
    "Card",
    "Bank Transfer"
]

# Branches
branches = [
    "Jhansi",
    "Kanpur",
    "Lucknow"
]

# Cities
cities = [
    "Jhansi",
    "Kanpur",
    "Lucknow",
    "Delhi",
    "Gwalior"
]

# Salespersons
salespersons = [
    "Amit",
    "Rahul",
    "Priya",
    "Neha",
    "Rohit",
    "Ankit",
    "Pooja"
]

# Festivals
festivals = [
    "Normal",
    "Diwali",
    "Akshaya Tritiya",
    "Wedding Season",
    "Dhanteras"
]

# Gender
genders = [
    "Male",
    "Female"
]

# Store Records
records = []

# Generate 20,000 Records
for i in range(1, 20001):

    product, metal = random.choice(products)

    bill_no = f"B{1000+i}"

    customer_name = fake.name()

    sale_date = fake.date_between(start_date="-2y", end_date="today")

    payment_mode = random.choice(payment_modes)

    branch = random.choice(branches)

    city = random.choice(cities)

    salesperson = random.choice(salespersons)

    festival = random.choice(festivals)

    customer_gender = random.choice(genders)

    customer_age = random.randint(18, 70)

    quantity = random.randint(1, 5)

    discount = random.randint(0, 15)

    # Gold / Silver Details
    if metal == "Gold":
        weight = round(random.uniform(2, 20), 2)
        rate = random.randint(5800, 7200)
        making_charge = random.randint(1000, 5000)
    else:
        weight = round(random.uniform(10, 100), 2)
        rate = random.randint(70, 120)
        making_charge = random.randint(100, 1000)

    # Price Calculations
    selling_price = (weight * rate) + making_charge

    cost_price = selling_price * random.uniform(0.82, 0.92)

    discount_amount = selling_price * (discount / 100)

    subtotal = (selling_price - discount_amount) * quantity

    gst = round(subtotal * 0.03, 2)

    total_amount = round(subtotal + gst, 2)

    profit = round((selling_price - cost_price) * quantity, 2)

    cost_price = round(cost_price, 2)

    selling_price = round(selling_price, 2)

    # Add Record
    records.append([
        bill_no,
        sale_date,
        customer_name,
        customer_gender,
        customer_age,
        city,
        branch,
        salesperson,
        product,
        metal,
        quantity,
        weight,
        rate,
        cost_price,
        selling_price,
        discount,
        making_charge,
        gst,
        profit,
        total_amount,
        payment_mode,
        festival
    ])

# Column Names
columns = [
    "bill_no",
    "sale_date",
    "customer_name",
    "customer_gender",
    "customer_age",
    "city",
    "branch",
    "salesperson",
    "product_name",
    "metal",
    "quantity",
    "weight_gm",
    "rate_per_gm",
    "cost_price",
    "selling_price",
    "discount_percent",
    "making_charge",
    "gst",
    "profit",
    "total_amount",
    "payment_mode",
    "festival"
]

# Create DataFrame
df = pd.DataFrame(records, columns=columns)

# Save CSV
df.to_csv("../dataset/sales_data.csv", index=False)

# Print Output
print("✅ 20,000 Records Generated Successfully!")
print(df.head())
print("\nTotal Records:", len(df))