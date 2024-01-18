import scrapy


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
        furigana = exact_match.xpath('.//span[@class="furigana"]')
        kanji = exact_match.xpath('.//span[@class="text"]')

        for f, k in zip(furigana, kanji):

            yield {
                "furigana": f.get(),
                "kanji": k.get(),
            }

        definitions = exact_match.xpath('.//div[@class="meanings-wrapper"]')

        types_of_words = definitions.xpath('.//div[@class="meaning-tags"]')
        meanings = definitions.xpath('.//div[@class="meaning-wrapper"]')

        if len(types_of_words) != len(meanings):
            raise Exception("Number of types of words and meanings do not match")

        for word_type, meaning in zip(types_of_words, meanings):
            word_type = word_type.xpath('.//text()')
            meaning = meaning.xpath('.//span[@class="meaning-meaning"]//text()')

            yield {
                "word_type": word_type.get(),
                "meaning": meaning.get(),
            }

        pass