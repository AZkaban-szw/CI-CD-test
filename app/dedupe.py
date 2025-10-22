def dedupe_header(columns, case_sensitive=False):
    """
    对列名列表进行去重处理，重复列名会添加序号后缀
    
    参数:
        columns: 列名列表
        case_sensitive: 是否区分大小写，默认为False（不区分）
    
    返回:
        去重后的列名列表
    """
    seen = {}
    result = []
    for col in columns:
        # 根据是否区分大小写选择键值
        key = col if case_sensitive else col.lower()
        if key not in seen:
            seen[key] = 1
            result.append(col)
        else:
            new_col = f"{col}.{seen[key]}"
            result.append(new_col)
            seen[key] += 1
    return result