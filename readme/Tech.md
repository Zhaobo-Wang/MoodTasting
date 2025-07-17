## 整体技术架构图


* **前端（Vue）**

  * 负责用户输入心情、学校；展示生成的配方与文案；提供分享/收藏功能。
  * 用 **组件化结构**（输入表单、结果卡片、历史列表），方便未来如果改用 React 或移动端，也好复用设计。

* **后端（Java + Spring Boot）**

  * 暴露 REST API 给前端，如：

    * `POST /api/recommend`：接收 `{ mood, school }`，返回渲染好的 prompt 和最终配方文本。
    * `GET  /api/history`：用户历史配方。
  * 负责：

    1. 调用 Hook 服务生成带情绪+学校信息的 prompt。
    2. 调用 Ollama CLI（或用 Java 进程直接执行 `ollama run …`）获取 LLM 输出。
    3. 解析并返回给前端。

* **模型服务（Ollama）**

  * 在服务器上以守护进程方式运行。后端通过 gRPC 或 HTTP 调用。
  * Modelfile、Hook 脚本、SQLite 数据库都放在同一个 `model/` 目录（对外只读）。

* **数据库（SQLite 或轻量 JSON）**

  * 存储心情标签、学校元数据、酒款映射、用户历史。
  * 如果后期流量上来，能平滑切换到 PostgreSQL + pgvector；调用层接口不变。


## 项目结构

```
your-gitlab-repo/
├── backend/                   # Java 后端
│   ├── src/
│   ├── pom.xml
│   └── ...
├── frontend/                  # Vue 前端
│   ├── src/
│   ├── package.json
│   └── ...
├── model/                     # Modelfile + Hook 脚本 + 数据库
│   ├── Modelfile
│   ├── hooks/
│   └── wines.db
├── .gitignore
└── README.md
```

* **`.gitignore`**：忽略所有编译产物、IDE 配置、模型/权重、数据库二进制（可选）。
* **`README.md`**：详细说明依赖环境、安装步骤、如何初始化 Ollama、如何运行前后端、如何更新模型配置。

---

## 架构可演进要点

1. **模型隔离**

   * 不在主代码中硬编码调用 `ollama`，而是通过统一的 “模型调用服务” 接口。未来换模型或云端 API，只需替换服务实现。

2. **数据层解耦**

   * 目前用 SQLite 做映射，但后端永远通过同一接口查询。未来可以换到任何关系型或向量数据库，无影响上层业务逻辑。

3. **前后端分离**

   * 前端完全通过 REST API 与后端交互，未来可以替换成移动端 App、Electron 桌面端，或者直接用 Swagger UI 调试。

4. **配置即代码**

   * Modelfile、Hook 脚本、标签词典都纳入 Git 管理，任何修改都能在 CI 中自动测试（例如模拟 `ollama run` 结果是否包含预期字段）。



