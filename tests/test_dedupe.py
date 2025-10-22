# 从dedupe.py中导入要测试的函数（与文档一致）
from dedupe import dedupe_header 

# 测试1：无重复列名（文档示例）
def test_unique_columns(): 
    assert dedupe_header(["id", "name", "age"]) == ["id", "name", "age"] 

# 测试2：同一列名重复多次（文档示例）
def test_duplicate_columns(): 
    assert dedupe_header(["id", "id", "id"]) == ["id", "id.1", "id.2"] 

# 测试3：多列名交叉重复（文档示例）
def test_mixed_columns(): 
    cols = ["id", "name", "id", "name", "name"] 
    expected = ["id", "name", "id.1", "name.1", "name.2"] 
    assert dedupe_header(cols) == expected