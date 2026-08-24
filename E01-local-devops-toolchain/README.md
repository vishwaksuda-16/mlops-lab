# Experiment 01 — Local DevOps Toolchain Setup

## Aim

To install and integrate Git, Docker, Java, and Jenkins on a local Ubuntu WSL2 environment, and trigger a Jenkins job that pulls source code from GitHub and executes a Docker container.

## Objective

The experiment demonstrates a basic DevOps toolchain integration:

```text
GitHub Repository
       ↓
Jenkins
       ↓
Git Checkout
       ↓
Execute Shell
       ↓
Docker Container
       ↓
Successful Build
```

It also demonstrates Jenkins source polling using Poll SCM.

---

## Tools and Environment

* **Operating System:** Ubuntu 26.04 LTS
* **Environment:** WSL2
* **Git:** Git 2.53.0
* **Docker:** Docker Desktop with WSL2 integration
* **Java:** OpenJDK 17 and OpenJDK 21
* **Jenkins:** Jenkins LTS
* **Source Control:** GitHub
* **Jenkins Job Type:** Freestyle Project

> Java 17 was installed as specified in the experiment. Java 21 was additionally installed because the current Jenkins version requires a newer Java runtime.

---

# Step-by-Step Procedure

## Step 1 — Verify the WSL Environment

Open the Ubuntu WSL terminal and verify the operating system:

```bash
lsb_release -a
```

Update the package information:

```bash
sudo apt update
sudo apt upgrade -y
```

---

## Step 2 — Verify Git

Check whether Git is installed:

```bash
git --version
```

If Git is not installed:

```bash
sudo apt install git-all -y
```

Configure the Git username and email if required:

```bash
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
```

---

## Step 3 — Configure Docker Desktop with WSL2

Docker Desktop was already installed on Windows.

Enable WSL integration in:

```text
Docker Desktop
→ Settings
→ Resources
→ WSL Integration
```

Enable integration for the Ubuntu WSL distribution and restart Docker Desktop.

Verify Docker from WSL:

```bash
docker --version
```

Test Docker:

```bash
docker run hello-world
```

A successful installation displays:

```text
Hello from Docker!
```

---

## Step 4 — Install Java 17

Install Java 17:

```bash
sudo apt install openjdk-17-jdk -y
```

Verify Java:

```bash
java --version
javac --version
```

Java 17 was installed to satisfy the experiment requirement.

---

## Step 5 — Install Java 21 for Jenkins

The current Jenkins version requires a newer Java runtime. Therefore, Java 21 was also installed without removing Java 17:

```bash
sudo apt install openjdk-21-jdk -y
```

Verify the available Java installations:

```bash
ls /usr/lib/jvm/
```

---

## Step 6 — Install Jenkins LTS

Install the required dependencies:

```bash
sudo apt update
sudo apt install wget fontconfig -y
```

Add the Jenkins repository signing key:

```bash
sudo mkdir -p /etc/apt/keyrings
```

```bash
sudo wget -O /etc/apt/keyrings/jenkins-keyring.asc \
https://pkg.jenkins.io/debian-stable/jenkins.io-2026.key
```

Add the Jenkins LTS repository:

```bash
echo "deb [signed-by=/etc/apt/keyrings/jenkins-keyring.asc] https://pkg.jenkins.io/debian-stable binary/" | \
sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null
```

Update package information:

```bash
sudo apt update
```

Install Jenkins:

```bash
sudo apt install jenkins -y
```

Enable and start Jenkins:

```bash
sudo systemctl enable jenkins
sudo systemctl start jenkins
```

Check the Jenkins service:

```bash
sudo systemctl status jenkins
```

The expected status is:

```text
Active: active (running)
```

---

## Step 7 — Complete Jenkins Initial Setup

Open Jenkins in the Windows browser:

```text
http://localhost:8080/
```

Retrieve the initial administrator password:

```bash
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
```

Complete the setup process:

1. Enter the initial administrator password.
2. Select **Install suggested plugins**.
3. Create a Jenkins administrator account.
4. Set the Jenkins URL to:

```text
http://localhost:8080/
```

5. Complete the Jenkins setup.

---

## Step 8 — Create and Push the GitHub Repository

The lab experiments are stored in a Git repository for future review.

Repository:

```text
mlops-lab
```

The local repository is located in:

```text
~/mlops-lab
```

Initialize Git if required:

```bash
cd ~/mlops-lab
git init
```

Add experiment files:

```bash
git add .
```

Commit the files:

```bash
git commit -m "Initialize Experiment 01"
```

Connect the repository to GitHub using SSH:

```bash
git remote set-url origin git@github.com:vishwaksuda-16/mlops-lab.git
```

Push the repository:

```bash
git push -u origin main
```

For future changes:

```bash
git add .
git commit -m "Description of changes"
git push
```

---

## Step 9 — Configure Jenkins Access to Docker

Jenkins runs as the `jenkins` Linux user, so Docker access must be verified for that user.

Check Docker access:

```bash
sudo -u jenkins docker --version
```

If Docker access is denied, add Jenkins to the Docker group:

```bash
sudo usermod -aG docker jenkins
```

Restart Jenkins:

```bash
sudo systemctl restart jenkins
```

Verify Git access:

```bash
sudo -u jenkins git --version
```

Verify Docker access again:

```bash
sudo -u jenkins docker run hello-world
```

---

## Step 10 — Configure GitHub SSH Credentials in Jenkins

A GitHub SSH key was created and added to the GitHub account.

The Jenkins credential was configured as:

```text
Kind: SSH Username with private key
Username: git
Credential ID: github-ssh
```

The GitHub repository URL used by Jenkins is:

```text
git@github.com:vishwaksuda-16/mlops-lab.git
```

The private SSH key was added only to Jenkins Credentials and was not committed to the Git repository.

---

## Step 11 — Configure GitHub Host Verification

Jenkins required GitHub's host key before cloning the repository.

Create the SSH directory for Jenkins:

```bash
sudo -u jenkins mkdir -p /var/lib/jenkins/.ssh
```

Add GitHub's ED25519 host key:

```bash
sudo -u jenkins ssh-keyscan -t ed25519 github.com | \
sudo -u jenkins tee /var/lib/jenkins/.ssh/known_hosts
```

Set the required permissions:

```bash
sudo chown -R jenkins:jenkins /var/lib/jenkins/.ssh
sudo chmod 700 /var/lib/jenkins/.ssh
sudo chmod 600 /var/lib/jenkins/.ssh/known_hosts
```

This resolves the Jenkins Git error:

```text
Host key verification failed
```

---

## Step 12 — Create the Jenkins Freestyle Project

From the Jenkins dashboard:

```text
New Item
→ Enter Name: E01-Git-Docker-Pipeline
→ Select: Freestyle project
→ OK
```

Under **Source Code Management**:

1. Select **Git**.
2. Enter the repository URL:

```text
git@github.com:vishwaksuda-16/mlops-lab.git
```

3. Select the SSH credential.
4. Configure the branch:

```text
*/main
```

The branch was explicitly set to `main` because Jenkins initially attempted to find the `master` branch and failed.

---

## Step 13 — Configure the Build Step

Under:

```text
Build Steps
→ Add build step
→ Execute shell
```

Add the following script:

```bash
echo "===== E01 DevOps Toolchain Test ====="

echo "Git version:"
git --version

echo "Docker version:"
docker --version

echo "Current directory:"
pwd

echo "Repository files:"
ls -la

echo "Running Docker container:"
docker run --rm hello-world

echo "===== E01 TEST COMPLETED ====="
```

Save the Jenkins job.

---

## Step 14 — Trigger and Verify the Build

From the Jenkins job page:

```text
Build Now
```

Open:

```text
Build History
→ Build Number
→ Console Output
```

Verify that Jenkins:

1. Clones the GitHub repository.
2. Checks out the `main` branch.
3. Executes the shell script.
4. Detects Git.
5. Detects Docker.
6. Runs the Docker container successfully.

The successful build output contains:

```text
+ echo ===== E01 DevOps Toolchain Test =====
===== E01 DevOps Toolchain Test =====
+ echo Git version:
Git version:
+ git --version
git version 2.53.0
+ echo Docker version:
Docker version:
+ docker --version
Docker version 29.5.3, build d1c06ef
+ echo Current directory:
Current directory:
+ pwd
/var/lib/jenkins/workspace/E01-Git-Docker-Pipeline
+ echo Repository files:
Repository files:
+ ls -la
total 16
drwxr-xr-x 4 jenkins jenkins 4096 Aug 19 05:50 .
drwxr-xr-x 4 jenkins jenkins 4096 Aug 19 05:49 ..
drwxr-xr-x 7 jenkins jenkins 4096 Aug 19 05:50 .git
drwxr-xr-x 2 jenkins jenkins 4096 Aug 19 05:50 E01-local-devops-toolchain
+ echo Running Docker container:
Running Docker container:
+ docker run --rm hello-world

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/

+ echo ===== E01 TEST COMPLETED =====
===== E01 TEST COMPLETED =====
Finished: SUCCESS
```

---

## Step 15 — Configure Poll SCM

Open:

```text
E01-Git-Docker-Pipeline
→ Configure
→ Build Triggers
```

Enable:

```text
Poll SCM
```

Set the schedule to:

```text
H/5 * * * *
```

This instructs Jenkins to periodically check the Git repository for changes.

Save the configuration.

---

# Result

The local DevOps toolchain was successfully configured and integrated.

The following components were successfully used:

* Git
* GitHub
* Docker Desktop with WSL2 integration
* Java 17
* Java 21
* Jenkins LTS

A Jenkins Freestyle project successfully cloned the GitHub repository through SSH and executed a Docker container.

The build completed successfully with:

```text
Finished: SUCCESS
```

Poll SCM was also configured using:

```text
H/5 * * * *
```

---

# Final Repository Contents

Only relevant files and final evidence are stored in the repository:

```text
E01-local-devops-toolchain/
├── README.md
└── screenshots/
    ├── 01-jenkins-successful-build.png
    ├── 02-jenkins-git-docker-job-config.png
    └── 03-poll-scm-config.png
```

## Screenshots

Only three final screenshots are required:

1. **Successful Jenkins Build**
   Show the Git checkout, Docker execution, `Hello from Docker!`, and `Finished: SUCCESS`.

2. **Jenkins Job Configuration**
   Show the GitHub repository, SSH credential, `*/main` branch, and the Docker build command.

3. **Poll SCM Configuration**
   Show:

```text
Poll SCM
H/5 * * * *
```

---
