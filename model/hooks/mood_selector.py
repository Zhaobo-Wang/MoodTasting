#!/usr/bin/env python3
import sys
import os
import sqlite3

# step 1: read user input

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding='utf-8')

user_input = sys.stdin.read().strip()
if not user_input:
    sys.exit(0)

# step 2: extract mood from user input

labels = ["happy","tired","nostalgic","stresponsesed","excited","relaxed",
          "romantic","angry","sad","bored","anxious","celebratory"]

classification_prompt = (
    "你是情绪分析师，请判断下面句子的主要心情，只能从以下标签中选择："
    f"{', '.join(labels)}\n\nUser Input:\"{user_input}\""
)

import subprocess, shlex

cmd = f"ollama run gemma3:1b {shlex.quote(classification_prompt)} --no-stream"
response = subprocess.run(shlex.split(cmd), capture_output=True, text=True, cwd=os.path.dirname(__file__))

if response.returncode != 0:
    sys.stderr.write(f"Error classifying mood: {response.stderr}")
    mood = "neutral"
else:
    mood = response.stdout.strip().splitlines()[-1].strip().lower()
    if mood not in labels:
        mood = "neutral"

# step 3: query db by mood

BASE = os.path.dirname(__file__)
db_path = os.path.join(BASE, '../alcohol.db')
recommendation = []

try:
    connectToDB = sqlite3.connect(db_path)
    cursor = connectToDB.cursor()
    cursor.execute("SELECT name, description, pairing FROM alcohol WHERE mood = ?", (mood,))
    for name, desc, pairing in cursor.fetchall():
        recommendation.append(f"- {name}: {desc} (Pairing: {pairing})")
    connectToDB.close()
    
except Exception as e:
    sys.stderr.write(f"DB query failed: {e}")

if recommendation:
    recommendation_text = "\n".join(recommendation)
else:
    "Sorry, I don't have any recommendations for you :("

output = (
    f"Mood Analysis:\n"
    f"Based on your mood ('{mood}'), here are my cocktail recommendations:\n"
    f"{recommendation_text}\n\n"
)

sys.stdout.write(output)
