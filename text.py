def count_upper_case_letters(text):

    upper_case_count = 0
    for char in text:
        if char.isupper():
            upper_case_count += 1
    return upper_case_count
