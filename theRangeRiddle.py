# Task 1: Your Mood Today:
import random
moods =["Happy", "Sad", "Energetic", "Calm"]
dayOfTheWeek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Staturday", "Sunday"]
for i in range(len(dayOfTheWeek)):
  mood = random.choice( moods )
  print(f"On {dayOfTheWeek[i]}, you were feeling {mood}.")