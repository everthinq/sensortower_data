# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json


class RequestsChainingPipeline:
    def process_item(self, item, spider):
        print('RequestsChainingPipeline')
        return item


class PostProcessingPipeline:
    def process_item(self, item, spider):
        print('PostProcessingPipeline')
        return item
