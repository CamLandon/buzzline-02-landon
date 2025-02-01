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
    "COMBAT: A band of orcs blocks your path!",
    "COMBAT: A shadowy assassin strikes from the darkness!",
    "COMBAT: A group of skeletons rises from the grave!",
    "COMBAT: A gelatinous cube oozes into the corridor!",
    "COMBAT: A mimic reveals its true form!",
    "COMBAT: A werewolf howls under the full moon!",
    "COMBAT: A swarm of bats fills the cave!",
    "COMBAT: A troll demands a toll—or else!",
    "LOOT: You find a treasure chest.",
    "LOOT: A magical sword lies in the ruins.",
    "LOOT: You discover an ancient spellbook covered in runes.",
    "LOOT: A cursed artifact hums with dark energy.",
    "LOOT: A hidden compartment reveals a pouch of gold!",
    "LOOT: A mysterious potion sits on an altar.",
    "LOOT: A merchant's abandoned cart is full of supplies.",
    "LOOT: A dragon's hoard glitters in the dim light.",
    "LOOT: A magical ring pulses with unknown power.",
    "LOOT: A forgotten chest contains a map to something greater.",
    "NPC: A mysterious stranger offers a quest.",
    "NPC: A town guard warns you about bandits.",
    "NPC: A hooded figure whispers, 'They're watching you...'",
    "NPC: An old wizard offers cryptic advice before vanishing.",
    "NPC: A wounded soldier begs for help on the road.",
    "NPC: A rogue offers to sell you stolen goods.",
    "NPC: A bard sings a song about a lost kingdom.",
    "NPC: A druid warns of unnatural storms approaching.",
    "NPC: A child claims to have seen a ghost in the woods.",
    "NPC: A beggar swears they know the location of a hidden treasure.",
    "WORLD: A thick fog rolls in, obscuring your vision.",
    "WORLD: The ground trembles as something massive moves below.",
    "WORLD: A sudden blizzard forces you to seek shelter.",
    "WORLD: A river blocks your path—will you cross it or find another way?",
    "WORLD: A magical portal hums with unstable energy.",
    "WORLD: A ruined castle looms on the horizon.",
    "WORLD: A solar eclipse darkens the sky—ominous whispers fill the air.",
    "WORLD: A mysterious storm crackles with arcane energy.",
]

while True:
    encounter = random.choice(encounters)
    producer.send(topic, value=encounter)
    print(f"Sent: {encounter}")
    time.sleep(3)  # Send an encounter every 3 seconds
