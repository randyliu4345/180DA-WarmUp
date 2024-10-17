import paho.mqtt.client as mqtt

# Create a new MQTT client
client = mqtt.Client()

# Connect to the broker
client.connect("test.mosquitto.org")

# Publish a message to the "ece180d/test" topic
client.publish("ece180d/test", payload="Hello from publisher!", qos=1)

# Disconnect after publishing
client.disconnect()