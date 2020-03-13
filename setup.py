from setuptools import setup

setup(
    name="aws-cloudwatch-alarms",
    version="0.0.1",
    description="A simple cli tool which displays AWS Cloudwatch alarms",
    author="c4tz",
    entry_points={
        "console_scripts": ["alarms = alarms:main"]
    },
    packages=["."],
    install_requires=[
        "boto3==1.12.20",
        "click==7.1.1",
        "dateparser==0.7.4"
    ],
)
