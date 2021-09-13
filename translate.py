from textblob import TextBlob
def from_spanish(my_text):
    lang = TextBlob(my_text)
    try: # sometimes fails because of API
        if lang.detect_language() == 'es':
            return lang.translate(to='en')
        else:
            return False
    except Exception as e:
        print(e)
        return False


if __name__ == "__main__":
    # this is a test that will run if you call the module directly
    result = from_spanish(my_text = "como estan")
    if result:
        print(result)