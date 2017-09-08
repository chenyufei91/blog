# 定义获取分页所需数据的函数
def pagination_data(paginator, page, is_paginated):
    # 若没分页 无需时任何数据
    if not is_paginated:
        return {}
    page_num = page.number
    # 总页码
    total_pages = paginator.num_pages
    # 整个分页页码表
    page_range = paginator.page_range
    if total_pages <= 7:
        # 若总页数小于7 全显
        page_range = page_range

    elif page_num <= 4:
        # 若当前页是前4页 页码显示1-7
        page_range = range(1, 7)

    elif total_pages - page_num <= 3:
        # 若当前页是后4页， 显示后7 页
        page_range = range(total_pages-6, total_pages+1)

    else:
        # 显示当前页的前3页和后3页
        page_range = range(page_num-3, page_num+4)
    return {'page_range': page_range}