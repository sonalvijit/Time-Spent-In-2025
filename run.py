from datetime import datetime

def calculate_time_spent():
    # Get the current date and time
    current_date = datetime.now()
    start_of_year = datetime(current_date.year, 1, 1)
    end_of_year = datetime(current_date.year + 1, 1, 1)

    # Calculate the total elapsed time
    elapsed_time = current_date - start_of_year
    total_year_time = end_of_year - start_of_year

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

    # Calculate percentage of the year passed
    year_percentage = (elapsed_time.total_seconds() / total_year_time.total_seconds()) * 100

    # Return the components
    return {
        "months": total_months,
        "weeks": total_weeks,
        "days": remaining_days,
        "hours": hours,
        "minutes": minutes,
        "seconds": seconds,
        "year_percentage": year_percentage,
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
if result['hours'] > 0:
    output.append(f"{result['hours']} hours")
if result['minutes'] > 0:
    output.append(f"{result['minutes']} minutes")
if result['seconds'] > 0:
    output.append(f"{result['seconds']} seconds")

output.append(f"{result['year_percentage']:.2f}% of the year has passed")

# Create a progress bar
progress_bar_length = 30  # Total length of the progress bar
filled_length = int(progress_bar_length * result['year_percentage'] / 100)
progress_bar = "=" * filled_length + "-" * (progress_bar_length - filled_length)

print("\033[92mTime spent in the new year: \033[00m \033[93m" + ", ".join(output),"\033[00m")
print(f"Progress: [{progress_bar}] {result['year_percentage']:.2f}%")
