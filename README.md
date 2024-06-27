# Trigger_Dataiku_Scenario
![Architectural Description](document/Architeture.png)

---
# Running the project
To successfully run this project, follow the steps outlined below

### Prerequisites
If you are using Linux or MacOS, please install Docker and Docker Compose. If you are using Windows, please install Docker Desktop

### Setup and Configuration
1. Clone the repository
```git
git clone https://github.com/Gnoud2411/Trigger_Dataiku_Scenario.git
```

2. Navigate to the project directory
```bash
cd Trigger_Dataiku_Scenario
```
3. Create Volume for Dataiku Service
```docker
docker volume create dataiku_volume
```
4. Navigate to ./docker/dataiku Folder and Restore Volume of Dataiku service on your machine
```docker
docker run --rm -v dataiku_volume:/volume -v $(pwd):/backup ubuntu bash -c "cd /volume && tar xzvf /backup/dataiku_volume_backup.tar.gz --strip 1"
```
5. Return to the ./docker directory and initialize the Airflow-init Service to check and create the necessary initial settings
```docker
docker compose up airflow-init
```
6. Start all Services
```docker
docker compose up -d
```

### Output Dashboard
