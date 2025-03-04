# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo
import json
import csv
import os

class MongoDBCphonesPipeline:
    def __init__(self):
        # Đọc thông tin kết nối MongoDB từ biến môi trường
        mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
        mongo_db = os.getenv("MONGO_DATABASE", "CellPhoneS")

        self.client = pymongo.MongoClient(mongo_uri)
        self.db = self.client[mongo_db]
        self.collection = self.db["phones"]

    def process_item(self, item, spider):
        try:
            self.collection.insert_one(dict(item))
            return item
        except Exception as e:
            print(f"Error inserting item: {e}")
            return None
        pass

class JsonDBCphonesPipeline:
    def __init__(self):
        self.data = []
    
    def process_item(self, item, spider):
        self.data.append(dict(item))
        return item
    
    def open_spider(self, spider):
        self.file = open('jsondatacphones.json', 'w', encoding='utf-8')

    def close_spider(self, spider):
        json.dump(self.data, self.file, ensure_ascii=False, indent=4)
        self.file.close()

class CSVDBUnitopPipeline:
     def process_item(self, item, spider):
        with open('phonedata.csv', 'a', encoding='utf-8', newline='') as file:
            writer = csv.writer(file, delimiter='$')
            writer.writerow([
                item['phoneUrl'],
                item['name'],
                item['upgrade_price'],
                item['price'],
                item['contain'],
                item['description'],
                item['highlight'],
            ])
        return item
     pass