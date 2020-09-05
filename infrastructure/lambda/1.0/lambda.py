import boto3
import os

table_name = os.environ["TABLE_NAME"]

my_session = boto3.session.Session()
my_region = my_session.region_name
dynamodb_client = boto3.client("dynamodb", region_name=my_region)


def query_dynamo(table_name):
    response = dynamodb_client.query(
        TableName=table_name,
        KeyConditionExpression=f"Who = :who AND Website = :website",
        ExpressionAttributeValues={
            ":who": {"S": "Austin Engle"},
            ":website": {"S": "resume"},
        },
    )
    # make sure we get at least 1 back
    value = response["Count"]

    if value != 0:
        viewcount = response["Items"][0]["viewcount"]["N"]

        return viewcount

    else:
        return None


def insert_website_data(table_name, view_count):
    response = dynamodb_client.put_item(
        TableName=table_name,
        Item={
            "Who": {"S": "Austin Engle"},
            "Website": {"S": "resume"},
            "viewcount": {"N": str(view_count)},
        },
    )
    # make sure response is a good response before returning True
    if response:
        return True
    return False


def update_website_view(table_name, updated_view_count):
    response = dynamodb_client.update_item(
        TableName=table_name,
        Key={"Who": {"S": "Austin Engle"}, "Website": {"S": "resume"},},
        UpdateExpression="Set viewcount = :viewcount",
        ExpressionAttributeValues={":viewcount": {"N": str(updated_view_count)},},
    )
    if response:
        return True
    return False


def handler(event, context):
    try:
        # Query dbTable to see if there is a viewcount history
        view_count = query_dynamo(table_name)
    except:
        print(f"Unable to find data on website in {table_name}")
        # since we were unable to find the data we assume this is the first time and there isn't a view count.
        # Setting view count as 1 and writting to the DynamoDB table
        view_count = 1
        insert_data = insert_website_data(table_name, view_count)

        if insert_data is True:
            print("Successfully updated dynamo with new viewcount")
            # If we inserted data successfully then exit script and return view_count
            return view_count

        else:
            raise ValueError(f"Unable to update DynamoDB table with new information")

    print(f"Current View Count: {view_count}")
    updated_view_count = int(view_count) + 1
    print(f"Updated View Count: {updated_view_count}")

    # write updated view count to dbTable
    response = update_website_view(table_name, updated_view_count)

    return updated_view_count
