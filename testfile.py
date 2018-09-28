from __future__ import print_function

entries  = [{
  'feedId': 32226171,
  'campaignId': 1055844607,
  'matchingFunction': {
    'operator': 'EQUALS',
    'lhsOperand': [
      {
        'FunctionArgumentOperand.Type': 'RequestContextOperand',
        'contextType': 'FEED_ITEM_ID'
      }
    ],
    'rhsOperand': [
      {
        'FunctionArgumentOperand.Type': 'ConstantOperand',
        'type': 'LONG',
        'unit': 'NONE',
        'longValue': 3037906008,
        'booleanValue': None,
        'doubleValue': None,
        'stringValue': None
      }
    ],
    'functionString': 'EQUALS(FEED_ITEM_ID,3037906008)'
  },
  'placeholderTypes': [
    2
  ],
  'status': 'ENABLED',
  'baseCampaignId': None
}, {
  'feedId': 32226171,
  'campaignId': 1356323449,
  'matchingFunction': {
    'operator': 'IDENTITY',
    'lhsOperand': [
      {
        'FunctionArgumentOperand.Type': 'ConstantOperand',
        'type': 'BOOLEAN',
        'unit': 'NONE',
        'longValue': None,
        'booleanValue': False,
        'doubleValue': None,
        'stringValue': None
      }
    ],
    'rhsOperand': [],
    'functionString': 'IDENTITY(false)'
  },
  'placeholderTypes': [
    2
  ],
  'status': 'ENABLED',
  'baseCampaignId': None
}, {
  'feedId': 827834,
  'campaignId': 179858354,
  'matchingFunction': {
    'operator': 'IN',
    'lhsOperand': [
      {
        'FunctionArgumentOperand.Type': 'RequestContextOperand',
        'contextType': 'FEED_ITEM_ID'
      }
    ],
    'rhsOperand': [
      {
        'FunctionArgumentOperand.Type': 'ConstantOperand',
        'type': 'LONG',
        'unit': 'NONE',
        'longValue': 9494990274,
        'booleanValue': None,
        'doubleValue': None,
        'stringValue': None
      },
      {
        'FunctionArgumentOperand.Type': 'ConstantOperand',
        'type': 'LONG',
        'unit': 'NONE',
        'longValue': 9498233077,
        'booleanValue': None,
        'doubleValue': None,
        'stringValue': None
      }
    ],
    'functionString': 'IN(FEED_ITEM_ID,{9494990274,9498233077})'
  },
  'placeholderTypes': [
    2
  ],
  'status': 'ENABLED',
  'baseCampaignId': None
}, {
  'feedId': 827834,
  'campaignId': 124457594,
  'matchingFunction': {
    'operator': 'AND',
    'lhsOperand': [
      {
        'FunctionArgumentOperand.Type': 'FunctionOperand',
        'value': {
          'operator': 'EQUALS',
          'lhsOperand': [
            {
              'FunctionArgumentOperand.Type': 'RequestContextOperand',
              'contextType': 'FEED_ITEM_ID'
            }
          ],
          'rhsOperand': [
            {
              'FunctionArgumentOperand.Type': 'ConstantOperand',
              'type': 'LONG',
              'unit': 'NONE',
              'longValue': 4903034,
              'booleanValue': None,
              'doubleValue': None,
              'stringValue': None
            }
          ],
          'functionString': 'EQUALS(FEED_ITEM_ID,4903034)'
        }
      },
      {
        'FunctionArgumentOperand.Type': 'FunctionOperand',
        'value': {
          'operator': 'EQUALS',
          'lhsOperand': [
            {
              'FunctionArgumentOperand.Type': 'RequestContextOperand',
              'contextType': 'DEVICE_PLATFORM'
            }
          ],
          'rhsOperand': [
            {
              'FunctionArgumentOperand.Type': 'ConstantOperand',
              'type': 'STRING',
              'unit': 'NONE',
              'longValue': None,
              'booleanValue': None,
              'doubleValue': None,
              'stringValue': 'Mobile'
            }
          ],
          'functionString': 'EQUALS(CONTEXT.DEVICE,"Mobile")'
        }
      }
    ],
    'rhsOperand': [],
    'functionString': 'AND(EQUALS(FEED_ITEM_ID,4903034),EQUALS(CONTEXT.DEVICE,"Mobile"))'
  },
  'placeholderTypes': [
    2
  ],
  'status': 'ENABLED',
  'baseCampaignId': None
}, {
  'feedId': 827834,
  'campaignId': 180296714,
  'matchingFunction': {
    'operator': 'IN',
    'lhsOperand': [
      {
        'FunctionArgumentOperand.Type': 'RequestContextOperand',
        'contextType': 'FEED_ITEM_ID'
      }
    ],
    'rhsOperand': [
      {
        'FunctionArgumentOperand.Type': 'ConstantOperand',
        'type': 'LONG',
        'unit': 'NONE',
        'longValue': 116818634,
        'booleanValue': None,
        'doubleValue': None,
        'stringValue': None
      },
      {
        'FunctionArgumentOperand.Type': 'ConstantOperand',
        'type': 'LONG',
        'unit': 'NONE',
        'longValue': 116818994,
        'booleanValue': None,
        'doubleValue': None,
        'stringValue': None
      }
    ],
    'functionString': 'IN(FEED_ITEM_ID,{116818634,116818994})'
  },
  'placeholderTypes': [
    2
  ],
  'status': 'ENABLED',
  'baseCampaignId': None
}, {
  'feedId': 827834,
  'campaignId': 319218314,
  'matchingFunction': {
    'operator': 'IN',
    'lhsOperand': [
      {
        'FunctionArgumentOperand.Type': 'RequestContextOperand',
        'contextType': 'FEED_ITEM_ID'
      }
    ],
    'rhsOperand': [
      {
        'FunctionArgumentOperand.Type': 'ConstantOperand',
        'type': 'LONG',
        'unit': 'NONE',
        'longValue': 116818634,
        'booleanValue': None,
        'doubleValue': None,
        'stringValue': None
      },
      {
        'FunctionArgumentOperand.Type': 'ConstantOperand',
        'type': 'LONG',
        'unit': 'NONE',
        'longValue': 116818994,
        'booleanValue': None,
        'doubleValue': None,
        'stringValue': None
      }
    ],
    'functionString': 'IN(FEED_ITEM_ID,{116818634,116818994})'
  },
  'placeholderTypes': [
    2
  ],
  'status': 'ENABLED',
  'baseCampaignId': None
}]

def getFeedItems(entry):
    '''
    Gets feed Item Ids from matching functions
    '''
    feedItemIds = []
    operator = entry['operator']
    if operator == 'EQUALS' or operator == 'IN':
        if len(entry['lhsOperand']) == 1:
            operandType = entry['lhsOperand'][0]['FunctionArgumentOperand.Type']
            lhType = entry['lhsOperand'][0]['contextType']
            if operandType == 'RequestContextOperand' and lhType == 'FEED_ITEM_ID':
                for item in entry['rhsOperand']:
                    feedItemIds.append(item['longValue'])
                return feedItemIds
    elif operator == 'AND':
        for left in entry['lhsOperand']:
            if left['FunctionArgumentOperand.Type'] == 'FunctionOperand':
                feedItemIds.extend(getFeedItems(left['value']))
        return feedItemIds
    return feedItemIds

formattedResponse = {}
for entry in entries:
    values = getFeedItems(entry['matchingFunction'])
    linkId = entry['campaignId']
    for value in values:
      if value in formattedResponse:
          formattedResponse[value].append(linkId)
      else:
          formattedResponse[value] = [linkId]

print(formattedResponse)
