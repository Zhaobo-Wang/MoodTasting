# Database 初始化与使用指南

本指南介绍如何管理 `alcohol` 应用的 SQLite 数据库，包括表结构变更、初始化脚本执行以及在 VSCode 中查看数据库。

---

## 一、目录结构示例

```
model/
├── alcohol.sql         # 定义 alcohol 表结构与初始数据
├── material.sql        # 定义 material 表结构与初始数据
├── init_db.py          # 初始化脚本：从 SQL 脚本生成并填充 alcohol.db
├── alcohol.db          # 生成的 SQLite 数据库（二进制文件）
└── hooks/
    └── mood_selector.py
```

> **说明**：
>
> * `.sql` 文件为建表与插入数据的文本脚本，适合版本控制和 diff。
> * `alcohol.db` 为二进制数据库，用于应用运行时的 CRUD 操作。

---

## 二、初次初始化数据库

1. **切换到 `model/` 目录**：

   ```bash
   cd model
   ```

2. **运行初始化脚本**：

   ```bash
   python3 init_db.py
   ```

   * 脚本会依次执行 `alcohol.sql` 与 `material.sql` 中的内容
   * 生成 `alcohol.db` 并填充示例数据

3. **验证数据库**：

   * 直接用 VSCode 插件查看

---

## 三、每次更改表结构或初始数据

1. 修改或新增对应的 `.sql` 文件 (`alcohol.sql`／`material.sql`)
2. **重新运行**：

   ```bash
   python3 init_db.py
   ```

   * 脚本会 **覆盖**（DROP+CREATE）已有表，并重新插入所有脚本中列出的数据

> **提示**：如果希望在保留旧数据的同时应用新表结构，可以：
>
> * 手动在 SQLite 客户端执行 ALTER TABLE 语句；
> * 或在 `init_db.py` 加入逻辑，先备份旧表，再迁移数据。

---

## 四、在 VSCode 中查看与操作数据库

1. **安装插件**：

   * 推荐 `SQLite`（alexcvzz） 或 `SQLite Viewer`
2. **打开数据库**：

   * 在左侧 **Explorer** 面板找到 `alcohol.db`，右键选择 **Open Database**
3. **浏览表与数据**：

   * 展开 `alcohol` 与 `material` 表，可执行 `SELECT *` 等查询；
   * 也可直接在编辑器里新建 `.sql` 文件，连接到该数据库并运行任何 SQL。

---