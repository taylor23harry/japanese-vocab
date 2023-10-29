import scrapy


class JishoSpider(scrapy.Spider):
    name = "jisho"
    allowed_domains = ["jisho.org"]

    def start_requests(self):
        vocab = "行きます半袖"
        if type(vocab) == str:
            base_url = 'https://jisho.org/search/'
            url = base_url + vocab
            yield scrapy.Request(url=url)
        else: raise Exception(f"Vocab parameter not a string: {type(vocab)}")

    def parse(self, response):
        with open("response.html", "w") as file:
            file.write(response.body.decode())

        selector = scrapy.Selector(response)
        furigana_words = {}
        words = selector.xpath('.//li[contains(@class, "japanese_word")]')
        for word in words:
            word_type = word.attrib['data-pos']
            furiganas = word.xpath('.//span[contains(@class, "japanese_word__furigana_wrapper")]')
            word_texts = word.xpath('.//span[contains(@class, "japanese_word__text_wrapper")]')
            
            for furigana, word_text in furiganas, word_texts:
                furigana_words[furigana] = word_text
                furigana_words[]

            for furigana in furiganas:
                print(furigana)
        furigana = selector.xpath('//*[@id="primary"]/div[1]/div/div[1]/div[1]/div/span[1]/span[1]/text()').get()
        pass