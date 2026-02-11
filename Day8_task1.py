import numpy as nt

scores = nt.random.randint(50, 101, size=(5, 3))

mean_scores = scores.mean(axis=0)

centered_scores = scores - mean_scores

print("Original Scores (5 students, 3 subjects):")
print(scores)

print("\nMean Scores of each subject:")
print(mean_scores)

print("\nCentered Scores (After Broadcasting):")
print(centered_scores)
