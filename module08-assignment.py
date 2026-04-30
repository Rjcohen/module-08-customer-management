# Module 8 Assignment

print("=" * 60)
print("GLOBALTECH SOLUTIONS - CUSTOMER MANAGEMENT SYSTEM")
print("=" * 60)

# TODO 1
services = {
    "Web Development": 150,
    "Data Analysis": 175,
    "Cybersecurity": 220,
    "Cloud Services": 200,
    "IT Support": 90
}

# TODO 2
customer1 = {"company_name": "TechCorp", "contact_person": "Alice Smith", "email": "alice@techcorp.com", "phone": "111-222-3333"}
customer2 = {"company_name": "DataWorks", "contact_person": "Bob Jones", "email": "bob@dataworks.com", "phone": "222-333-4444"}
customer3 = {"company_name": "SecureIT", "contact_person": "Charlie Brown", "email": "charlie@secureit.com", "phone": "333-444-5555"}
customer4 = {"company_name": "CloudNet", "contact_person": "Diana Prince", "email": "diana@cloudnet.com", "phone": "444-555-6666"}

# TODO 3
customers = {
    "C001": customer1,
    "C002": customer2,
    "C003": customer3,
    "C004": customer4
}

# TODO 4
print("\nAll Customers:")
print("-" * 60)
for cid, info in customers.items():
    print(cid, ":", info)

# TODO 5
print("\n\nCustomer Lookups:")
print("-" * 60)
c002_info = customers["C002"]
print("C002:", c002_info)

c003_contact = customers["C003"]["contact_person"]
print("C003 Contact:", c003_contact)

c999_info = customers.get("C999", "Customer not found")
print("C999:", c999_info)

# TODO 6
print("\n\nUpdating Customer Information:")
print("-" * 60)
customers["C001"]["phone"] = "999-999-9999"
customers["C002"]["industry"] = "Technology"
print(customers["C001"])
print(customers["C002"])

# TODO 7
project1 = {"name": "Website Revamp", "service": "Web Development", "hours": 100, "budget": 15000}
project2 = {"name": "Data Audit", "service": "Data Analysis", "hours": 80, "budget": 14000}
project3 = {"name": "Security Upgrade", "service": "Cybersecurity", "hours": 60, "budget": 13000}
project4 = {"name": "Cloud Migration", "service": "Cloud Services", "hours": 120, "budget": 24000}

projects = {
    "C001": [project1],
    "C002": [project2],
    "C003": [project3],
    "C004": [project4]
}

print("\n\nProject Information:")
print("-" * 60)
print(projects)

# TODO 8
print("\n\nProject Cost Calculations:")
print("-" * 60)
for cid, plist in projects.items():
    for p in plist:
        rate = services[p["service"]]
        cost = rate * p["hours"]
        print(p["name"], "Cost:", cost)

# TODO 9
print("\n\nCustomer Statistics:")
print("-" * 60)
print("IDs:", customers.keys())
print("Companies:", [c["company_name"] for c in customers.values()])
print("Total Customers:", len(customers))

# TODO 10
print("\n\nService Usage Analysis:")
print("-" * 60)
service_counts = {}
for plist in projects.values():
    for p in plist:
        s = p["service"]
        service_counts[s] = service_counts.get(s, 0) + 1
print(service_counts)

# TODO 11
print("\n\nFinancial Summary:")
print("-" * 60)
all_projects = [p for plist in projects.values() for p in plist]

total_hours = sum(p["hours"] for p in all_projects)
total_budget = sum(p["budget"] for p in all_projects)
avg_budget = total_budget / len(all_projects)
max_budget = max(p["budget"] for p in all_projects)
min_budget = min(p["budget"] for p in all_projects)

print(total_hours, total_budget, avg_budget, max_budget, min_budget)

# TODO 12
print("\n\nCustomer Summary Report:")
print("-" * 60)
for cid, plist in projects.items():
    total_h = sum(p["hours"] for p in plist)
    total_b = sum(p["budget"] for p in plist)
    print(cid, customers[cid]["company_name"], len(plist), total_h, total_b)

# TODO 13
print("\n\nAdjusted Service Rates (10% increase):")
print("-" * 60)
adjusted_rates = {s: r * 1.1 for s, r in services.items()}
print(adjusted_rates)

# TODO 14
print("\n\nActive Customers (with projects):")
print("-" * 60)
active_customers = {cid: customers[cid] for cid in projects if len(projects[cid]) > 0}
print(active_customers)

# TODO 15
print("\n\nCustomer Budget Totals:")
print("-" * 60)
customer_budgets = {cid: sum(p["budget"] for p in plist) for cid, plist in projects.items()}
print(customer_budgets)

# TODO 16
print("\n\nService Pricing Tiers:")
print("-" * 60)
service_tiers = {
    s: "Premium" if r >= 200 else "Standard" if r >= 100 else "Basic"
    for s, r in services.items()
}
print(service_tiers)

# TODO 17
print("\n\nCustomer Validation:")
print("-" * 60)
def validate_customer(c):
    required = ["company_name", "contact_person", "email", "phone"]
    return all(k in c for k in required)

for cid, c in customers.items():
    print(cid, validate_customer(c))

# TODO 18
print("\n\nProject Status Summary:")
print("-" * 60)

status_counts = {
    "active": 0,
    "completed": 0,
    "pending": 0
}

status_list = ["active", "completed", "pending", "active"]

index = 0
for plist in projects.values():
    for p in plist:
        p["status"] = status_list[index]
        status_counts[p["status"]] += 1
        index += 1

print(status_counts)


# TODO 19
print("\n\nDetailed Budget Analysis:")
print("-" * 60)
def analyze_customer_budgets(projects_dict):
    result = {}
    for cid, plist in projects_dict.items():
        total = sum(p["budget"] for p in plist)
        count = len(plist)
        avg = total / count
        result[cid] = {"total": total, "average": avg, "count": count}
    return result

print(analyze_customer_budgets(projects))

# TODO 20
print("\n\nService Recommendations:")
print("-" * 60)
def recommend_services(customer_id, customers, projects, services):
    used = [p["service"] for p in projects.get(customer_id, [])]
    return [s for s in services if s not in used]

print(recommend_services("C001", customers, projects, services))