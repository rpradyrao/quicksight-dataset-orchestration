import boto3
import json
from typing import Dict, Any
from botocore.exceptions import ClientError

def lambda_handler(event: Dict[str, Any], context) -> Dict[str, Any]:
    """
    Checks most recent QuickSight dataset ingestion status
    """
    try:
        # Extract parameters from the event
        account_id = event['account_id']
        dataset_id = event['dataset_id']
        
        # Initialize QuickSight client
        quicksight = boto3.client('quicksight')
        
        # Get list of ingestions (most recent first)
        list_response = quicksight.list_ingestions(
            DataSetId=dataset_id,
            AwsAccountId=account_id,
            MaxResults=1  # We only need the most recent
        )
        
        if not list_response['Ingestions']:
            return {
                'statusCode': 404,
                'body': {
                    'message': 'No ingestions found for dataset',
                    'account_id': account_id,
                    'dataset_id': dataset_id,
                    'aws_request_id': context.aws_request_id
                }
            }
            
        most_recent_ingestion = list_response['Ingestions'][0]
        ingestion_id = most_recent_ingestion['IngestionId']
        
        # Get detailed status
        response = quicksight.describe_ingestion(
            DataSetId=dataset_id,
            IngestionId=ingestion_id,
            AwsAccountId=account_id
        )
        
        ingestion_status = response['Ingestion']['IngestionStatus']
        
        return {
            'statusCode': 200,
            'body': {
                'account_id': account_id,
                'dataset_id': dataset_id,
                'ingestion_id': ingestion_id,
                'ingestion_status': ingestion_status,
                'status': 'IN_PROGRESS' if ingestion_status == 'RUNNING' else ingestion_status,
                'error_info': response['Ingestion'].get('ErrorInfo', None),
                'row_info': response['Ingestion'].get('RowInfo', None),
                'queued_time': str(response['Ingestion'].get('QueuedTime')),
                'ingestion_time_in_seconds': response['Ingestion'].get('IngestionTimeInSeconds'),
                'aws_request_id': context.aws_request_id
            }
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'body': {
                'error': 'Internal Error',
                'message': str(e),
                'account_id': account_id,
                'dataset_id': dataset_id,
                'aws_request_id': context.aws_request_id
            }
        }
