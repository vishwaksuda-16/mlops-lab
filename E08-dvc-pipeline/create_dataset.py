import pandas as pd

data = {
    "hours_studied": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                      2, 3, 5, 7, 8, 9, 4, 6, 10, 1],
    "attendance": [55, 60, 65, 70, 75, 80, 85, 90, 95, 98,
                   62, 68, 78, 88, 92, 96, 72, 82, 99, 50],
    "assignments_completed": [1, 2, 2, 3, 4, 5, 6, 7, 8, 9,
                              2, 3, 4, 6, 7, 8, 3, 5, 9, 1],
    "passed": [0, 0, 0, 0, 1, 1, 1, 1, 1, 1,
               0, 0, 1, 1, 1, 1, 0, 1, 1, 0]
}

df = pd.DataFrame(data)

df.to_csv("data.csv", index=False)

print("Dataset created successfully!")
print(df)
