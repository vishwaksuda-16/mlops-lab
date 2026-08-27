import pandas as pd
import matplotlib.pyplot as plt


# ==========================================
# 1. Load deployment data
# ==========================================

df = pd.read_csv("deployments.csv")

# Parse deploy_date as datetime
df["deploy_date"] = pd.to_datetime(df["deploy_date"])


# ==========================================
# 2. Deployment Frequency
# ==========================================

# Use deploy_date as index and count deployments per week
weekly_deployments = (
    df.set_index("deploy_date")
      .resample("W")
      .size()
)

average_weekly_frequency = weekly_deployments.mean()


# ==========================================
# 3. Lead Time for Changes
# ==========================================

average_lead_time = df["lead_time_hours"].mean()


# ==========================================
# 4. Change Failure Rate
# ==========================================

change_failure_rate = (
    df["failed"].sum() / len(df)
) * 100


# ==========================================
# 5. Mean Time to Recovery
# ==========================================

failed_deployments = df[df["failed"] == 1]

mttr = failed_deployments["recovery_time_hours"].mean()


# ==========================================
# 6. DORA Elite Thresholds
# ==========================================

# Weekly frequency:
# Elite means multiple deployments per day.
# 7 deployments/week is used as the minimum
# weekly equivalent for this experiment.

elite_frequency = 7

# Elite lead time is less than 1 hour
elite_lead_time = 1

# Elite change failure rate is 0-15%
elite_cfr = 15

# Elite MTTR is less than 1 hour
elite_mttr = 1


# ==========================================
# 7. Determine metric status
# ==========================================

frequency_status = (
    "Elite" if average_weekly_frequency >= elite_frequency
    else "Below Elite"
)

lead_time_status = (
    "Elite" if average_lead_time < elite_lead_time
    else "Below Elite"
)

cfr_status = (
    "Elite" if change_failure_rate <= elite_cfr
    else "Below Elite"
)

mttr_status = (
    "Elite" if mttr < elite_mttr
    else "Below Elite"
)


# ==========================================
# 8. Print Summary Table
# ==========================================

summary = pd.DataFrame({
    "Metric": [
        "Deployment Frequency",
        "Lead Time for Changes",
        "Change Failure Rate",
        "Mean Time to Recovery"
    ],

    "Your Value": [
        f"{average_weekly_frequency:.2f} deployments/week",
        f"{average_lead_time:.2f} hours",
        f"{change_failure_rate:.2f}%",
        f"{mttr:.2f} hours"
    ],

    "Elite Threshold": [
        ">= 7 deployments/week",
        "< 1 hour",
        "<= 15%",
        "< 1 hour"
    ],

    "Status": [
        frequency_status,
        lead_time_status,
        cfr_status,
        mttr_status
    ]
})

print("\n========== DORA METRICS SUMMARY ==========\n")
print(summary.to_string(index=False))


# ==========================================
# 9. Create 2x2 Dashboard
# ==========================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

fig.suptitle(
    "DORA Metrics Dashboard",
    fontsize=18,
    fontweight="bold"
)


# ------------------------------------------
# Chart 1: Deployment Frequency
# ------------------------------------------

frequency_color = (
    "green"
    if frequency_status == "Elite"
    else "red"
)

axes[0, 0].bar(
    weekly_deployments.index.strftime("%Y-%m-%d"),
    weekly_deployments.values,
    color=frequency_color
)

axes[0, 0].axhline(
    elite_frequency,
    linestyle="--",
    label="Elite Threshold"
)

axes[0, 0].set_title(
    f"Deployment Frequency\n"
    f"Average: {average_weekly_frequency:.2f}/week"
)

axes[0, 0].set_xlabel("Week")
axes[0, 0].set_ylabel("Deployments")
axes[0, 0].tick_params(axis="x", rotation=45)
axes[0, 0].legend()


# ------------------------------------------
# Chart 2: Lead Time
# ------------------------------------------

lead_color = (
    "green"
    if lead_time_status == "Elite"
    else "red"
)

axes[0, 1].plot(
    range(1, len(df) + 1),
    df["lead_time_hours"],
    marker="o",
    color=lead_color
)

axes[0, 1].axhline(
    elite_lead_time,
    linestyle="--",
    label="Elite Threshold"
)

axes[0, 1].set_title(
    f"Lead Time for Changes\n"
    f"Average: {average_lead_time:.2f} hours"
)

axes[0, 1].set_xlabel("Deployment")
axes[0, 1].set_ylabel("Lead Time (hours)")
axes[0, 1].legend()


# ------------------------------------------
# Chart 3: Change Failure Rate
# ------------------------------------------

success_count = len(df[df["failed"] == 0])
failure_count = len(df[df["failed"] == 1])

cfr_color = (
    "green"
    if cfr_status == "Elite"
    else "red"
)

axes[1, 0].pie(
    [success_count, failure_count],
    labels=["Successful", "Failed"],
    autopct="%1.1f%%",
    startangle=90
)

axes[1, 0].set_title(
    f"Change Failure Rate\n"
    f"{change_failure_rate:.2f}%"
)


# ------------------------------------------
# Chart 4: MTTR
# ------------------------------------------

mttr_color = (
    "green"
    if mttr_status == "Elite"
    else "red"
)

axes[1, 1].hist(
    failed_deployments["recovery_time_hours"],
    bins=5,
    color=mttr_color
)

axes[1, 1].axvline(
    elite_mttr,
    linestyle="--",
    label="Elite Threshold"
)

axes[1, 1].set_title(
    f"Mean Time to Recovery\n"
    f"Average: {mttr:.2f} hours"
)

axes[1, 1].set_xlabel("Recovery Time (hours)")
axes[1, 1].set_ylabel("Frequency")
axes[1, 1].legend()


# ==========================================
# 10. Final Dashboard Formatting
# ==========================================

plt.tight_layout(rect=[0, 0, 1, 0.95])

plt.savefig(
    "dashboard.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# ==========================================
# 11. Save Summary CSV
# ==========================================

summary.to_csv(
    "dora_summary.csv",
    index=False
)

print("\nDashboard saved as: dashboard.png")
print("Summary saved as: dora_summary.csv")
