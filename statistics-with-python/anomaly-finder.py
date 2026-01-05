import numpy as np

# 1. Create a list of normal numbers (around 50)
data = np.array([52, 48, 49, 51, 50, 48, 52, 200, 49, 51])
# Note the '200' hiding in there!

# 2. Calculate the Mean and Standard Deviation
mean = np.mean(data)
std_dev = np.std(data)

# 3. Calculate Z-Scores for EVERY number at once
z_scores = (data - mean) / std_dev

print("Z-Scores:", z_scores)

#here is how a noob would check the outliers:
print("Noob type: ")
for z_score in z_scores:
    if(z_score >= 2.8 or z_score <= -2.8):
        print(f"Outlier found: {z_score}")

#here is how a pro would check the outliers
print("Pro type")
outliers = data[z_scores > 2.8]
print(f"Outliers: {outliers}")