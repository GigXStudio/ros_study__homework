nums = [
    ['zero', 'ноль'],
    ['one', 'один'],
    ['two', 'два'],
    ['three', 'три'],
    ['four', 'четыре'],
    ['five', 'пять'],
    ['six', 'шесть'],
    ['seven', 'семь'],
    ['eight', 'восемь'],
    ['nine', 'девять'],
    ['ten', 'десять']
]


def num_translate(num):
    if isinstance(num, str):
        for original, translated in nums:
            if num.strip().lower() == original:
                return translated
    return num
