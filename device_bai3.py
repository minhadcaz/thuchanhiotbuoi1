import paho.mqtt.client as mqtt
import json

BROKER = "broker.emqx.io"   # thu doi neu test.mosquitto.org khong ket noi duoc
PORT = 1883
CMD_TOPIC = "iot/lab/light01/cmd"
STATUS_TOPIC = "iot/lab/light01/status"

status = "OFF"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Da ket noi MQTT Broker")
        client.subscribe(CMD_TOPIC)

def on_message(client, userdata, msg):
    global status

    command = msg.payload.decode("utf-8").strip().upper()

    if command == "ON":
        status = "ON"
    elif command == "OFF":
        status = "OFF"
    else:
        return

    data = {
        "device_id": "light01",
        "status": status
    }

    client.publish(STATUS_TOPIC, json.dumps(data))
    print(f"Den da chuyen sang: {status}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

print("Dang ket noi MQTT Broker...")
client.connect(BROKER, PORT, 60)

client.loop_forever()