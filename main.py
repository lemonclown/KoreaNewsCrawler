from korea_news_crawler.articlecrawler import ArticleCrawler

if __name__ == "__main__":
    crawler = ArticleCrawler()
    crawler.set_category("경제", "사회")
    crawler.set_date_range(2019,1,2019,1)
    crawler.start()