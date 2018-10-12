from googleads import adwords
from googleads import oauth2
import configparser
import traceback
import sys
import argparse

CLIENT_ID = ''
# adwords secret
CLIENT_SECRET = ''
# adwords developer token
DEVELOPER_TOKEN = ''
# static user agent used to identify our conversion requests
USER_AGENT = ''
# API release version for adwords
ADWORDS_API_VERSION = ''

def feedItems(client_customer_id, refresh_token):
    oauth2_client = oauth2.GoogleRefreshTokenClient(CLIENT_ID, CLIENT_SECRET, refresh_token)

    try:
        adwords_client = adwords.AdWordsClient(
            DEVELOPER_TOKEN, oauth2_client, USER_AGENT, client_customer_id=client_customer_id)
    except:
        print('Oauth error for %s' % client_customer_id)
        traceback.print_exc()
        return None

    feed_service = adwords_client.GetService('FeedService', version='v201806')
    feed_mapping_service = adwords_client.GetService('FeedMappingService', version='v201806')
    feed_item_service = adwords_client.GetService('FeedItemService', version='v201806')

    feed_selector = {
        'fields': ['Id', 'Name'],
        'predicates': [
            # {
            #   'field': 'Origin',
            #   'operator': 'NOT_IN',
            #   'values': ['ADWORDS']
            # },
            {
              'field': 'FeedStatus',
              'operator': 'IN',
              'values': ['ENABLED']
            }
        ]
    }

    # itemSelector = {
    #     'fields': [
    #         'AttributeValues',
    #         'FeedId',
    #         'FeedItemId',
    #         'Status',
    #         'TargetingCampaignId',
    #         'TargetingAdGroupId'
    #     ],
    #     'predicates': [
    #         {
    #           'field': 'Status',
    #           'operator': 'EQUALS',
    #           'values': ['ENABLED']
    #         },
    #         {
    #           'field': 'FeedId',
    #           'operator': 'IN',
    #           'values': [75151834]
    #         }
    #     ]
    # }


    # feed_item = {
    #     'feedItemId': 37733926609,
    #     'feedId': 1734030
    # }

    # feed_item_operation = {
    #     'operator': 'REMOVE',
    #     'operand': feed_item
    # }
    response = feed_service.get(feed_selector)
    print(response)
    # feed_ids = []
    # for entry in response['entries']:
    #     feed_ids.append(entry['id'])

    # mapping_selector = {
    #     'fields': [
    #         'AttributeFieldMappings',
    #         'CriterionType',
    #         'FeedId',
    #         'FeedMappingId',
    #         'PlaceholderType',
    #         'Status'
    #     ],
    #     'predicates': [
    #         {
    #             'field': 'PlaceholderType',
    #             'operator': 'EQUALS',
    #             'values': 2
    #         },
    #         {
    #             'field': 'FeedId',
    #             'operator': 'IN',
    #             'values': feed_ids
    #         }
    #     ]
    # }

    # # response = feed_item_service.get(itemSelector)

    # response = feed_mapping_service.get(mapping_selector)
    # print(response)

    # new_feed_ids = []
    # for entry in response['entries']:
    #     new_feed_ids.append(entry['feedId'])
    # print(new_feed_ids)

    # itemSelector = {
    #     'fields': [
    #         'AttributeValues',
    #         'FeedId',
    #         'FeedItemId',
    #         'Status',
    #         'TargetingCampaignId',
    #         'TargetingAdGroupId'
    #     ],
    #     'predicates': [
    #         {
    #           'field': 'Status',
    #           'operator': 'EQUALS',
    #           'values': ['ENABLED']
    #         },
    #         {
    #           'field': 'FeedId',
    #           'operator': 'IN',
    #           'values': new_feed_ids
    #         }
    #     ]
    # }

    # response = feed_item_service.get(itemSelector)
    # print(response)



def main(id, token, env = 'dev'):
    config = configparser.ConfigParser()
    config.read("config.ini")

    global CLIENT_ID
    global CLIENT_SECRET
    global DEVELOPER_TOKEN
    global USER_AGENT
    global ADWORDS_API_VERSION

    CLIENT_ID               = config.get(env, 'CLIENT_ID')
    CLIENT_SECRET           = config.get(env, 'CLIENT_SECRET')
    DEVELOPER_TOKEN         = config.get(env, 'DEVELOPER_TOKEN')
    USER_AGENT              = config.get(env, 'USER_AGENT')
    ADWORDS_API_VERSION     = config.get(env, 'ADWORDS_API_VERSION')

    feedItems(id, token)


if __name__ == '__main__':
    # Get Acct ID
    parser = argparse.ArgumentParser(
        description='something completely different'
    )
    parser.add_argument(
        'env',
        type=str,
        help='''
            Environment for deployment
            '''
    )
    parser.add_argument(
        'client_customer_id',
        type=str,
        help='''
            client customer id
            '''
    )
    parser.add_argument(
        'refresh_token',
        type=str,
        help='''
            Refresh token
            '''
    )

    args = parser.parse_args()

    main(args.client_customer_id, args.refresh_token, args.env)
