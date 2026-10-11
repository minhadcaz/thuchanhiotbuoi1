
import paho.mqtt.client as mqtt
from datetime import datetime

BROKER = "broker.emqx.io"   # thu doi neu test.mosquitto.org khong ket noi duoc
PORT = 1883
TOPIC = "iot_lab/message"


# Callback khi kết nối thành công
def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code.is_failure:
        print("Ket noi MQTT that bai!")
        return

    print("Da ket noi MQTT broker!")
    client.subscribe(TOPIC)


# Callback khi nhận được message
def on_message(client, userdata, msg):
    payload = msg.payload.decode("utf-8", errors="replace")
    received_time = datetime.now().strftime("%H:%M:%S")

    print("\nNhan duoc message:")
    print(f"Topic: {msg.topic}")
    print(f"Payload:\n{payload}")
    print(f"Time: {received_time}")
    print("-" * 40)


# Tạo MQTT client
client = mqtt.Client(
    callback_api_version=mqtt.CallbackAPIVersion.VERSION2
)

# Đăng ký callback
client.on_connect = on_connect
client.on_message = on_message

try:
    # Kết nối tới broker
    client.connect(BROKER, PORT, 60)

    print("Dang cho message...")
    # Duy trì kết nối và lắng nghe liên tục
    client.loop_forever()

except KeyboardInterrupt:
    print("\nDang ngat ket noi...")

finally:
    client.disconnect()
