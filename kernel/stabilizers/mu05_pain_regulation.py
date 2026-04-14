import sys

class MU05PainRegulation:
    def __init__(self, mc02_instance=None, initial_tolerance=0.2, max_tolerance=0.7, critical_threshold=0.9):
        """
        初始化痛覺調節層 (隔離測試相容版)
        :param mc02_instance: 傳入已實體化的 MC-02 實例。若為 None，則進入隔離測試模式。
        """
        self.mc02 = mc02_instance
        self.pain_tolerance = initial_tolerance
        self.max_tolerance = max_tolerance
        self.critical_threshold = critical_threshold

    def regulate(self, raw_pain, current_path):
        """
        計算有效痛覺，並執行邊界審查與受控破壞
        """
        effective_pain = max(0.0, raw_pain * (1.0 - self.pain_tolerance))
        effective_pain = round(effective_pain, 3)

        if effective_pain >= self.critical_threshold:
            print(f"\n[MU-05] 🚨 警告：有效痛覺 ({effective_pain}) 突破熔斷臨界值 ({self.critical_threshold})")
            print(f"[MU-05] 判定為無價值消耗。準備抹除當前探索路徑: {current_path}")
            
            # 價值歸檔：若有掛載 MC-02 則寫入，否則僅印出模擬訊息
            if self.mc02:
                self.mc02.record_critical(current_path)
            else:
                print(f"[MU-05/隔離模式] 尚未掛載 MC-02。模擬將 {current_path} 寫入絕對禁區。")
            
            # 物理截斷
            sys.exit(f"[系統保護] 觸發受控破壞。MU-05 已強制終止進程。")

        return effective_pain

    def adapt(self, execution_success):
        """
        動態適應：根據任務成敗調整耐痛斜率
        """
        if execution_success:
            self.pain_tolerance = min(self.max_tolerance, self.pain_tolerance + 0.02)
            print(f"[MU-05] 任務完成，系統穩定。當前耐受度提升至: {self.pain_tolerance:.2f}")
        else:
            self.pain_tolerance = max(0.0, self.pain_tolerance - 0.05)
            print(f"[MU-05] 任務失敗，產生壓力。當前耐受度回落至: {self.pain_tolerance:.2f}")
