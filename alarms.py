import sys

from datetime import datetime

import boto3
import botocore
import click
import dateparser


def get_alarms(filters: dict) -> None:
    """Filter, fetch and display alarms from AWS"""
    try:
        # filter out None values, because paginate can't handle them
        filters = {k: v for k, v in filters.items() if v is not None}
        # instanciate client
        client = boto3.client("cloudwatch")
        # get paginator to iterate over
        paginator = client.get_paginator("describe_alarm_history")
        # filter results
        filtered_iterator = paginator.paginate(**filters)
        # loop through results and print them
        for page in filtered_iterator:
            for alarm in page["AlarmHistoryItems"]:
                print(alarm)
    except botocore.exceptions.NoCredentialsError:
        sys.exit((
            "Could not read AWS credentials from ~/.aws/credentials.",
            'Please use "aws configure" or provide them manually.',
        ))
    except botocore.exceptions.ClientError as msg:
        # The errormsg from botocore is already sufficient,
        # only hide the stacktrace from the user
        sys.exit(msg)


@click.command()
@click.option(
    "--name",
    "-n",
    help="Specific alarm name as shown in AWS console"
)
@click.option(
    "--alarm-types",
    "-a",
    multiple=True,
    help="Can be set multiple times. Value: 'CompositeAlarm'|'MetricAlarm'",
)
@click.option(
    "--item-type",
    "-i",
    help="'ConfigurationUpdate'|'StateUpdate'|'Action'"
)
@click.option(
    "--order",
    "-o",
    help="'TimestampDescending'|'TimestampAscending'"
)
@click.option("--start", "-s", help="Start date")
@click.option("--end", "-e", help="End date")
def main(
    name: str,
    alarm_types: list,
    item_type: str,
    start: str,
    end: str,
    order: str
) -> None:
    """CLI tool to display AWS Cloudwatch alarms"""
    # overcome too static date parsing of click
    if start:
        start = dateparser.parse(start)
    if end:
        end = dateparser.parse(end)

    get_alarms({
        "AlarmName": name,
        "AlarmTypes": alarm_types,
        "HistoryItemType": item_type,
        "StartDate": start,
        "EndDate": end,
        "ScanBy": order
    })


if __name__ == "__main__":
    main()
