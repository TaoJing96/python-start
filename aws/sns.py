import boto3

client = boto3.client('sns', region_name='us-west-2', aws_access_key_id='AKIAQB2R3N2TVDTXDGFH',
    aws_secret_access_key= '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')

def pubish_sns(topic_arn, subject, msg):
    return client.publish(
                TopicArn=topic_arn,
                Subject=subject,
                Message=msg,
            )


if __name__ == '__main__':
    arn = 'arn:aws:sns:us-west-2:003929763495:tj-test'
    subject = 'tj-subject-02'
    msg = 'msg-02'
    print(pubish_sns(arn, subject, msg))