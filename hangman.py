import random
import shutil


# list of words
WORDS = [
    "python", "programming", "computer", "keyboard", "developer",
    "algorithm", "variable", "function", "internet", "software"
]

MAX_WRONG = 6


def print_title(title, fill="="):
    # print a centered title.
    width = shutil.get_terminal_size().columns
    print(fill * width)
    print(title.center(width))
    print(fill * width)


def display_word(secret_word, guessed_letters):
    # show the word with guessed letters revealed.
    return " ".join(
        letter if letter in guessed_letters else "_"
        for letter in secret_word
    )


def play_hangman():
    secret_word = random.choice(WORDS)
    guessed_letters = set()
    wrong_guesses = 0

    print_title("🎮 Hangman 🎮")

    while wrong_guesses < MAX_WRONG:
        # show current state
        print(f"\nWord: {display_word(secret_word, guessed_letters)}")
        print(f"Wrong guesses: {wrong_guesses}/{MAX_WRONG}")
        print(f"❤️  Lives left: {MAX_WRONG - wrong_guesses}")
        if guessed_letters:
            print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")

        # win check
        if all(letter in guessed_letters for letter in secret_word):
            print_title("🎉 You Win! 🎉", fill="-")
            print(f"The word was: {secret_word}")
            return

        # get input
        user_input = input("\nGuess a letter: ").strip().lower()

        # validate
        if len(user_input) != 1 or not user_input.isalpha():
            print("Please enter a single letter (a-z).")
            continue

        # already guessed?
        if user_input in guessed_letters:
            print(f"⚠️  You already guessed '{user_input}'. Try another.")
            continue

        guessed_letters.add(user_input)

        # correct or wrong?
        if user_input in secret_word:
            print(f"✅ Good guess! '{user_input}' is in the word.")
        else:
            wrong_guesses += 1
            print(f"❌ Wrong! '{user_input}' is not in the word.")
            print(f"💔 You lost a life. ({MAX_WRONG - wrong_guesses} left)")

    print_title(" Game Over ", fill="-")
    print(f"The word was: {secret_word}")


if __name__ == "__main__":
    play_hangman()
