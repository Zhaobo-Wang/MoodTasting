#!/usr/bin/env python3
import sys
import os
import sqlite3
import subprocess, shlex
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from logger_config import get_logger

logger = get_logger('mood_selector')

logger.info("Starting mood_selector.py")

# step 1: 获得用户输入

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding='utf-8')

user_input = sys.stdin.read().strip()
logger.info(f"User input: {user_input}")

if not user_input:
    logger.warning("No user input provided")
    sys.exit(0)

# step 2: 从用户输入中分析当前心情

labels = ["happy","tired","nostalgic","stresponsesed","excited","relaxed",
          "romantic","angry","sad","bored","anxious","celebratory"]

classification_prompt = (
    "分析以下文本的情绪, 只回复一个词: happy, tired, nostalgic, stressed, excited, relaxed, romantic, angry, sad, bored, anxious, celebratory。\n\n"
    f"文本：\"{user_input}\""
)


cmd = f"ollama run gemma3:1b {shlex.quote(classification_prompt)}"
logger.info(f"Running command: {cmd}")

try:
    response = subprocess.run(
            shlex.split(cmd), 
            capture_output=True, 
            text=True, 
            encoding='utf-8',
            errors='replace',
            cwd=os.path.dirname(__file__)
        )

    logger.info(f"Command output: {response.stdout}")
    logger.info(f"Command error: {response.stderr}")
    logger.info(f"Command returncode: {response.returncode}")
    
    if response.returncode != 0 or response.stdout is None:
        logger.error(f"Error classifying mood: {response.stderr}")
        mood = "neutral"
    else:
        mood = response.stdout.strip().splitlines()[-1].strip().lower()
        
        logger.info(f"Mood: {mood}")
        
        if mood not in labels:
            logger.info(f"Mood not in labels: {mood}, setting to neutral")
            mood = "neutral"
            
except Exception as e:
    logger.exception(f"Error classifying mood: {e}")
    mood = "neutral"
    
logger.info(f"Final mood: {mood}")

# step 3: 从数据库中根据当前心情获取推荐

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
    recommendation_text = "Sorry, I don't have any recommendations for you :("

output = (
    f"Mood Analysis:\n"
    f"Based on your mood ('{mood}'), here are my cocktail recommendations:\n"
    f"{recommendation_text}\n\n"
)

sys.stdout.write(output)
