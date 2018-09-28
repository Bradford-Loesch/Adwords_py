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

# def DisplayAccountTree(account, accounts, links, depth=0):
#   """Displays an account tree.
#   Args:
#     account: dict The account to display.
#     accounts: dict Map from customerId to account.
#     links: dict Map from customerId to child links.
#     depth: int Depth of the current account in the tree.
#   """
#   prefix = '-' * depth * 2
#   print '%s%s, %s' % (prefix, account['customerId'], account['name'])
#   if account['customerId'] in links:
#     for child_link in links[account['customerId']]:
#       child_account = accounts[child_link['clientCustomerId']]
#       DisplayAccountTree(child_account, accounts, links, depth + 1)

def getManagedCustomer(client_customer_id, refresh_token):
    oauth2_client = oauth2.GoogleRefreshTokenClient(CLIENT_ID, CLIENT_SECRET, refresh_token)

    try:
        adwords_client = adwords.AdWordsClient(
            DEVELOPER_TOKEN, oauth2_client, USER_AGENT, client_customer_id=client_customer_id)
    except:
        print('Oauth error for %s' % client_customer_id)
        traceback.print_exc()
        return None

    criterion_service = adwords_client.GetService('AdGroupCriterionService', version=ADWORDS_API_VERSION)


    selector = {
        'fields': ['KeywordText', 'Id', 'KeywordMatchType', 'CriteriaType'],
        'predicates': [{
            'field': 'AdGroupId',
            'operator': 'IN',
            'values': [21902709882]
        },
        {'field': 'CriteriaType',
              'operator': 'NOT_IN',
              'values': ['USER_LIST','USER_INTEREST','PRODUCT_PARTITION' ]}
    ]
    }

    result = criterion_service.get(selector)

    print(result)


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

    getManagedCustomer(id, token)


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
        type=str,
        help='''
            Environment for deployment
            '''
    )
    parser.add_argument(
        'refresh_token',
        type=str,
        help='''
            Environment for deployment
            '''
    )

    args = parser.parse_args()

    main(args.client_customer_id, args.refresh_token, args.env)
