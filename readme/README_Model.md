# moodTaste 模型目录说明

本目录存放与 Ollama 定制模型相关的配置和脚本。

## 目录结构

```

model/
├── Modelfile            # Ollama 定制模型的 Modelfile
├── moods.json           # 心情标签词典（关键词映射）
├── alcohol.sql            # 建库脚本（可选）
├── alcohol.db             # SQLite 数据库（或由 alcohol.sql 生成）
└── hooks/
└── mood\_selector.py # 输入钩子脚本，用于情绪解析和酒款查询

```

## 依赖环境

- Python 3.x
- sqlite3 命令行工具
- Ollama CLI (gemma3:1b 已 pull)

## 初始化步骤

1. 确保 `moods.json` 与 `alcohol.db` 在同级目录。
2. 给钩子脚本赋予执行权限：

   ```bash
   chmod +x hooks/mood_selector.py
   ```

## 创建并运行定制模型

1. 进入 `model/` 目录：

   ```bash
   cd model
   ```

2. 创建模型（首次或更新时使用 `--force` 覆盖）：

   ```bash
   ollama create mood-taste -f Modelfile --force
   ```

3. 运行模型：

   ```bash
   ollama run mood-taste --template default --vars school="清华大学" --vars mood="happy" "I feel great today"
   ```

## 脚本测试

如果想单独测试 Hook 脚本输出：

```bash
echo "happy" | python3 hooks/mood_selector.py
```

根据输出的 SYSTEM+USER 部分，你可以在 `ollama run` 时把它当作 prompt 发给模型。

