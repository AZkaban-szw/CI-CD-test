from collections import defaultdict
from typing import List 

def dedupe_header(columns: List[str]) -> List[str]: 
    """ 
    给重复列名添加数字后缀以确保唯一（符合文档规则）
    规则：
    - 首次出现的列名保持原样
    - 第2、3...次出现的列名添加“.1”“.2”...
    - 保持原列表顺序
    - 输入输出均为字符串列表
    示例：["id", "name", "id", "name", "name"] → ["id", "name", "id.1", "name.1", "name.2"]
    """
    seen_counts = defaultdict(int) 
    result: List[str] = [] 
    for col in columns: 
        count = seen_counts[col] 
        if count == 0: 
            result.append(col) 
        else: 
            result.append(f"{col}.{count}") 
        seen_counts[col] += 1  # 记录该列名出现次数（关键步骤）
    return result 