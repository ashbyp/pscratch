

def find_anagrams(words: list[str]) -> list[str]:
    tally = {}
    for word in words:
        key = ''.join(sorted(word.lower()))
        if key not in tally:
            tally[key] = [word]
        else:
            tally[key].append(word)

    # return [x for x in tally.values() if len(x) > 1]
    return tally.values()


if __name__ == '__main__':
    print(find_anagrams(["car", "tree", "boy", "girl", "arc", "Tree", 'YOB']))


