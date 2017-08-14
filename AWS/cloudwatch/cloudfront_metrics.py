import boto3
import datetime
import sys

region = 'us-east-1'


cw = boto3.client('cloudwatch', region_name = region)

#Checking the amounto of arguments used
if len(sys.argv) != 7:
	print "Some arguments are missing: python cloudwatch_metrics.py Namespace MetricName DimensionName DimensionValue Statistic period"
else: 
	namespace = sys.argv[1] # e.g. 'AWS/CloudFront'
	metricname = sys.argv[2] # e.g. Requests
	dimname = sys.argv[3] # e.g. DistributionId
	dimvalue = sys.argv[4] # e.g. ZONE
	statistic = sys.argv[5] # [ Sum, Maximum, Minimum, SampleCount, Average ]
	period = int(sys.argv[6]) # Period 1200
	try:
		print "AWS/CloudFront" "Requests" "DistributionId" "ZONE" "Sum"
		metric = cw.get_metric_statistics(
	        Namespace = namespace,
	        MetricName = metricname,
	        Dimensions = [
	        				{
	        					'Name': dimname,
	        			 		'Value': dimvalue
	        			 	},
	        			 	 { 'Name':'Region', 'Value':'Global'}

	        			 ],
	        # Statistic from de last period (variable) seconds.
	        StartTime = datetime.datetime.utcnow() - datetime.timedelta(seconds = period),
	        EndTime = datetime.datetime.utcnow(),
	        Period = 600,
	        Statistics = [statistic]	   
	    )
		#print datetime.datetime.utcnow()
		for data in metric['Datapoints']:
			print data[statistic]
	except Exception, e:
		print e
	