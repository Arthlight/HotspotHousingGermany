# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import _sqlite3

class FlatCrawlerScrapyPipeline():

    def __init__(self):
        self.establish_connection()
        self.create_db_table()

    def establish_connection(self):
        self.conn = _sqlite3.connect('flat_data.db')
        self.cursor = self.conn.cursor()

    def create_db_table(self):
        self.cursor.execute('''DROP TABLE IF EXISTS flat_data''')
        self.cursor.execute('''CREATE TABLE flat_data(
                            price text,
                            sqm text,
                            street text,
                            area text,
                            city text,
                            rooms text,
                            detail_view_url text
                            )
                            ''')

    def process_item(self, item, spider):
        self.store_in_db(item)
        return item

    def store_in_db(self, item):
        self.cursor.execute('''INSERT INTO flat_data VALUES (?, ?, ?, ?, ?, ?, ?)''', (
            item['price'],
            item['sqm'],
            item['street'],
            item['area'],
            item['city'],
            item['rooms'],
            item['detail_view_url'],
        ))
        self.conn.commit()
