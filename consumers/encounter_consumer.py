from kafka import KafkaConsumer

consumer = KafkaConsumer(
    "dnd_encounters",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda x: x.decode("utf-8"),  # Decode bytes to text
)

for message in consumer:
    encounter = message.value

    print(f"🔹 Encounter: {encounter}")

    if event_type == "combat":
        print("⚔️ Prepare for battle!")
    elif event_type == "loot":
        print("💰 Rolling for loot...")
    elif event_type == "npc":
        print("🗣️ What do you do?")
    elif event_type == "world":
        print("🌍 You turn to your compatriots and...")
