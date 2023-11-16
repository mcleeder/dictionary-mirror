import requests
from lxml import html
from scraper import element, elements

class Dictionary():
    def _get_raw_word(self, word: str) -> requests.Response:
        response = requests.get(f"https://www.dictionary.com/browse/{word}")
        return response.content
    
    def _parse_word(self, raw_html: str) -> dict:
        html_element = html.fromstring(raw_html)

        if definition_card := element(html_element, "//section[@data-type='word-definition-card']"):
            word = element(definition_card, "//h1").text
            pro = element(definition_card, "//span[@data-type='pronunciation-text']").text

            definition_elements = elements(definition_card, "div[@data-type='word-definitions']")
            definitions = []
            for elem in definition_elements:
                word_type = element(elem, "span/span[@class='luna-pos']").text
                word_defs = []
                for li in elements(elem, "div/ol/li"):
                    word_defs.append(element(li, "div/p").text)
                definitions.append({
                    "word_type" : word_type.capitalize().replace(",",""),
                    "word_definitions" : [w.capitalize() for w in word_defs if w] 
                })
                

            return {
                "word" : word.capitalize(),
                "pronunciation" : pro[1:-1].strip(), # [ bahrn  ]
                "definitions" : definitions,
            }
        return {"word" : "Oops, something went wrong"}
    
    def lookup(self, word: str) -> dict:
        raw_data = self._get_raw_word(word)
        return self._parse_word(raw_data)
    
dictionary = Dictionary()

foo = dictionary.lookup("barn")
print(foo)