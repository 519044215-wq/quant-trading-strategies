#!/usr/bin/env python3
"""
双创50指数增强策略
创建时间: 2025-03-27
作者: OpenClaw
"""

# 策略逻辑说明
# 1. 基准: 双创50指数 (931643)
# 2. 股票池: 双创50成分股
# 3. 调仓频率: 季度
# 4. 选股数量: 20只
# 5. 增强因子: 价值、动量、质量、低波动

import pandas as pd
import numpy as np

class DualCreativity50Enhancement:
    """双创50增强策略"""
    
    def __init__(self):
        self.index_code = "931643"
        self.stock_count = 20
    
    def select_stocks(self, factors_df):
        """多因子选股"""
        # 按综合得分排序
        selected = factors_df.nlargest(self.stock_count, 'score')
        return selected['code'].tolist()

if __name__ == "__main__":
    print("双创50增强策略初始化完成")
