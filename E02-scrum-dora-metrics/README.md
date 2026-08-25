# Experiment 02 — Scrum Board & DORA Metrics Mapping

## Aim

To create and manage a Scrum project using Jira, simulate sprint activities, map Scrum practices to DevOps principles, and calculate the four DORA metrics using Python.

---

## Objectives

- Create a Scrum project and manage work using Jira.
- Create an Epic and User Stories with story-point estimates.
- Plan and execute a one-week sprint.
- Simulate daily standups.
- Track completed and carried-forward work.
- Map Scrum activities to DevOps practices.
- Generate deployment data for DORA analysis.
- Calculate the four DORA metrics using Python.
- Generate visualizations using Matplotlib.

---

# 1. Tools and Technologies Used

| Tool | Purpose |
|---|---|
| Jira | Scrum project, backlog, sprint and work tracking |
| Python 3.14.4 | DORA metric calculation |
| Pandas | CSV processing and data analysis |
| Matplotlib | DORA metric visualization |
| Git | Version control |
| GitHub | Remote repository |

---

# 2. Jira Scrum Project

A Jira Scrum project was created with the name:

**DevOps-Lab-Sprint**

Project key:

**DLS**

The project was used to manage the Scrum activities required for this experiment.

---

# 3. Epic

The following Epic was created:

**DevOps Toolchain Setup**

Description:

> Set up and integrate the DevOps toolchain including Git, Docker, Jenkins and CI/CD practices.

---

# 4. User Stories

Five User Stories were created under the Epic.

| Issue | User Story | Story Points |
|---|---|---:|
| DLS-3 | Set up Git repository | 1 |
| DLS-4 | Set up Docker environment | 2 |
| DLS-5 | Configure Jenkins CI | 3 |
| DLS-6 | Create automated build pipeline | 5 |
| DLS-7 | Integrate Git, Jenkins and Docker | 8 |

Total planned effort:

**19 story points**

---

# 5. Sprint Planning

A sprint named:

**Sprint 1 – Week 1**

was created.

All five User Stories were initially assigned to the sprint.

The sprint started with:

- 5 stories
- 19 total story points
- All stories in the To Do state

---

# 6. Daily Standup Simulation

Three daily standups were simulated.

## Day 1

**Yesterday:**  
Sprint planning was completed and Git repository requirements were reviewed.

**Today:**  
Set up Git repository.

**Blockers:**  
None.

The Git repository story was moved from:

`To Do → In Progress → Done`

---

## Day 2

**Yesterday:**  
Git repository setup was completed.

**Today:**  
Configure Docker environment.

**Blockers:**  
None.

The Docker story was moved from:

`To Do → In Progress → Done`

---

## Day 3

**Yesterday:**  
Docker environment configuration was completed.

**Today:**  
Configure Jenkins CI.

**Blockers:**  
None.

The Jenkins story was moved from:

`To Do → In Progress → Done`

---

# 7. Sprint Result

Three stories were completed during Sprint 1.

### Completed

| User Story | Story Points |
|---|---:|
| Set up Git repository | 1 |
| Set up Docker environment | 2 |
| Configure Jenkins CI | 3 |

**Completed:** 6 story points

### Carried Forward

The following two stories were moved to the next-sprint backlog:

| User Story | Story Points |
|---|---:|
| Create automated build pipeline | 5 |
| Integrate Git, Jenkins and Docker | 8 |

**Carried forward:** 13 story points

Original sprint commitment:

**19 story points**

---

# 8. Scrum → DevOps Mapping

| Scrum Activity | What Was Done | DevOps Connection | Reflection |
|---|---|---|---|
| Product Backlog | Created an Epic and five User Stories | Work organization | Breaking work into smaller units makes development easier to track |
| Sprint Planning | Assigned five stories to Sprint 1 | Planning and predictable delivery | Story points helped estimate the amount of work |
| Daily Standup | Simulated three daily standups | Continuous communication | Frequent progress checks help identify problems early |
| Sprint Execution | Moved stories through To Do → In Progress → Done | Continuous flow | Visualizing work helps identify bottlenecks |
| Sprint Completion | Completed three stories and carried two forward | Continuous delivery and feedback | Unfinished work can be prioritized in a future iteration |
| Automation | Connected the Scrum workflow conceptually with Git, Jenkins and Docker | CI/CD automation | Automation reduces manual effort and improves delivery speed |
| Metrics | Calculated the four DORA metrics | Engineering performance measurement | Metrics provide measurable evidence of software delivery performance |

### Reflection

Scrum provides a structured way to plan and manage development work, while DevOps extends this process through automation, continuous integration, continuous delivery, and measurement.

In this experiment, Jira was used to manage work through a sprint, while the Git, Jenkins, and Docker workflow from Experiment 1 demonstrates how development work can be automated. DORA metrics were then used to measure delivery performance.

---

# 9. DORA Metrics

A dataset containing 10 deployment records was created in:

```text
deployment_data.csv
Each record contains:

Deployment ID
Commit date
Deployment date
Deployment status
Recovery time

Example:

deployment_id,commit_date,deployment_date,status,recovery_hours
D001,2026-08-01 09:00,2026-08-01 11:00,Success,0

The dataset contains 10 deployments, including successful and failed deployments.

10. Python Implementation

The DORA metrics were calculated using:

dora_metrics.py

The following Python libraries were used:

import pandas as pd
import matplotlib.pyplot as plt

Run the program using:

python3 dora_metrics.py
11. DORA Metric Calculations
11.1 Deployment Frequency

Deployment Frequency measures how frequently deployments occur.

Formula:

Deployment Frequency =
Number of Deployments / Number of Days

Result:

0.83 deployments/day
11.2 Lead Time for Changes

Lead Time for Changes measures the time between a code change and its deployment.

Formula:

Lead Time =
Deployment Time - Commit Time

The average lead time was calculated across all 10 deployments.

Result:

3.20 hours
11.3 Change Failure Rate

Change Failure Rate measures the percentage of deployments that resulted in failure.

Formula:

Change Failure Rate =
(Failed Deployments / Total Deployments) × 100

There were:

2 failed deployments
10 total deployments

Therefore:

(2 / 10) × 100 = 20%

Result:

20.00%
11.4 Mean Time to Recovery

Mean Time to Recovery (MTTR) measures the average time required to recover from failed deployments.

Formula:

MTTR =
Total Recovery Time / Number of Failed Deployments

The two failed deployments had recovery times of:

2 hours
3 hours

Therefore:

(2 + 3) / 2 = 2.5 hours

Result:

2.50 hours
12. DORA Metrics Results
DORA Metric	Result
Deployment Frequency	0.83 deployments/day
Average Lead Time for Changes	3.20 hours
Change Failure Rate	20.00%
Mean Time to Recovery	2.50 hours

The results were also saved to:

dora_metrics_output.txt
13. Visualizations

Four Matplotlib charts were generated.

Deployment Frequency
charts/deployment_frequency.png
Lead Time for Changes
charts/lead_time.png
Change Failure Rate
charts/change_failure_rate.png
Mean Time to Recovery
charts/mttr.png

All charts were generated automatically by the Python program.

----
