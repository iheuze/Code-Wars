def mix(s1, s2):
    def count_chars(s):
        return {c: s.count(c) for c in set(s) if c.islower() and s.count(c) > 1}

    counts1 = count_chars(s1)
    counts2 = count_chars(s2)

    result = []
    for char in set(counts1.keys()) | set(counts2.keys()):
        if char in counts1 and char in counts2:
            max_count = max(counts1[char], counts2[char])
            prefix = '=' if counts1[char] == counts2[char] else '1' if counts1[char] > counts2[char] else '2'
        elif char in counts1:
            max_count = counts1[char]
            prefix = '1'
        else:  # char in counts2
            max_count = counts2[char]
            prefix = '2'

        if max_count > 1:
            result.append(f"{prefix}:{char * max_count}")

    result.sort(key=lambda x: (-len(x), x))
    return '/'.join(result)
