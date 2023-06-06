import random


class Hangman:
    def __init__(self, wordlist):
        self.wordlist = wordlist
        self.max_attempts = 3
        self.current_attempt = 0
        self.secret_word = ""
        self.guessed_letters = set()
        self.available_letters = set('abcdefghijklmnopqrstuvwxyz')
        self.hints = {
            "python": "bahasa programming yang populer",
            "hangman": "nama game yang kamu mainkan",
            "game": "sebuah aktivitas atau kompetisi yang menggunakan peraturan",
            "programming": "proses dari membuat program komputer"
        }
        self.emoticons = {
            "level_win": "\U0001F389",  # Fireworks emoji
            "game_win": "\U0001F973"    # Party popper emoji
        }
        self.stages = [
            """
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |     / \\
               -
            """,
            """
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |     /
               -
            """,
            """
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |
               -
            """,
            """
               --------
               |      |
               |      O
               |     \\|
               |      |
               |
               -
            """,
            """
               --------
               |      |
               |      O
               |      |
               |      |
               |
               -
            """,
            """
               --------
               |      |
               |      O
               |    
               |      
               |
               -
            """,
            """
               --------
               |      |
               |      
               |    
               |      
               |
               -
            """
        ]

    def choose_word(self):
        self.secret_word = random.choice(self.wordlist).lower()

    def play(self):
        print("Selamat datang digame Hangman!")
        self.choose_word()
        self.display_hint()

        while True:
            self.display_hangman()
            self.display_word()
            self.display_available_letters()

            guess = input("Tebak kata : ").lower()

            if guess == 'exit':
                print("Game berakhir. sampai jumpa lagi!")
                break

            if not guess.isalpha() or len(guess) != 1:
                print("Tebakan tidak berlaku. Masukkan satu huruf")
                continue

            if guess in self.guessed_letters:
                print("kamu sudah menebak huruf tersebut.")
                continue

            if guess not in self.available_letters:
                print("huruf tersebut tidak tersedia silahkan menebak huruf yang lain.")
                continue

            self.guessed_letters.add(guess)
            self.available_letters.remove(guess)

            if guess in self.secret_word:
                print("tebakanmu benar!")
                if self.is_word_guessed():
                    self.display_word()
                    print("selamat!kamu berhasil menyelesaikannya! " +
                          self.emoticons["level_win"])
                    self.wordlist.remove(self.secret_word)
                    if len(self.wordlist) > 0:
                        choice = input(
                            "Apakah kamu mau naik ke level selanjutnya? (ya/tidak): ")
                        if choice.lower() == "ya":
                            self.reset_game()
                            continue
                        else:
                            print("terima kasih telah bermain!sampai bertemu lagi!")
                    else:
                        print(
                            "Selamat! kamu telah berhasil menyelesaikan semua level" + self.emoticons["game_win"])
                    break
            else:
                print("Tebakan salah!")
                self.current_attempt += 1
                if self.current_attempt == self.max_attempts:
                    self.display_hangman()
                    print("Game over! kata tersebut adalah :", self.secret_word)
                    choice = input(
                        "Apakah kamu ingin bermain lagi? (ya/tidak): ")
                    if choice.lower() == "ya":
                        self.reset_game()
                        continue
                    else:
                        print("terima kasih telah bermain! sampai bertemu lagi")
                        break

    def reset_game(self):
        self.current_attempt = 0
        self.guessed_letters = set()
        self.available_letters = set('abcdefghijklmnopqrstuvwxyz')
        self.choose_word()
        self.display_hint()

    def display_hangman(self):
        print(self.stages[self.current_attempt])

    def display_word(self):
        for letter in self.secret_word:
            if letter in self.guessed_letters:
                print(letter, end=" ")
            else:
                print("_", end=" ")
        print()

    def display_available_letters(self):
        available_letters = self.available_letters - self.guessed_letters
        print("Huruf yang tersedia :", " ".join(available_letters))

    def display_hint(self):
        hint = self.hints.get(self.secret_word, "petunjuk tidak tersedia")
        print("Petunjuk:", hint)

    def is_word_guessed(self):
        for letter in self.secret_word:
            if letter not in self.guessed_letters:
                return False
        return True


wordlist = ["python", "hangman", "game", "programming"]
game = Hangman(wordlist)
game.play()
