# X-EVOLVE-MU05 Pain Regulation Layer

### 📌 模組定位
本專案為 X-EVOLVE 架構中的心理緩衝與最終保險模組。負責接收運算壓力與邏輯衝突產生的「原始痛覺」，並透過動態耐受度進行折減。

### ⚙️ 核心機制
- **痛覺緩衝 (Pain Attenuation)**：使系統免於因微小錯誤頻繁停機。
- **動態適應 (Dynamic Adaptation)**：根據任務成敗自動增減耐痛閾值。
- **自動熔斷 (Auto-Kill Switch)**：當有效痛覺突破臨界值，主動抹除當前進程，避免無價值的算力死鎖。

### 🚀 測試指令
於終端機執行 `python test_simulation.py` 觀測系統如何從適應走向受控破壞。
