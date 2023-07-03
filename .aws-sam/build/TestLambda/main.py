import os


def lambda_handler(event, context):
    print("Event", event)
    print("ls in efs before", os.listdir('/mnt/efs'))
    os.mkdir('/mnt/efs/temp')
    print("ls in efs after", os.listdir('/mnt/efs'))
    return {
            'statusCode': 200,
            'body': 'Function executed successfully'
            }

