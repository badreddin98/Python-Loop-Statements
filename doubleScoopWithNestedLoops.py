# Task 1: Your Mood Tracker:
import random
moods =["Happy", "Sad", "Energetic", "Calm"]
timesOfTheDay = ["morning", "afternoon", "evening"]
dayOfTheWeek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Staturday", "Sunday"]
for day in dayOfTheWeek:
  for time in timesOfTheDay:
    mood = random.choice(moods)
    print(f"On {day} {time} you were {mood}.")