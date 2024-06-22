import json
import requests


def lambda_handler(event, context):
    print("Event Data", event)
    print("Trigger Received")
    print("context", context)
    a = 2
    b = 3
    print("sum of a and b is = ", a + b)

    # # ToDo implement
    # return {
    #    'statusCode': 200,
    #    'body': json.dumps('Bye Bye !!'),
    #    'print': json.dumps(response.text)
    # }

    print("Event Data -->   ", event)
    response = requests.get("https://www.google.co.in/")
    print(response.text)
    return response.text
