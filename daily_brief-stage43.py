# === Stage 43: Добавь пагинацию длинных списков ===
# Project: DailyBrief
def paginate(items, page_size=10):
    """Compact pagination helper: returns (page_index, page_items, total_pages)."""
    total_pages = (len(items) + page_size - 1) // page_size
    if page_size <= 0:
        total_pages = 0
        page_items = []
    else:
        page_index = int(input("Enter page number (1-based): "))
        if page_index < 1 or page_index > total_pages:
            print(f"Invalid page. Choose 1..{total_pages}")
            return page_index, [], total_pages
        start = (page_index - 1) * page_size
        page_items = items[start:start + page_size]
    return page_index, page_items, total_pages
