from kernel.stabilizers.mu05_pain_regulation import MU05PainRegulation
import time

def run_simulation():
    # 初始化 MU-05 (不掛載 MC-02，進行隔離測試)
    mu05 = MU05PainRegulation(initial_tolerance=0.2, critical_threshold=0.8)
    
    print("=== 開始模擬受控擾動測試 ===")
    
    # 測試階段 1：日常輕微阻礙 (適應性測試)
    print("\n[階段 1] 模擬一般性任務執行...")
    for _ in range(3):
        eff_pain = mu05.regulate(raw_pain=0.3, current_path="normal_API_request")
        print(f"原始痛覺 0.3 -> 有效痛覺 {eff_pain} (未達熔斷值，繼續執行)")
        mu05.adapt(execution_success=True)
        time.sleep(0.5)

    # 測試階段 2：模擬死鎖/無限迴圈 (熔斷測試)
    print("\n[階段 2] 模擬邏輯死鎖，原始痛覺急速飆升...")
    loop_path = "infinite_recursive_search"
    pain_surge = [0.5, 0.7, 0.95, 1.2]
    
    for raw in pain_surge:
        print(f"輸入原始痛覺: {raw}...")
        # 當輸入 1.2 時，即便有耐受度折減，有效痛覺仍會衝破 0.8，觸發強制退出
        eff_pain = mu05.regulate(raw_pain=raw, current_path=loop_path)
        print(f"有效痛覺 {eff_pain}，系統依然存活，嘗試適應...")
        mu05.adapt(execution_success=False)
        time.sleep(0.5)

if __name__ == "__main__":
    run_simulation()
