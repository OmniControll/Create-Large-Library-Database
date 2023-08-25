from ics import Calendar, Event
from datetime import datetime, timedelta
import pytz

# Helper function to convert time string to datetime object
def str_to_datetime(date_str, time_str, timezone):
    date_time_str = f"{date_str} {time_str}"
    date_time_format = "%Y-%m-%d %I:%M %p"
    dt = datetime.strptime(date_time_str, date_time_format)
    return timezone.localize(dt)

# Set the date for the schedule
date_str = "2023-04-10"  # Adjust this to the desired date

# Define the timezone
timezone = pytz.timezone("America/New_York")  # Adjust this to your local timezone

schedule = [
    ("5:00 am", "5:05 am", "Wake up"),
    ("5:05 am", "5:10 am", "Hydrate"),
    ("5:10 am", "5:20 am", "Morning mindfulness"),
    ("5:20 am", "5:30 am", "Cold shower"),
    ("5:30 am", "5:40 am", "Get dressed"),
    ("5:40 am", "6:00 am", "Breakfast"),
    ("6:00 am", "6:15 am", "Review goals and plan your day"),
    ("6:15 am", "8:00 am", "Start work on group report"),
    ("8:00 am", "8:15 am", "Break"),
    ("8:15 am", "10:00 am", "Continue work on group report"),
    ("10:00 am", "10:15 am", "Prepare for meeting"),
    ("10:15 am", "10:30 am", "Meeting"),
    ("10:30 am", "11:30 am", "Gym time"),
    ("11:30 am", "12:00 pm", "Post-workout meal"),
    ("12:00 pm", "2:00 pm", "Work on first video"),
    ("2:00 pm", "2:30 pm", "Lunch"),
    ("2:30 pm", "4:30 pm", "Work on second video"),
    ("4:30 pm", "4:45 pm", "Break"),
    ("4:45 pm", "5:30 pm", "Finish work for the day"),
    ("5:30 pm", "6:30 pm", "Dinner"),
    ("6:30 pm", "8:30 pm", "Evening relaxation"),
    ("8:30 pm", "9:00 pm", "Wind down"),
    ("9:00 pm", "9:30 pm", "Prepare for sleep"),
    ("9:30 pm", "5:00 am", "Sleep"),
]

calendar = Calendar()

for start_time_str, end_time_str, activity in schedule:
    start_time = str_to_datetime(date_str, start_time_str, timezone)
    end_time = str_to_datetime(date_str, end_time_str, timezone)

    # If the end time is earlier than the start time, assume the event spans across midnight
    if end_time < start_time:
        end_time += timedelta(days=1)

    event = Event(name=activity, begin=start_time, end=end_time)
    calendar.events.add(event)

# Save the calendar to an ICS file
with open("schedule.ics", "w") as ics_file:
    ics_file.writelines(calendar)
