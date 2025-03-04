def count_words(text):
    """
    This function takes a string input and returns the number of words in it.
    """
    words = text.split()
    return len(words)
# Main function for User input handling and display the word count
def main():
   user_input = input("Enter a sentence or paragraph: ").strip()

   # Error handling for empty input
   if not user_input:
       print("Error: No input provided. Please enter a valid sentence or paragraph.")
   else:
     # Counting words
     word_count = count_words(user_input)
     
     # Output display
     print(f"Word count: {word_count}")
     
if __name__ == "__main__":
    main()
