import pandas as pd
import matplotlib.pyplot as plt

# Load deployment data
df = pd.read_csv("deployment_data.csv")

# Convert date columns
df["commit_date"] = pd.to_datetime(df["commit_date"])
df["deployment_date"] = pd.to_datetime(df["deployment_date"])

# -----------------------------------
# 1. Deployment Frequency
# -----------------------------------

total_days = (
    df["deployment_date"].max() - df["deployment_date"].min()
).days + 1

deployment_frequency = len(df) / total_days


# -----------------------------------
# 2. Lead Time for Changes
# -----------------------------------

df["lead_time_hours"] = (
    df["deployment_date"] - df["commit_date"]
).dt.total_seconds() / 3600

average_lead_time = df["lead_time_hours"].mean()


# -----------------------------------
# 3. Change Failure Rate
# -----------------------------------

failed_deployments = len(
    df[df["status"] == "Failure"]
)

change_failure_rate = (
    failed_deployments / len(df)
) * 100


# -----------------------------------
# 4. Mean Time to Recovery
# -----------------------------------

failed_df = df[df["status"] == "Failure"]

mttr = failed_df["recovery_hours"].mean()


# -----------------------------------
# Display results
# -----------------------------------

print("===== DORA METRICS =====")

print(f"Deployment Frequency: {deployment_frequency:.2f} deployments/day")

print(f"Average Lead Time for Changes: {average_lead_time:.2f} hours")

print(f"Change Failure Rate: {change_failure_rate:.2f}%")

print(f"Mean Time to Recovery: {mttr:.2f} hours")


# -----------------------------------
# Save results
# -----------------------------------

with open("dora_metrics_output.txt", "w") as file:
    file.write("===== DORA METRICS =====\n")
    file.write(
        f"Deployment Frequency: {deployment_frequency:.2f} deployments/day\n"
    )
    file.write(
        f"Average Lead Time for Changes: {average_lead_time:.2f} hours\n"
    )
    file.write(
        f"Change Failure Rate: {change_failure_rate:.2f}%\n"
    )
    file.write(
        f"Mean Time to Recovery: {mttr:.2f} hours\n"
    )


# -----------------------------------
# Chart 1: Deployment Frequency
# -----------------------------------

plt.figure()
plt.bar(["Deployments"], [len(df)])
plt.ylabel("Number of Deployments")
plt.title("Deployment Frequency")
plt.savefig("charts/deployment_frequency.png")
plt.close()


# -----------------------------------
# Chart 2: Lead Time
# -----------------------------------

plt.figure()
plt.plot(
    range(1, len(df) + 1),
    df["lead_time_hours"],
    marker="o"
)
plt.xlabel("Deployment")
plt.ylabel("Lead Time (hours)")
plt.title("Lead Time for Changes")
plt.savefig("charts/lead_time.png")
plt.close()


# -----------------------------------
# Chart 3: Change Failure Rate
# -----------------------------------

success_count = len(df[df["status"] == "Success"])
failure_count = len(df[df["status"] == "Failure"])

plt.figure()
plt.bar(
    ["Success", "Failure"],
    [success_count, failure_count]
)
plt.ylabel("Number of Deployments")
plt.title("Change Failure Rate")
plt.savefig("charts/change_failure_rate.png")
plt.close()


# -----------------------------------
# Chart 4: MTTR
# -----------------------------------

plt.figure()
plt.bar(
    ["Failed Deployment 1", "Failed Deployment 2"],
    failed_df["recovery_hours"]
)
plt.ylabel("Recovery Time (hours)")
plt.title("Mean Time to Recovery")
plt.savefig("charts/mttr.png")
plt.close()

print("\nCharts saved in charts/")
