# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo
import json
import csv

class MongoDBCphonesPipeline:
    def __init__(self):
        # localhost
        self.client = pymongo.MongoClient('mongodb://localhost:27017/')
        self.db = self.client['CellPhoneS']
        self.collection =self.db['phones']
        pass

    def process_item(self, item, spider):
        try:
            self.collection.insert_one(dict(item))
            return item
        except Exception as e:
            raise DropItem(f"Error inserting item: {e}")
    
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