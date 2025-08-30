def word_frequency_counter(paragraph):
    # Split words and make lowercase
    words = paragraph.lower().split()

    # Dictionary for counting
    freq = {}

    for word in words:

        word = word.strip('.,!?;:" ') #remove punctuations around the word
        if word in freq:
            freq[word] += 1   # if already exists, add +1
        else:
            freq[word] = 1    # if first time, set as 1

    # Sort dictionary by values (descending)
    sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)


    # Prints TOP 3 most frequent words in the paragraph
    print("Top 3 most frequent words:")
    for word, count in sorted_items[:3]:
        print(f"{word} : {count}")

#Finally running the input command
para = input("Enter the paragraph: ")
word_frequency_counter(para)
