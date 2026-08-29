import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("data.csv")

train, test = train_test_split(
    df,
    test_size=0.2,
    random_state=42,
    stratify=df["passed"]
)

train.to_csv("train.csv", index=False)
test.to_csv("test.csv", index=False)

print("Data preparation completed.")
print(f"Training samples: {len(train)}")
print(f"Testing samples: {len(test)}")
