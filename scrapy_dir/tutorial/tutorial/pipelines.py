# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import csv

class MoviePipeline():

    def __init__(self):
        self.csvwriter = csv.writer(open("MovieInfo.csv", "w", newline=''))
        self.csvwriter.writerow(["Movie Titles"])

    def process_item(self, item, spider):
        row = []
        row.append(item["title"])

        self.csvwriter.writerow(row)

        return item

    def close_spider(self, spider):
        print("Done")
