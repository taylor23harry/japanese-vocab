import scrapy
from scrapy.loader import ItemLoader

from jishoscrapy.items import JishoWordItem

class JishoSpider(scrapy.Spider):
    name = "jisho"
    allowed_domains = ["jisho.org"]
    start_urls = ["https://jisho.org"]

    def __init__(self, item):
        self.item = item

    def start_requests(self):
        url = f"https://jisho.org/search/{self.item}"
        yield scrapy.Request(url=url)

    def parse(self, response):
        exact_match = response.xpath('.//div[@class="exact_block"]')

        representation = exact_match.xpath('.//div[@class="concept_light-representation"]')
        furigana = exact_match.xpath('.//span[@class="furigana"]//span').getall()
        kanji = exact_match.xpath('.//span[@class="text"]//text()').getall[:-1]

        hiragana_word = '' # Word without Kanji
        kanji_word = '' # Word with Kanji
        for f, k in zip(furigana, kanji):
            f, k = f.xpath('.//text()').get().split(), k.get().split()
            hiragana_word += f
            if k:
                kanji_word += k
            else:
                kanji_word += f
            pass

        definitions = exact_match.xpath('.//div[@class="meanings-wrapper"]')

        types_of_words = definitions.xpath('.//div[@class="meaning-tags"]')
        meanings = definitions.xpath('.//div[@class="meaning-wrapper"]')

        if len(types_of_words) != len(meanings):
            raise Exception("Number of types of words and meanings do not match")

        for word_type, meaning in zip(types_of_words, meanings):
            word_type = word_type.xpath('.//text()')
            meaning = meaning.xpath('.//span[@class="meaning-meaning"]//text()')

            if word_type == 'Other forms' or word_type == 'Notes':
                continue

            itemloader = ItemLoader(item=JishoWordItem(), response=response)
            itemloader.add_value("word_type", word_type.get())
            itemloader.add_value("meaning", meaning.get())
            yield itemloader.load_item()

        pass