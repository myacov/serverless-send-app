import boto3

ses = boto3.client('ses')
def lambda_handler(event, context):
    ses.send_email(
        Source = 'medinayacov@gmail.com',
        Destination = {
            'ToAddresses': [
                event['destinationEmail'],
            ]
        },
        Message = {
            'Subject': {
                'Data': 'This is a message'
            },
            'Body': {
                'Text': {
                    'Data': event['message']
                }
            }
        }
    )
    return 'Email sent!'
