import pandas as pd
grades = pd.Series([85, None, 92, 45, None, 78, 55])

missing_values = grades.isnull()
grades_filled = grades.fillna(0)


high_scores = grades_filled[grades_filled > 60]

print("Original Grades Series:")
print(grades)

print("\nMissing Values (True indicates missing):")
print(missing_values)

print("\nGrades after filling missing values with 0:")
print(grades_filled)

print("\nScores greater than 60:")
print(high_scores)
