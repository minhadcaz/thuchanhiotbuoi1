# thuchanhiotbuoi1
README - MQTT IoT Lab

1. Broker su dung
- MQTT broker cong khai: "broker.emqx.io" 
- Port: 1883
- Thu vien Python: paho-mqtt
- Cai dat thu vien:
  pip install paho-mqtt

2. Cach chay
Mo moi chuong trinh trong mot terminal rieng. Chay subscriber/device truoc,
then chay publisher/controller.

Bai 1 - Gui nhan message:
- Terminal 1:
  cd message
  python subcriber_bai1.py
- Terminal 2:
  cd message
  python publisher_bai1.py
- Topic: iot/lab/message

Bai 2 - Cam bien nhiet do va do am:
- Terminal 1:
  cd sensor01/data
  python moniter_subcriber_bai2.py
- Terminal 2:
  cd sensor01/data
  python sensor_publisher_bai2.py
- Topic: iot_lab/sensor01/data
- Dung publisher bang Ctrl+C.

Bai 3 - Dieu khien den:
- Terminal 1:
  cd light01/cmd
  python device_bai3.py
- Terminal 2:
  cd light01/controller.py
  python controller_bai3.py
- Nhap ON hoac OFF de dieu khien den; nhap EXIT de thoat controller.
- Topic lenh: iot/lab/light01/cmd
- Topic trang thai: iot/lab/light01/status

3. Ket qua dat duoc
- Bai 1: Publisher gui thanh cong thong tin nguoi dung; Subscriber nhan va
  hien thi message cung thoi gian nhan.
  '''
   @mint  python publisher_bai1.py
        Da gui message thanh cong!
        Topic: iot_lab/message
        Payload:
        Ho ten: Tran Nhat Minh
        Ma sinh vien: B23DCCN565
        Noi dung: Xin chao tu client Python MQTT
  '''
   @mint  python subscriber_bai1.py
        Dang cho message...
        Da ket noi MQTT broker!
        Nhan duoc message:
        Topic: iot_lab/message
        Payload:
        Ho ten: Tran Nhat Minh
        Ma sinh vien: B23DCCN565
        Noi dung: Xin chao tu client Python MQTT
        Time: 22:21:06
  '''
- Bai 2: Sensor publisher tao nhiet do 25-40 C va do am 30-80%, gui moi 3
  giay. Subscriber hien thi du lieu va canh bao khi nhiet do > 35 C hoac do am
  < 40%.
- Bai 3: Controller gui lenh ON/OFF den device. Device cap nhat trang thai
  den va gui phan hoi ve controller.
