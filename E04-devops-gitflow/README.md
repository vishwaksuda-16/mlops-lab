# Experiment 04 — Full GitFlow Implementation

## Aim

To implement a complete GitFlow workflow using Git, including feature development, merge conflict resolution, release management, version tagging, and hotfix handling.

---

## Objectives

- Initialize a Git repository using GitFlow.
- Create and manage `main` and `develop` branches.
- Create a feature branch.
- Develop and commit a user authentication feature.
- Demonstrate and resolve a merge conflict.
- Create and finish a release branch.
- Create a release tag.
- Create and finish a hotfix branch.
- Create a hotfix version tag.
- Push the final branches and tags to GitHub.
- Understand how GitFlow supports structured software development.

---

## Tools Used

| Tool | Purpose |
|---|---|
| Git | Version control |
| GitFlow | Branching workflow |
| GitHub | Remote repository |
| WSL Ubuntu | Local development environment |
| Python | Testing `auth.py` |

---

# 1. Repository Initialization

A separate working directory was initially created for the GitFlow experiment:

```text
devops-gitflow
Git was initialized using:

git init

The production branch was configured as:

main

GitFlow was then initialized:

git flow init

The following branch configuration was used:

Production branch: main
Development branch: develop

Feature prefix: feature/
Release prefix: release/
Hotfix prefix: hotfix/
Bugfix prefix: bugfix/
Support prefix: support/

The initial branch structure was:

main
develop
2. Feature Development

A feature branch was created using:

git flow feature start user-auth

This created:

feature/user-auth

The file auth.py was created to implement a basic login function.

The feature was committed using:

git add auth.py
git commit -m "feat: add user authentication"

The feature was completed using:

git flow feature finish user-auth

This merged the feature into:

develop
3. Merge Conflict Demonstration

A second feature branch was created:

git flow feature start login-validation

The login success message in auth.py was modified and committed.

The develop branch was then modified independently on the same line.

When the feature was merged:

git merge feature/login-validation

Git produced a merge conflict because the same line had been modified differently in both branches.

The conflict was manually resolved in auth.py.

The resolved file was committed using:

git add auth.py
git commit -m "fix: resolve login validation merge conflict"

This demonstrated how Git handles conflicting changes from different development branches.

4. Release Management

A release branch was created:

git flow release start 1.0

The release version was recorded in:

version.txt

with the content:

1.0

The change was committed:

git add version.txt
git commit -m "chore: prepare release 1.0"

The release was then merged into main.

The release was tagged:

git tag -a v1.0 -m "Release version 1.0"

The resulting release tag was:

v1.0
5. Hotfix

A hotfix branch was created from main:

git flow hotfix start login-bug

The authentication code in auth.py was modified to handle whitespace in the username.

The fix changed the username validation to:

if username.strip() == "admin" and password == "admin123":

The hotfix was committed:

git add auth.py
git commit -m "fix: resolve login username validation bug"

The hotfix was merged into both main and develop.

A patch version tag was created:

git tag -a v1.0.1 -m "Hotfix login bug"

The final hotfix tag was:

v1.0.1
6. Final Branch Structure

The temporary feature, release, and hotfix branches were removed after merging.

The final local branch structure was:

develop
main

The final tags were:

v1.0
v1.0.1
7. Git History

The Git history demonstrates the complete workflow:

main
 |
 |--- v1.0
 |       |
 |       └── release/1.0
 |
 |--- v1.0.1
         |
         └── hotfix/login-bug

The development history also contains:

feature/user-auth
feature/login-validation

and the deliberate merge conflict and its resolution.

The final history can be viewed using:

git log --oneline --decorate --graph --all
8. Important GitFlow Commands Used
Initialize GitFlow
git flow init
Start a feature
git flow feature start user-auth
Finish a feature
git flow feature finish user-auth
Start a release
git flow release start 1.0
Finish a release
git flow release finish 1.0
Start a hotfix
git flow hotfix start login-bug
Finish a hotfix
git flow hotfix finish login-bug
Create annotated tags
git tag -a v1.0 -m "Release version 1.0"
git tag -a v1.0.1 -m "Hotfix login bug"
View branches
git branch
View tags
git tag
View complete history
git log --oneline --decorate --graph --all
9. GitFlow Workflow

The workflow implemented in this experiment was:

                    ┌── feature/user-auth
                    │
develop ────────────┤
                    │
                    └── feature/login-validation
                              │
                              ↓
                       Merge Conflict
                              │
                              ↓
                           develop
                              │
                              ↓
                         release/1.0
                              │
                              ↓
                           main
                              │
                            v1.0
                              │
                              ↓
                       hotfix/login-bug
                              │
                              ↓
                     main + develop
                              │
                           v1.0.1
10. Final Files

The experiment files stored in this directory are:

E04-devops-gitflow/
├── README.md
├── auth.py
└── version.txt
11. Result

The GitFlow workflow was successfully implemented.

The experiment demonstrated:

Git repository initialization
GitFlow configuration
Feature branch development
Feature merging
Merge conflict creation and resolution
Release branch management
Release tagging
Hotfix branch management
Hotfix merging
Version tagging
Branch and history management

The final repository contains:

Branches:
main
develop

Tags:
v1.0
v1.0.1
