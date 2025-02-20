def count_unique_characters(val: str) -> int:
    val = val.lower()
    return sum(map(lambda x: val.count(x) == 1, set(val)))


message = "Today is a beautiful day! The sun is shining and the birds are singing."

unique_count = count_unique_characters(message)
print("Количество уникальных символов в строке:", unique_count)
