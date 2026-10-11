import paho.mqtt.client as mqtt
import json


BROKER = "broker.emqx.io"   # thu doi neu test.mosquitto.org khong ket noi duoc
PORT = 1883
TOPIC = "iot_lab/sensor01/data"


def on_connect(client, userdata, flags, rc):

    if rc == 0:
        print("Da ket noi MQTT Broker!")

        # Subscribe topic
        client.subscribe(TOPIC)

        print(f"Da subscribe: {TOPIC}")
        print("Dang cho du lieu cam bien...\n")

    else:
        print(f"Ket noi that bai. Ma loi: {rc}")



def on_message(client, userdata, msg):

    try:
        # Chuyển Payload từ bytes -> string
        payload = msg.payload.decode("utf-8")

        # Chuyển JSON -> Python dictionary
        data = json.loads(payload)

        # Lấy dữ liệu
        device_id = data["device_id"]
        temperature = data["temperature"]
        humidity = data["humidity"]

        # In thông tin cảm biến
        print(f"Device: {device_id}")
        print(f"Temperature: {temperature} C")
        print(f"Humidity: {humidity} %")

        # Kiểm tra nhiệt độ
        if temperature > 35:
            print("CANH BAO: Nhiet do cao")

        # Kiểm tra độ ẩm
        if humidity < 40:
            print("CANH BAO: Do am thap")

        print()

    except json.JSONDecodeError:
        print("Loi: Payload khong phai JSON hop le")

    except KeyError as e:
        print(f"Loi: Thieu truong {e}")


client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message


print("Dang ket noi toi MQTT Broker...")

client.connect(BROKER, PORT, 60)



client.loop_forever()