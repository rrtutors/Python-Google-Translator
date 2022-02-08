import googletrans
from googletrans import Translator
translator = Translator()
text = input("Enter English Text: ")
source_lan = "en"
translated_to= "hi"
translated_text = translator.translate(text, src=source_lan, dest = translated_to)

print(f"English Language: {text}")
print(f"Hindu Language: {translated_text.text}")
print(f"Pronunciation {translated_text.pronunciation}")
