import random
import statistics as st

def generate_grades(count):
    rates = []
    for i in range(0, count):
        rates.append(random.randint(1,12))
    return rates

def average_grade(grades):
    return round(st.mean(grades), 1)

def get_level(average):
    if average >= 10 and average <= 12:
        return "good"
    if average >= 7 and average < 10:
        return "enough"
    if average >= 4 and average < 7:
        return "middle"
    else:
        return "beginner"