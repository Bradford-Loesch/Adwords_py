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

    customer_service = adwords_client.GetService('CustomerService', version=ADWORDS_API_VERSION)
    managed_customer_service = adwords_client.GetService('ManagedCustomerService', version=ADWORDS_API_VERSION)

    selector = {
        'fields': ['CustomerId', 'CanManageClients'],
    }

    customers = customer_service.getCustomers()
    print('from customer service')
    print(customers)
    for customer in customers:
        if customer['customerId'] == int(client_customer_id):
            print('hi alex')
        else:
            print(type(customer['customerId']))
            print(customer['customerId'])
            print('vs')
            print(type(client_customer_id))
            print(client_customer_id)

    #     print customer
    # print '\n'

    print('from managed customer service')
    page = managed_customer_service.get(selector)
    print(page)
    # if 'entries' in page and page['entries']:
    #     for customer in page['entries']:
    #         print customer
    # else:
    #     print 'why?'

    # Construct selector to get all accounts.
    # offset = 0
    # selector = {
    #     'fields': ['CustomerId', 'Name'],
    #     'paging': {
    #         'startIndex': str(offset),
    #         'numberResults': str(10)
    #     }
    # }
    # more_pages = True
    # accounts = {}
    # child_links = {}
    # parent_links = {}
    # root_account = None

    # while more_pages:
    #     # Get serviced account graph.
    #     page = managed_customer_service.get(selector)
    #     if 'entries' in page and page['entries']:
    #         # Create map from customerId to parent and child links.
    #         if 'links' in page:
    #             for link in page['links']:
    #                 if link['managerCustomerId'] not in child_links:
    #                     child_links[link['managerCustomerId']] = []
    #                 child_links[link['managerCustomerId']].append(link)
    #                 if link['clientCustomerId'] not in parent_links:
    #                     parent_links[link['clientCustomerId']] = []
    #                 parent_links[link['clientCustomerId']].append(link)
    #         # Map from customerID to account.
    #         for account in page['entries']:
    #             accounts[account['customerId']] = account
    #     offset += 10
    #     selector['paging']['startIndex'] = str(offset)
    #     more_pages = offset < int(page['totalNumEntries'])

    # # Find the root account.
    # for customer_id in accounts:
    #     if customer_id not in parent_links:
    #         root_account = accounts[customer_id]

    # # Display account tree.
    # if root_account:
    #     print 'CustomerId, Name'
    #     DisplayAccountTree(root_account, accounts, child_links, 0)
    # else:
    #     print 'Unable to determine a root account'



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
