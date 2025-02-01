import random
import time
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: v.encode("utf-8"),  # Encode text as bytes
)

topic = "dnd_encounters"

encounters = [
    "COMBAT: A goblin ambushes!",
    "COMBAT: A dragon appears!",
    "LOOT: You find a treasure chest.",
    "LOOT: A magical sword lies in the ruins.",
    "NPC: A mysterious stranger offers a quest.",
    "NPC: A town guard warns you about bandits.",
]

while True:
    encounter = random.choice(encounters)
    producer.send(topic, value=encounter)
    print(f"Sent: {encounter}")
    time.sleep(2)  # Send an encounter every 2 seconds
