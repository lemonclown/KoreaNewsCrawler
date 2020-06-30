import mysql.connector

class DBManager(object):

    def __init__(self, username, password, database, host='127.0.0.1'):
        self.cnx = mysql.connector.connect(user=username, password=password,
                                           host=host,
                                           database=database)

    def insert_news(self, category, company, headline, content, content_url, news_date):
        params = locals()
        del params['self']
        query = ("INSERT INTO news (category, company, headline, content, url, date) "
                "VALUES (%(category)s, %(company)s, %(headline)s, %(content)s, %(content_url)s, %(news_date)s) ")
        cursor = self.cnx.cursor()
        try:
            cursor.execute(query, params)
            self.cnx.commit()
        except Exception as e:
            print(e)

    def insert_urls(self, urls, category):
        if len(urls) == 0:
            return
        query = ("INSERT INTO news_urls (category, url) "
                "VALUES ")
        query += ','.join([f'({category},{url})' for url in urls])
        cursor = self.cnx.cursor()
        try:
            cursor.execute(query)
            self.cnx.commit()
        except Exception as e:
            print(e)

    def select_url(self, url):
        params = locals()
        del params['self']
        query = ("SELECT count(*) FROM news WHERE url=%(url)s")
        cursor = self.cnx.cursor()
        try:
            cursor.execute(query, params)
            res = cursor.fetchall()
            return int(res[0][0])
        except Exception as e:
            print(e)
