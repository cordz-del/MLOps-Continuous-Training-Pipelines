# cloudwatch_monitoring.py
import boto3
import time

def send_metric(namespace, metric_name, value):
    client = boto3.client('cloudwatch', region_name='us-east-1')
    client.put_metric_data(
        Namespace=namespace,
        MetricData=[
            {
                'MetricName': metric_name,
                'Timestamp': time.gmtime(),
                'Value': value,
                'Unit': 'Count'
            },
        ]
    )

if __name__ == "__main__":
    # Example: Report number of processed logs
    send_metric("AIModel/Metrics", "ProcessedLogs", 100)
    print("Metric sent to CloudWatch.")
