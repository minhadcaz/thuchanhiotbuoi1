
import paho.mqtt.client as mqtt

BROKER = "broker.emqx.io"   # thu doi neu test.mosquitto.org khong ket noi duoc
PORT = 1883
TOPIC = "iot_lab/message"

HO_TEN = "Tran Nhat Minh"
MA_SV = "B23DCCN565"

# Nội dung thông điệp
message = (
    f"Ho ten: {HO_TEN}\n"
    f"Ma sinh vien: {MA_SV}\n"
    "Noi dung: Xin chao tu client Python MQTT"
)

# Tạo MQTT client
client = mqtt.Client(
    callback_api_version=mqtt.CallbackAPIVersion.VERSION2
)

try:
    # Kết nối tới broker
    client.connect(BROKER, PORT, 60)

    # Bắt đầu vòng lặp xử lý MQTT
    client.loop_start()

    # Gửi thông điệp lên topic
    info = client.publish(TOPIC, message, qos=0)

    # Chờ gửi xong
    info.wait_for_publish()

    print("Da gui message thanh cong!")
    print(f"Topic: {TOPIC}")
    print(f"Payload:\n{message}")

finally:
    client.loop_stop()
    client.disconnect()
