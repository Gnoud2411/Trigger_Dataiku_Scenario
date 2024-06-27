# Trigger_Dataiku_Scenario
![Mô tả kiến trúc](docker/dataiku/Architeture.png)

# Running the project
To successfully run this project, follow the steps outlined below

### Prerequisites
If use Window Machine, ensure Docker Destop installed on your system

### Setup and Configuration
1. Clone the repository
```git
git clone https://github.com/Gnoud2411/Trigger_Dataiku_Scenario.git
```

2. Navigate to the project directory
```bash
cd Trigger_Dataiku_Scenario
```
3. Tạo Volume cho Dataiku
```docker
docker volume create dataiku_volume
```
4. Đi vào thư mục ./docker/dataiku và Restore Volume của Dataiku trên máy tính của bạn 
```docker
docker run --rm -v dataiku_volume:/volume -v $(pwd):/backup ubuntu bash -c "cd /volume && tar xzvf /backup/dataiku_volume_backup.tar.gz --strip 1"
```
5. Quay trở lại thư mục ./docker khởi tạo Serivce Airflow-init để kiểm tra và tạo các thiết lập cần thiết ban đầu
```docker
docker compose up airflow-init
```
6. Khởi động tất cả các Services
```docker
docker compose up -d
```

### Output Dashboard
