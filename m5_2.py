with open("text_1.txt", "r", encoding='utf-8') as f_obj:
    text2 = [f'{line}. {count.strip()}, {len(count.strip())}'
             for line, count in enumerate(f_obj, 1)]
    print(*text2, f"total row - {len(text2)}.", sep="/n")