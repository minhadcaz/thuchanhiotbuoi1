import paho.mqtt.client as mqtt
import json
import random
import time


BROKER = "broker.emqx.io"   # thu doi neu test.mosquitto.org khong ket noi duoc
PORT = 1883
TOPIC = "iot_lab/sensor01/data"

# Tạo MQTT client
client = mqtt.Client()

print("Dang ket noi toi MQTT Broker...")

client.connect(BROKER, PORT, 60)

print("Da ket noi MQTT Broker!")
print("Bat dau gui du lieu cam bien...\n")


try:
    while True:

        # Sinh nhiệt độ ngẫu nhiên: 25 -> 40 độ C
        temperature = round(random.uniform(25, 40), 1)

        # Sinh độ ẩm ngẫu nhiên: 30 -> 80 %
        humidity = round(random.uniform(30, 80), 1)

        # Tạo dữ liệu sensor
        data = {
            "device_id": "sensor01",
            "temperature": temperature,
            "humidity": humidity
        }

        # Chuyển dictionary thành JSON
        payload = json.dumps(data)

        # Gửi dữ liệu lên MQTT
        client.publish(TOPIC, payload)

        print("Da gui:")
        print(payload)
        print()

        # Chờ 3 giây
        time.sleep(3)

except KeyboardInterrupt:
    print("\nDung Sensor Publisher.")

finally:
    client.disconnect()
    print("Da ngat ket noi MQTT Broker.")