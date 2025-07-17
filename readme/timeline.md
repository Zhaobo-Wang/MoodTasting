# Phase 1:

## 模型策略

MoodTaste —— 用户输入学校和自然语言心情，模型返回风格化文案、匹配酒款和调配表  

NLP + LLM 联合识别学校和多样化心情的最佳策略  

### 1 数据与结构准备  

#### 1.1 心情标签词典  

**目标：**  

覆盖常见的情绪以及同义词，支撑后续关键词匹配和分类模型对比  

**步骤：**  

列出 12–15 个核心情绪标签（如：happy、tired、nostalgic、stressed、excited、relaxed、romantic、angry、sad、bored、anxious、celebratory）。  

为每个标签搜集 8–12 个中文同义词/短语，写入 model/moods.json。  

**交付：**  

model/moods.json    

#### 1.2 数据库准备  

**目标：**  

设计两张以上表，存储酒款基本信息与调配明细，支持后续检索和CRUD  

**表设计：**  

**alcohol:**       
mood  
name  
description  
pairing  

**ingredient:**  
alcohol_name TEXT,  
material,  
volume_ml,  
FOREIGN KEY(alcohol_name) REFERENCES alcohol(name)  

**交付：**  
model/alcohol.sql  
model/ingredient.sql  
model/init_db.py  
model/alcohol.db  

### 2 情绪解析 Hook    

#### 2.1 关键词匹配版

