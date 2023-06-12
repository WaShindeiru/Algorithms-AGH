import copy
import time

def naive_search(text, pattern):
    text_len = len(text)
    pattern_len = len(pattern)
    answer_count = 0
    comparison_count = 0

    m = 0
    while(m < text_len - pattern_len + 1):
        valid = True

        i = 0
        while(i < pattern_len):
            comparison_count += 1
            if text[m + i] != pattern[i]:
                valid = False
                break
    
            i += 1

        if valid is True:
            answer_count += 1

        m += 1

    return answer_count, comparison_count


def hash(word):
    hw = 0
    word_len = len(word)
    d = 256
    q = 101

    for i in range(word_len):
        hw = (hw*d + ord(word[i])) % q

    return hw


def simple_hash_comparison(text, pattern):
    text_len = len(text)
    pattern_len = len(pattern)
    pattern_hash = hash(pattern)

    comparison_count = 0
    answer_count = 0

    for m in range(0, text_len - pattern_len + 1, 1):
        text_hash = hash(text[m:m+pattern_len:1])

        comparison_count += 1
        if text_hash == pattern_hash:
            if pattern == text[m : m+pattern_len : 1]:
                answer_count += 1

    return answer_count, comparison_count


def rolling_hash_comparison(text, pattern):
    d = 256
    q = 101

    text_len = len(text)
    pattern_len = len(pattern)
    pattern_hash = hash(pattern)

    h = 1
    for i in range(pattern_len - 1):
        h = (h*d) % q

    comparison_count = 0
    answer_count = 0
    collision_count = 0

    text_hash = hash(text[0: pattern_len: 1])

    for m in range(0, text_len - pattern_len + 1, 1):
        comparison_count += 1
        if text_hash == pattern_hash:
            if pattern == text[m : m+pattern_len : 1]:
                answer_count += 1
            else:
                collision_count += 1

        if m + pattern_len < text_len:
            text_hash = (d * (text_hash - ord(text[m]) * h) + ord(text[m + pattern_len])) % q
            if text_hash < 0:
                text_hash += q

    return answer_count, comparison_count, collision_count

def kmp_table(word):
    pos = 1
    cnd = 0

    T = [0 for i in range(len(word) + 1)]

    T[0] = -1

    while pos < len(word):
        if word[pos] == word[cnd]:
            T[pos] = T[cnd]

        else:
            T[pos] = cnd

            while cnd >= 0 and word[pos] != word[cnd]:
                cnd = T[cnd]

        pos += 1
        cnd += 1

    T[pos] = cnd

    return T


def kmp_search(text, word):
    m = 0
    i = 0
    T = kmp_table(word)
    match = 0

    action = 0

    np = 0
    while m < len(text):
        action += 1

        if word[i] == text[m]:
            m += 1
            i += 1

            if i == len(word):
                match += 1
                np += 1
                if T[i] != -1:
                    i = T[i]

        else:
            i = T[i]
            if i < 0:
                m += 1
                i += 1

    return match, action, T


def main():
    with open("lotr.txt", encoding='utf-8') as f:
        text = f.readlines()
        S = "".join(text).lower()

        t_start = time.perf_counter()
        answer_count, comparison_count = naive_search(S, "time.")
        t_stop = time.perf_counter()

        print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
        print(answer_count, comparison_count, sep="; ")

        t_start = time.perf_counter()
        answer_count, comparison_count = simple_hash_comparison(S, "time.")
        t_stop = time.perf_counter()

        print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
        print(answer_count, comparison_count, sep=", ")

        t_start = time.perf_counter()
        answer_count, comparison_count, collision_count = rolling_hash_comparison(S, "time.")
        t_stop = time.perf_counter()

        print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
        print(answer_count, comparison_count, collision_count, sep=", ")

        t_start = time.perf_counter()
        answer_count, comparison_count, T_table = kmp_search(S, "time.")
        t_stop = time.perf_counter()

        print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
        print(answer_count, comparison_count, T_table, sep=", ")

if __name__ == "__main__":
    main()