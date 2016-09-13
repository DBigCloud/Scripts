import boto3
import datetime
import sys

region = 'eu-west-1'
period = 300

cw = boto3.client('cloudwatch', region_name = region)

#Checking the amount of arguments used
if len(sys.argv) != 6:
	print "Some arguments are missing: python cloudwatch_metrics.py Namespace MetricName DimensionName DimensionValue Statistic"
else: 
	namespace = sys.argv[1] # e.g. 'AWS/RDS'
	metricname = sys.argv[2] # e.g. CPUUtilization
	dimname = sys.argv[3] # e.g. DBInstanceIdentifier
	dimvalue = sys.argv[4] # e.g. MyDB
	statistic = sys.argv[5] # [ Sum, Maximum, Minimum, SampleCount, Average ]
	try:
		metric = cw.get_metric_statistics(
	        Namespace = namespace,
	        MetricName = metricname,
	        Dimensions = [
	        				{
	        					'Name': dimname,
	        			 		'Value': dimvalue
	        			 	}

	        			 ],
	        # Statistic from de last period (variable) seconds.
	        StartTime = datetime.datetime.utcnow() - datetime.timedelta(seconds = period),
	        EndTime = datetime.datetime.utcnow(),
	        Period = period,
	        Statistics = [statistic]
	   )
		#print datetime.datetime.utcnow()
		for data in metric['Datapoints']:
			print data[statistic]
	except Exception, e:
		print e
