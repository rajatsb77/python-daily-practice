# Employee Attendance Analyzer
# Today's Python Practice

employees = [
    {"name": "Ravi", "department": "IT", "days_present": 22, "working_days": 24},
    {"name": "Priya", "department": "HR", "days_present": 20, "working_days": 24},
    {"name": "Aman", "department": "IT", "days_present": 23, "working_days": 24},
    {"name": "Neha", "department": "Finance", "days_present": 18, "working_days": 24},
    {"name": "Arjun", "department": "IT", "days_present": 21, "working_days": 24},
]


def calculate_attendance_percentage(days_present, working_days):
    return (days_present / working_days) * 100


def get_attendance_status(percentage):
    if percentage >= 90:
        return "Excellent"
    elif percentage >= 75:
        return "Good"
    else:
        return "Low"


# Analyze employees
for employee in employees:
    percentage = calculate_attendance_percentage(
        employee["days_present"],
        employee["working_days"]
    )

    status = get_attendance_status(percentage)

    print(
        f"{employee['name']:10} | "
        f"{employee['department']:10} | "
        f"Attendance: {percentage:.2f}% | "
        f"Status: {status}"
    )


# Find employees with low attendance
low_attendance = []

for employee in employees:
    percentage = calculate_attendance_percentage(
        employee["days_present"],
        employee["working_days"]
    )

    if percentage < 75:
        low_attendance.append(employee["name"])


print("\nEmployees with low attendance:")

if low_attendance:
    for name in low_attendance:
        print("-", name)
else:
    print("None")