# Instructions

#### Copy both files to /usr/lib/zabbix/externalscripts/
```
git clone https://github.com/DBigCloud/Scripts
cp AWS/cloudwatch/* /usr/lib/zabbix/externalscripts/
```

#### In Zabbix, create a Item, type external check, in key field call the cloudwatch_metrics.sh script.
```
cloudwatch_metrics.sh["AWS/NameSpace", "Latency", "ApiName", "NAME", "Average"]
```
#### Parameters list
	- namespace  # e.g. 'AWS/RDS'
	- metricname # e.g. CPUUtilization
	- dimname # e.g. DBInstanceIdentifier
	- dimvalue # e.g. MyDB
	- statistic # [ Sum, Maximum, Minimum, SampleCount, Average ]

