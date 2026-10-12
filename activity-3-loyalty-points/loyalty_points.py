"""
Loyalty Points

A coffee shop awards points on every purchase. This program takes a
day's purchases and works out where everybody stands at closing time.
"""

BRONZE_THRESHOLD = 100
SILVER_THRESHOLD = 200
GOLD_THRESHOLD = 250

points = {
    "alice": 120,
    "bob": 40,
    "siobhan": 195
}

purchases = [
    ("alice", 30),
    ("chen", 15),
    ("bob", 60),
    ("alice", 10),
    ("siobhan", 12)
]

tier_counts = {
    "Gold" : 0,
    "Silver" : 0,
    "Bronze" : 0,
    "Standard" : 0
}


def award_points(points, purchases):
    for name, amount in purchases:
        if amount >= 50:
            amount *= 2
        points[name] = points.get(name, 0) + amount


def tier(total):
    if total >= GOLD_THRESHOLD:
        return "Gold"
    elif total >= SILVER_THRESHOLD:
        return "Silver"
    elif total >= BRONZE_THRESHOLD:
        return "Bronze"
    else:
        return "Standard"


print(f"Customers at open: {len(points)}")

award_points(points, purchases)

print(f"Customers at close: {len(points)}")
print("End of day standings:")
for name, total in points.items():
    customer_tier = tier(total)
    print(f"  {name}: {total} points, {customer_tier}")
    tier_counts[customer_tier] += 1

for tier_name, count in tier_counts.items():
    print(f"There are {count} customers in {tier_name}")
