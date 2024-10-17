import paho.mqtt.client as mqtt

# Callback when the client receives a CONNACK response from the server
def on_connect(client, userdata, flags, rc):
    print("Connection returned result: " + str(rc))
    # Subscribe to the topic
    client.subscribe("ece180d/test", qos=1)

# Callback when the client disconnects
def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected Disconnect")
    else:
        print("Expected Disconnect")

# Callback when a message is received
def on_message(client, userdata, message):
    print("Received message: " + str(message.payload.decode()) + " on topic " + message.topic + " with QoS " + str(message.qos))

# 1. Create a client instance
client = mqtt.Client()

# 2. Add callbacks
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message

# 3. Connect to the broker
client.connect_async("test.mosquitto.org")

# 4. Start the MQTT network loop
client.loop_start()

# Keep the script running to receive messages
try:
    while True:
        pass
except KeyboardInterrupt:
    print("Disconnecting...")
    client.loop_stop()
    client.disconnect()
