# AWS Cloudwatch alarm cli display

A simple cli tool which displays AWS Cloudwatch alarms

## Prequisites

AWS credentials must be stored in `~/.aws/credentials`.

You can use `aws configure` to do so or find more info [here](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/setup-credentials.html).

Also, you user need to have at least `CloudWatchReadOnlyAccess` rights.

## Installation

`pip install git+https://github.com/c4tz/aws-cloudwatch-alarms.git`

## Usage

All arguments are optional, so the most simple usage would be:
```bash
alarms
```
but there are several ways to filter the alarms, a full-blown call would look like this:

```bash
alarms --name SOMEALARM --alarm-types CompositeAlarm --alarm-types MetricAlarm --item-type StateUpdate --start "yesterday" --end "-3 hours" --order TimestampAscending
```

for more information on each argument, please see
```bash
alarms --help
```
