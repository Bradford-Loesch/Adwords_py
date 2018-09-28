from googleads import adwords
from googleads import oauth2
import re
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

def getBetaInfo(client_customer_id, refresh_token, acct_id, numbers):

    oauth2_client = oauth2.GoogleRefreshTokenClient(CLIENT_ID, CLIENT_SECRET, refresh_token)

    try:
        adwords_client = adwords.AdWordsClient(
            DEVELOPER_TOKEN, oauth2_client, USER_AGENT, client_customer_id=client_customer_id)
    except:
        print('Oauth error for %s' % client_customer_id)
        traceback.print_exc()
        return None

    # get the correct feed
    feed_service = adwords_client.GetService('FeedService', version='v201710')
    feed_selector = {
        'fields': ['Attributes', 'FeedStatus', 'Id', 'Name', 'Origin', 'SystemFeedGenerationData'],
        'predicates': [
            {
              'field': 'Name',
              'operator': 'IN',
              'values': ['Main phone number feed', 'Main call feed']
            },
        ]
    }
    page = feed_service.get(feed_selector)
    feed = page['entries'][0]
    feed_id = feed['id']

    # get the feed items (call extensions)
    feed_item_service = adwords_client.GetService('FeedItemService', version='v201710')
    itemSelector = {
        'fields': [
            'AttributeValues',
            'FeedId',
            'FeedItemId',
            'Status',
            'Scheduling',
            'TargetingCampaignId',
            'TargetingAdGroupId'
        ],
        'predicates': [
            {
              'field': 'Status',
              'operator': 'EQUALS',
              'values': ['ENABLED']
            },
            {
              'field': 'FeedId',
              'operator': 'IN',
              'values': [feed_id]
            }
        ]
    }

    feed_item_pages = feed_item_service.get(itemSelector)
    feed_items = feed_item_pages['entries']
    print(feed_items)
    extensions = []
    for feed_item in feed_items:
        for att in feed_item['attributeValues']:
            if att['feedAttributeId'] == 1:
                number = re.sub('[^\d]','', att['stringValue'])
                if int(number) in numbers:
                    # grab all call extensions
                    extensions.append(
                        {
                            'phone_number': number,
                            'acct_id': acct_id,
                            'client_customer_id': client_customer_id,
                            'feed_id': feed_id,
                            'feed_item_id': feed_item['feedItemId']
                        }
                    )
    # now that we have all call extensions we need to insert data into the relevant tables
    # for now lets just print it so we can manually insert
    print(extensions)



    # print(feed_items)



def main(id, token, acct_id, env = 'dev', numbers = []):
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

    getBetaInfo(id, token, acct_id, numbers)


if __name__ == '__main__':
    # Get Acct ID
    parser = argparse.ArgumentParser(
        description='Dialogtech CDR Docstore population'
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
        type=int,
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

    parser.add_argument(
        'acct_id',
        type=int,
        help='''
            DT Account Id for this accountd
            '''
    )

    parser.add_argument(
        'numbers',
        type=int,
        nargs=argparse.REMAINDER,
        help='''
            list of phone numbers for created call extensions
            '''
    )

    args = parser.parse_args()

    main(args.client_customer_id, args.refresh_token, args.acct_id, args.env, numbers=args.numbers)
