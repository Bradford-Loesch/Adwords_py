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

def getCMCDReport(client_customer_id, refresh_token):
    print("dowloading yesterday's CMCD Report" )

    oauth2_client = oauth2.GoogleRefreshTokenClient(CLIENT_ID, CLIENT_SECRET, refresh_token)

    try:
        adwords_client = adwords.AdWordsClient(
            DEVELOPER_TOKEN, oauth2_client, USER_AGENT, client_customer_id=client_customer_id)
    except:
        print('Oauth error for %s' % client_customer_id)
        traceback.print_exc()
        return None

    report_downloader = adwords_client.GetReportDownloader(version=ADWORDS_API_VERSION)

    print('past report downloader')
    report = {
        'reportName': 'CALL METRICS CALL DETAILS REPORT',
        'dateRangeType': 'TODAY',
        'reportType': 'CALL_METRICS_CALL_DETAILS_REPORT',
        'downloadFormat': 'XML',
        'selector': {
            'fields': ['AccountDescriptiveName','AccountTimeZone', 'AdGroupId', 'AdGroupName', 'CampaignId', 'CampaignName', 'CallDuration', 'CallStartTime',
                        'CallEndTime', 'CallerNationalDesignatedCode', 'CallType', ]
        }
    }

    report_downloader.DownloadReport(
      report, sys.stdout, skip_report_header=False, skip_column_header=False,
      skip_report_summary=False)

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

    getCMCDReport(id, token)


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
