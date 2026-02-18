# Given probabilities
P_spam = 0.1
P_ham = 0.9

P_free_given_spam = 0.9
P_free_given_ham = 0.05

# Total Probability of "Free"
P_free = (P_free_given_spam * P_spam) + (P_free_given_ham * P_ham)

# Apply Bayes' Theorem
P_spam_given_free = (P_free_given_spam * P_spam) / P_free

print("Total Probability of 'Free':", P_free)
print("Probability email is Spam given it contains 'Free':", P_spam_given_free)