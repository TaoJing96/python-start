#! /usr/bin/env python
# coding=utf-8

import boto3
import json

messages = [
    {
        "name": "alan",
        "age": 25
    },
    {
        "name": "ayun",
        "age": 18
    },
]

queue_name = "tj-test"

receipt_handles = []


def run():
    # init sqs
    # if (raw_input("init sqs: [y/n]") != 'y'):
    #     return
    session_args = {}  # Found credentials in shared credentials file: ~/.aws/credentials
    # session_args = {'profile_name': 'alan'}
    session_args = {
     'aws_access_key_id': 'AKIAQB2R3N2TVDTXDGFH',
     'aws_secret_access_key': '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',
    }
    session = boto3.session.Session(**session_args)
    sqs = session.resource('sqs', region_name='us-west-2')
    # sqs = session.resource('sqs', region_name='cn-northwest-1', endpoint_url='https://xxx.xxx.com')

    # list queues
    # if (raw_input("list queues: [y/n]") != 'y'):
    #     return
    queues = [q.url for q in sqs.queues.all()]
    for q in queues:
        print(q)
    #
    # # create queue
    # # if (raw_input("create queue: [y/n]") != 'y'):
    # #     return
    # attributes = {
    #     'DelaySeconds': '0',
    #     'VisibilityTimeout': '18000',
    #     'MessageRetentionPeriod': '1209600'
    # }
    # queue = sqs.create_queue(QueueName=queue_name, Attributes=attributes, tags={'Owner': 'alan'})
    # queue_url = sqs.get_queue_by_name(QueueName=queue_name).url
    # print(queue_url)  # https://cn-northwest-1.queue.amazonaws.com.cn/111222333444/alan_test
    #
    # # send message
    # if (raw_input("send message: [y/n]") != 'y'):
    #     return
    # queue = sqs.get_queue_by_name(QueueName=queue_name)
    # for msg in messages:
    #     response = queue.send_message(MessageBody=json.dumps(msg))
    #
    # # batch send message
    # if (raw_input("batch send message: [y/n]") != 'y'):
    #     return
    # entries = [{'Id': str(idx),
    #             'MessageBody': json.dumps(msg)}
    #            for idx, msg in enumerate(messages)]
    # sqs_client = boto3.client('sqs', region_name='cn-northwest-1')
    # response = sqs_client.send_message_batch(QueueUrl=queue_url, Entries=entries)
    #
    # # read message
    # if (raw_input("read message: [y/n]") != 'y'):
    #     return
    queue = sqs.get_queue_by_name(QueueName=queue_name)
    while True:
        msgs = queue.receive_messages(MaxNumberOfMessages=10, MessageAttributeNames=['All'])
        if len(msgs) == 0:
            break
        msg = msgs[0]
        msg_body = json.loads(msg.body)
        receipt_handle = msg.receipt_handle
        print(json.dumps(msg_body, indent=2))
        receipt_handles.append(receipt_handle)
    #
    # # delete message
    # if (raw_input("delete message: [y/n]") != 'y'):
    #     return
    # entries = [{'Id': str(idx), 'ReceiptHandle': rh}
    #            for idx, rh in enumerate(receipt_handles)]
    # queue.delete_messages(QueueUrl=queue_url, Entries=entries)
    # for rh in receipt_handles:
    #     print('deleted message: %s', rh[:30])
    #
    # # delete queue
    # if (raw_input("delete queue: [y/n]") != 'y'):
    #     return
    # sqs.meta.client.delete_queue(QueueUrl=queue_url)


if __name__ == '__main__':
    run()