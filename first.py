import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Hours_Studied": [1, 2, 3, 4, 5, 6],
    "Attendance": [50, 55, 65, 70, 85, 90],
    "Marks": [30, 35, 45, 55, 75, 85]
}

df = pd.DataFrame(data)
plt.scatter(df["Hours_Studied"],df["Marks"])
plt.xlabel("Hours_studied")
plt.ylabel("Marks")
plt.title("study hours vs Marks")

print(df)
plt.show()
print("study_hours",df["Hours_Studied"].corr(df["Marks"]))
print("study_hours",df["Attendance"].corr(df["Marks"]))