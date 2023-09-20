from googletrans import Translator
translator = Translator()
# <Translated src=ko dest=en text=Good evening. pronunciation=Good evening.>
out = translator.translate('hi', dest='ar')

print(out.text)