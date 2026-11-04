import pandas as pd

data = {
    "Hours_Studied": [1, 2, 3, 4, 5, 6],
    "Attendance": [50, 55, 65, 70, 85, 90],
    "Marks": [30, 35, 45, 55, 75, 85]
}

df = pd.DataFrame(data)

print(df)