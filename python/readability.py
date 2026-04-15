# Returns the reading level of any text

from cs50 import get_string

def main():
    # Get text from the user
    text = get_string("Text: ")

    # Count letters in the text
    letter_count = count_letters(text)

    # Count words in the text
    word_count = count_words(text)

    # Count sentences in the text
    sentence_count = count_sentences(text)

    # Calculate reading level
    avg_letters = (letter_count / word_count) * 100

    avg_sentences = (sentence_count / word_count) * 100

    reading_level = coleman_liau(avg_letters, avg_sentences)

    # Print reading level between 1 and 16
    if 1 <= reading_level < 16:
        print(f"Grade {round(reading_level)}")
    elif reading_level < 1:
        print("Below Grade 1")
    elif reading_level > 16:
        print("Grade 16+")


def count_letters(text):
    letter_count = 0
    for character in text.lower():
        if character.isalpha():
            letter_count += 1
    return letter_count
            

def count_words(text):
    word_count = 1
    for character in text:
        if character == " ":
            word_count += 1
    return word_count


def count_sentences(text):
    sentence_count = 0
    for character in text:
        if character in ".?!":
            sentence_count += 1
    return sentence_count

def coleman_liau(avg1, avg2):
    level = 0.0588 * avg1 - 0.296 * avg2 - 15.8
    return level
    


if __name__ == "__main__":
    main()