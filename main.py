from googletrans import Translator, LANGUAGES


def translate_text():
    translator = Translator()

    # Display supported languages
    print("Supported languages:")
    for lang_code, lang_name in LANGUAGES.items():
        print(f"{lang_code}: {lang_name}")

    source_lang = input("Enter the source language code (e.g., 'en' for English): ").strip().lower()
    target_lang = input("Enter the target language code (e.g., 'fr' for French): ").strip().lower()

    while True:
        text = input("Enter text to translate (or type 'exit' to quit): ").strip()
        if text.lower() == 'exit':
            break

        try:
            translated = translator.translate(text, src=source_lang, dest=target_lang)
            print(f"Translation ({LANGUAGES[source_lang]} to {LANGUAGES[target_lang]}): {translated.text}")
        except Exception as e:
            print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    translate_text()
