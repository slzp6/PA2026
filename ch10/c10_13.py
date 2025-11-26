"""c10_13.py"""


def pattern_search(text, pattern):
    """pattern search"""
    len_t = len(text)
    len_p = len(pattern)
    for i in range(0, len_t - len_p + 1):
        j = 0
        while j < len_p and text[i + j] == pattern[j]:
            j = j + 1
        if j == len_p:
            return i
    return -1


# -----012345678901
TXT = "AUGUAAUAGUGG"
PAT1 = "UAG"
PAT2 = "UAA"

stat = pattern_search(TXT, PAT1)
print("012345678912")
print(f"{TXT} {PAT1} {stat}")

stat = pattern_search(TXT, PAT2)
print("012345678912")
print(f"{TXT} {PAT2} {stat}")
