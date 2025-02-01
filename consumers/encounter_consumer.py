from kafka import KafkaConsumer

consumer = KafkaConsumer(
    "dnd_encounters",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda x: x.decode("utf-8"),  # Decode bytes to text
)

for message in consumer:
    encounter = message.value

    print(f"🔹 Encounter: {encounter}")

    if "COMBAT" in encounter:
        print("⚔️ Prepare for battle! Roll for initiative!")
    elif "LOOT" in encounter:
        print("💰 Have you ever seen such treasure?")
    elif "NPC" in encounter:
        print("🗣️ What is your reply?")
    elif "WORLD" in encounter:
        print("🌍 You turn to your companions and..." )