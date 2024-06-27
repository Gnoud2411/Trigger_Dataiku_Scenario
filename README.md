# Trigger_Dataiku_Scenario
![Architectural Description](document/Architeture.png)

Dự án được thiết kế để Demo quá trình tương tác dữ liệu giữa Dataiku và Snowflake, trong đó Dataiku Scenario sẽ được điều phối bởi Airflow

Dataiku Project overview

Project được thiết kế theo logic như sau:
- Bước 1: Tích hợp dữ liệu
+ Dữ liệu từ các file csv được vào tầng Staging - Bảng Raw_Churn_Dataset trong Schema Raw để phục vụ cho bước biến đổi 

- Bước 2: Biến đổi dữ liệu
+ Dữ liệu thô sẽ được khử duplicate, chuẩn hóa các trường dữ liệu

- Bước 3: Load dữ liệu
+ Dữ liệu sau khi được làm sạch sẽ được Incremental Update vào bảng DWH_Churn_Dataset trong Schema Dev của Snowflake
+ Dữ liệu về các bản ghi có số lượng giao dịch bất thường sẽ được gửi Email cảnh báo

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
![Output Dashboard 1](document/Customer_dashboard_1.png)
![Output Dashboard 2](document/Customer_dashboard_2.png)
