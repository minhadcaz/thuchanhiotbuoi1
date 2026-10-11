import paho.mqtt.client as mqtt
import json

BROKER = "broker.emqx.io"   # thu doi neu test.mosquitto.org khong ket noi duoc
PORT = 1883
CMD_TOPIC = "iot/lab/light01/cmd"
STATUS_TOPIC = "iot/lab/light01/status"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Da ket noi MQTT Broker")
        client.subscribe(STATUS_TOPIC)

def on_message(client, userdata, msg):
    try:
        data = json.loads(msg.payload.decode("utf-8"))

        print("\nTrang thai den:")
        print(f"Device: {data['device_id']}")
        print(f"Status: {data['status']}")
        print()

    except (json.JSONDecodeError, KeyError):
        print("Du lieu trang thai khong hop le")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

print("Dang ket noi MQTT Broker...")
client.connect(BROKER, PORT, 60)

client.loop_start()

while True:
    command = input("Nhap lenh ON/OFF (EXIT de thoat): ").strip().upper()

    if command == "EXIT":
        break

    if command in ["ON", "OFF"]:
        client.publish(CMD_TOPIC, command)
        print(f"Da gui lenh: {command}")
    else:
        print("Lenh khong hop le")

client.loop_stop()
client.disconnect()