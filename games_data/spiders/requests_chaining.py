import scrapy
import json
from datetime import datetime
from games_data.items import GamesDataItem


class requests_chaining(scrapy.Spider):
    # requests chaining is too bad for scaling?
    name = 'requests_chaining'
    custom_settings = {
        'ITEM_PIPELINES': {
            'games_data.pipelines.RequestsChainingPipeline': 300
        }
    }

    def start_requests(self):
        urls_FYI = [
            'https://sensortower.com/api/ios/landing_page/report_card?app_id=553834731', # candycrushsaga
            'https://sensortower.com/api/ios/review/app_history_summary/?app_id=553834731', # candycrushsaga

            'https://sensortower.com/api/android/landing_page/report_card?app_id=com.king.candycrushsaga',
            'https://sensortower.com/api/android/review/app_history_summary/?app_id=com.king.candycrushsaga',

            'https://sensortower.com/api/ios/landing_page/report_card?app_id=1001250333', # StarTrekTimelines
            'https://sensortower.com/api/ios/review/app_history_summary/?app_id=1001250333' # StarTrekTimelines

            'https://sensortower.com/api/android/landing_page/report_card?app_id=com.disruptorbeam.StarTrekTimelines',
            'https://sensortower.com/api/android/review/app_history_summary/?app_id=com.disruptorbeam.StarTrekTimelines'
        ]

        yield scrapy.Request(
            url='https://sensortower.com/api/ios/landing_page/report_card?app_id=553834731',
            callback=self.candycrush_ios_card
        )

    def candycrush_ios_card(self, response):
        if (response.text):
            items_json = json.loads(response.text)

            candycrush_ios_item = GamesDataItem()
            candycrush_ios_item['game_name'] = 'Candy Crush Saga'
            candycrush_ios_item['platform'] = 'Android' if 'android' in response.url else 'iOS'
            candycrush_ios_item['date_scrapped'] = f'{datetime.now():%Y-%m-%d %H:%M:%S%z}'
            candycrush_ios_item['sensor_score'] = items_json['sensor_score']
            candycrush_ios_item['visibility'] = items_json['visibility_score']
            candycrush_ios_item['internationalization_score'] = items_json['internationalization_score']
            candycrush_ios_item['downloads'] = items_json['downloads']
            candycrush_ios_item['revenue'] = items_json['revenue']
            candycrush_ios_item['list_of_keywords'] = items_json['keywords']

            yield scrapy.Request(
                url='https://sensortower.com/api/ios/review/app_history_summary/?app_id=553834731',
                callback=self.candycrush_ios_history,
                meta={'candycrush_ios_item': candycrush_ios_item}
            )

    def candycrush_ios_history(self, response):
        if (response.text):
            items_json = json.loads(response.text)
            candycrush_ios_item = response.meta['candycrush_ios_item']
            candycrush_ios_item['review_breakdown'] = items_json['data']
            yield candycrush_ios_item

            yield scrapy.Request(
                url='https://sensortower.com/api/android/landing_page/report_card?app_id=com.king.candycrushsaga',
                callback=self.candycrush_android_card
            )

    def candycrush_android_card(self, response):
        if (response.text):
            items_json = json.loads(response.text)

            candycrush_android_item = GamesDataItem()
            candycrush_android_item['game_name'] = 'Candy Crush Saga'
            candycrush_android_item['platform'] = 'Android' if 'android' in response.url else 'iOS'
            candycrush_android_item['date_scrapped'] = f'{datetime.now():%Y-%m-%d %H:%M:%S%z}'
            candycrush_android_item['sensor_score'] = items_json['sensor_score']
            candycrush_android_item['visibility'] = items_json['visibility_score']
            candycrush_android_item['internationalization_score'] = items_json['internationalization_score']
            candycrush_android_item['downloads'] = items_json['downloads']
            candycrush_android_item['revenue'] = items_json['revenue']
            candycrush_android_item['list_of_keywords'] = items_json['keywords']

            yield scrapy.Request(
                url='https://sensortower.com/api/android/review/app_history_summary/?app_id=com.king.candycrushsaga',
                callback=self.candycrush_android_history,
                meta={'candycrush_android_item': candycrush_android_item}
            )

    def candycrush_android_history(self, response):
        if (response.text):
            items_json = json.loads(response.text)
            candycrush_android_item = response.meta['candycrush_android_item']
            candycrush_android_item['review_breakdown'] = items_json['data']
            yield candycrush_android_item

            yield scrapy.Request(
                url='https://sensortower.com/api/ios/landing_page/report_card?app_id=1001250333',
                callback=self.startrek_ios_card
            )

    def startrek_ios_card(self, response):
        if (response.text):
            items_json = json.loads(response.text)

            startrek_ios_item = GamesDataItem()
            startrek_ios_item['game_name'] = 'Star Trek Timelines'
            startrek_ios_item['platform'] = 'Android' if 'android' in response.url else 'iOS'
            startrek_ios_item['date_scrapped'] = f'{datetime.now():%Y-%m-%d %H:%M:%S%z}'
            startrek_ios_item['sensor_score'] = items_json['sensor_score']
            startrek_ios_item['visibility'] = items_json['visibility_score']
            startrek_ios_item['internationalization_score'] = items_json['internationalization_score']
            startrek_ios_item['downloads'] = items_json['downloads']
            startrek_ios_item['revenue'] = items_json['revenue']
            startrek_ios_item['list_of_keywords'] = items_json['keywords']

            yield scrapy.Request(
                url='https://sensortower.com/api/ios/review/app_history_summary/?app_id=1001250333',
                callback=self.startrek_ios_history,
                meta={'startrek_ios_item': startrek_ios_item}
            )

    def startrek_ios_history(self, response):
        if (response.text):
            items_json = json.loads(response.text)
            startrek_ios_item = response.meta['startrek_ios_item']
            startrek_ios_item['review_breakdown'] = items_json['data']
            yield startrek_ios_item

            yield scrapy.Request(
                url='https://sensortower.com/api/android/landing_page/report_card?app_id=com.disruptorbeam.StarTrekTimelines',
                callback=self.startrek_android_card
            )

    def startrek_android_card(self, response):
        if (response.text):
            items_json = json.loads(response.text)

            startrek_android_item = GamesDataItem()
            startrek_android_item['game_name'] = 'Star Trek Timelines'
            startrek_android_item['platform'] = 'Android' if 'android' in response.url else 'iOS'
            startrek_android_item['date_scrapped'] = f'{datetime.now():%Y-%m-%d %H:%M:%S%z}'
            startrek_android_item['sensor_score'] = items_json['sensor_score']
            startrek_android_item['visibility'] = items_json['visibility_score']
            startrek_android_item['internationalization_score'] = items_json['internationalization_score']
            startrek_android_item['downloads'] = items_json['downloads']
            startrek_android_item['revenue'] = items_json['revenue']
            startrek_android_item['list_of_keywords'] = items_json['keywords']

            yield scrapy.Request(
                url='https://sensortower.com/api/android/review/app_history_summary/?app_id=com.disruptorbeam.StarTrekTimelines',
                callback=self.startrek_android_history,
                meta={'startrek_android_item': startrek_android_item}
            )

    def startrek_android_history(self, response):
        if (response.text):
            items_json = json.loads(response.text)
            startrek_android_item = response.meta['startrek_android_item']
            startrek_android_item['review_breakdown'] = items_json['data']
            yield startrek_android_item