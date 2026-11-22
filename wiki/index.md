# AI Agents LLM Wiki — 知識庫索引

主題：**AI Agents：從大型語言模型到自主執行任務的 AI 系統**。

## 先討論、後生成
先規劃五個教學問題：「什麼是 Agent？」「有哪些組件？」「怎麼循環運作？」「Workflow/Graph 差異？」「有什麼風險？」才選擇官方資料、轉述入庫、建立引用與檢索。

## 章節
1. [基本概念](concepts.md)
2. [核心架構](architecture.md)
3. [Agent Loop](agent-loop.md)
4. [Workflow 與 Graph](workflows.md)
5. [限制與安全性](safety.md)

## Ingest 清單
| ID | 來源 | 摘要檔 | 核心證據 |
|---|---|---|---|
| S01 | OpenAI Practical Guide | [S01](../sources/S01.md) | S01-E1, E2, E3 |
| S02 | Anthropic Building Effective Agents | [S02](../sources/S02.md) | S02-E1, E2, E3 |
| S03 | OpenAI Developers Building Agents | [S03](../sources/S03.md) | S03-E1, E2 |
| S04 | Microsoft Agent Architecture | [S04](../sources/S04.md) | S04-E1, E2 |
| S05 | Microsoft Agent Framework | [S05](../sources/S05.md) | S05-E1, E2 |

**檢索方法**：執行 `python scripts/query.py "查詢詞"`；程式只搜尋本地 Wiki 與 source 摘要，回傳檔名與證據卡 ID。這是可重現的輕量 Wiki 檢索，不使用向量資料庫或 LLM API。後續 AI 必須依檢索結果撰寫，不能自稱即時讀到網路上的新資料。
