from spellchecker import SpellChecker

class SpellCheckerApp:
    def __init__(self):
        self.spell = SpellChecker()

    def correct_text(self, text):
        words = text.split()
        corrected_words = []

        for word in words:
            corrected_word = self.spell.correction(word)
            if corrected_word != word.lower():
                print(f'Correction to "{word}" is "{corrected_word}"')
            corrected_words.append(corrected_word)

        return ' '.join(corrected_words)  # Use space instead of dot

    def run(self):
        print("\n..Spell Checker")

        while True:
            text = input('Enter your text to be spelled (or "exit" to quit): ')

            if text.lower() == 'exit':
                print('Exiting Spell Checker')
                break

            corrected_text = self.correct_text(text)
            print(f'Final corrected text: "{corrected_text}"\n')

if __name__ == "__main__":
    SpellCheckerApp().run()
