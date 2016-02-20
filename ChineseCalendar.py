def date(num):
    assert 0 < num <= 30, "Number out of bound"
    if num % 10 == 0:
        alphabet = "初二三"
        key = num // 10
        return alphabet[key-1] + "十"
    else:
        alphabet = "初十廿"
        alph = "一二三四五六七八九"
        key = num //10
        return alphabet[key] + alph[num % 10 - 1]
