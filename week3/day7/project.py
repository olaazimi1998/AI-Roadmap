#Finall umpy project

import numpy as np
scores =np.array([
    [85, 90, 78],
    [72, 88, 91],
    [95, 92, 89],
    [60, 75, 70],
    [88, 84, 93]
])
print("Scores:")
print(scores)

print("Shape")
print(scores.shape)

overall_mean = np.mean(scores)
print("Overall mean:", overall_mean)

student_average = np.mean(scores, axis=1)
print("Student average")
print(student_average)

subject_average = np.mean(scores, axis=0)
print("Subject average")
print(subject_average)

highest_score =np.max(scores)
lowest_score = np.min(scores)
print("Highest score:", highest_score)
print("Lowest score:", lowest_score)

passing_score = scores[scores >= 70]
print("best scores")
print(passing_score)

passing_count = np.sum(scores >= 70)
print("NUmber of passing scores:", passing_count)


bonus_score = scores + 5
print("Scores after bonus:")
print(bonus_score)
final_scores = np.clip(scores + 5, 0, 100)
print("Final scores")
print(final_scores)

weights = np.array([
    [0.3],
    [0.3],
    [0.4]
])

weight_scores = scores @ weights
print("Weight scores:")
print(weight_scores)

#Complete project

import numpy as np


# -----------------------------
# 1. Dataset
# -----------------------------

scores = np.array([
    [85, 90, 78],
    [72, 88, 91],
    [95, 92, 89],
    [60, 75, 70],
    [88, 84, 93]
])


# -----------------------------
# 2. Basic information
# -----------------------------

print("Scores:")
print(scores)

print("\nShape:")
print(scores.shape)

print("\nDimensions:")
print(scores.ndim)


# -----------------------------
# 3. Overall statistics
# -----------------------------

print("\nOverall mean:")
print(np.mean(scores))

print("\nHighest score:")
print(np.max(scores))

print("\nLowest score:")
print(np.min(scores))


# -----------------------------
# 4. Student averages
# -----------------------------

student_average = np.mean(scores, axis=1)

print("\nStudent averages:")
print(student_average)


# -----------------------------
# 5. Subject averages
# -----------------------------

subject_average = np.mean(scores, axis=0)

print("\nSubject averages:")
print(subject_average)


# -----------------------------
# 6. Passing scores
# -----------------------------

passing_scores = scores[scores >= 70]

print("\nPassing scores:")
print(passing_scores)


# -----------------------------
# 7. Add bonus
# -----------------------------

final_scores = np.clip(scores + 5, 0, 100)

print("\nScores after bonus:")
print(final_scores)


# -----------------------------
# 8. Weighted score
# -----------------------------

weights = np.array([
    [0.3],
    [0.3],
    [0.4]
])

weighted_scores = scores @ weights

print("\nWeighted scores:")
print(weighted_scores)

print(np.zeros(4))

































