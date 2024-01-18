from playwright.async_api import async_playwright
import asyncio
import time

class Playwright:

    async def scrape(self, item):
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=False)
            page = await browser.new_page()
            await page.goto(f'https://jisho.org/search/{item}')
            await page.wait_for_timeout(1000)

            content = await page.content()

            word = page.get_by_text(item, exact=False).nth(3)
            furigana = page.locator(".furigana")

            translation = page.locator("meanings-wrapper")

            
            element = page.locator(".concept_light-representation > .text").first
            element = page.locator(".meaning-tags").first
            element = page.locator(".meaning-meaning").first
            time.sleep(500)
            await browser.close()

if __name__ == "__main__":
    pw = Playwright()
    asyncio.run(pw.scrape("行きます半袖"))