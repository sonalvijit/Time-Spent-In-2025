from datetime import datetime

def calculate_time_spent():
    # Get the current date and time
    current_date = datetime.now()
    start_of_year = datetime(current_date.year, 1, 1)

    # Calculate the total elapsed time
    elapsed_time = current_date - start_of_year

    # Convert the elapsed time into components
    total_seconds = elapsed_time.total_seconds()
    total_days = elapsed_time.days
    total_weeks = total_days // 7
    remaining_days = total_days % 7
    total_months = current_date.month - 1

    # Calculate hours, minutes, and seconds
    remaining_seconds = total_seconds - (total_days * 86400)
    hours = int(remaining_seconds // 3600)
    remaining_seconds %= 3600
    minutes = int(remaining_seconds // 60)
    seconds = int(remaining_seconds % 60)

    # Return the components
    return {
        "months": total_months,
        "weeks": total_weeks,
        "days": remaining_days,
        "hours": hours,
        "minutes": minutes,
        "seconds": seconds,
    }

# Automatically get the current date and time
result = calculate_time_spent()

# Display the results in a single line
output = []
if result['months'] > 0:
    output.append(f"{result['months']} months")
if result['weeks'] > 0:
    output.append(f"{result['weeks']} weeks")
if result['days'] > 0:
    output.append(f"{result['days']} days")
output.append(f"{result['hours']} hours")
output.append(f"{result['minutes']} minutes")
output.append(f"{result['seconds']} seconds")

print("Time spent in the new year: " + ", ".join(output))
