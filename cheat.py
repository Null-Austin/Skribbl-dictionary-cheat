import requests

def get_words_from_url(url):
    response = requests.get(url)
    response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code
    data = response.text.splitlines()
    words = [line.split(',')[0] for line in data[1:]]  # Skip header and split to get the words
    return words

def filter_words(words, pattern):
    filtered_words = []
    pattern_length = len(pattern)
    for word in words:
        if len(word) == pattern_length:
            match = True
            for i in range(pattern_length):
                if pattern[i] != '_' and pattern[i] != word[i]:
                    match = False
                    break
            if match:
                filtered_words.append(word)
    return filtered_words

# URL of the word list
file = open('dict.txt','r')
words = get_words_from_url("https://gist.githubusercontent.com/mvark/9e0682c62d75625441f6ded366245203/raw/Skribbl-words.csv")

# Pattern to match
pattern = input("Current word: ")

# Get filtered words
matching_words = filter_words(words, pattern)

print(f"Words matching the pattern '{pattern}':\n")
for word in matching_words:
    print(word)
