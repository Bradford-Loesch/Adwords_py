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


    # feed_mapping_service = adwords_client.GetService('FeedMappingService', version='v201710')
    # feed_item_service = adwords_client.GetService('FeedItemService', version='v201710')

    campaign_service = adwords_client.GetService('CampaignService', 'v201806')

    PAGE_SIZE = 1
    campaigns = []
    more_pages = True

    selector = {
        'fields': ['Id', 'Name','Settings', 'AdvertisingChannelType' ],
        'predicates': [
            # {
            #     'field': 'Id',
            #     'operator': 'EQUALS',
            #     'values': [1419349875]
            # },
            # {
            #     'field': 'FeedId',
            #     'operator': 'IN',
            #     'values': [188002722]
            # },
            # {
            #     'field': 'PlaceholderTypes',
            #     'operator': 'CONTAINS_ANY',
            #     'values': [2]
            # }
        ],
        'paging': {
            'startIndex': 0,
            'numberResults': PAGE_SIZE
        }
    }

    while more_pages:
        page = campaign_service.get(selector)
        print(page['totalNumEntries'])

        if 'entries' in page:
            campaigns.extend(page['entries'])

        selector['paging']['startIndex'] += PAGE_SIZE
        more_pages = selector['paging']['startIndex'] < int(page['totalNumEntries'])

    print(campaigns)



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
