# 2023_무선네트워크 수업

## 라즈베리파이 초기 설정
```
 sudo apt update
 sudo apt upgrade
```
* 한글깨짐
```
sudo apt-get install fonts-unfonts-core -y
sudo apt-get install ibus ibus-hangul -y
```
* GPIO.setmode
```
GPIO.BCM : GPIO 번호
GPIO.BOARD : 핀 번호
```
## InfluxDB 설치
* InfluxDB download key
```
wget -q https://repos.influxdata.com/influxdata-archive_compat.key
echo '393e8779c89ac8d958f81f942f9ad7fb82a25e133faddaf92e15b16e6ac9ce4c influxdata-archive_compat.key' | sha256sum -c && cat influxdata-archive_compat.key | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/influxdata-archive_compat.gpg > /dev/null
echo 'deb [signed-by=/etc/apt/trusted.gpg.d/influxdata-archive_compat.gpg] https://repos.influxdata.com/debian stable main' | sudo tee /etc/apt/sources.list.d/influxdata.list
```
* install influxdb
```
sudo apt-get update && sudo apt-get install influxdb -y
```
* service start, status
```
sudo service influxdb start
sudo service influxdb status
```
