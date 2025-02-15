import boto3
import json
import uuid
from typing import Dict, Any
from botocore.exceptions import ClientError

def lambda_handler(event: Dict[str, Any], context) -> Dict[str, Any]:
    """
    Initiates a QuickSight dataset ingestion
    """
    try:
        # Extract parameters from the event
        account_id = event['account_id']
        dataset_id = event['dataset_id']
        
        # Initialize QuickSight client
        quicksight = boto3.client('quicksight')
        
        # Generate unique ingestion ID
        ingestion_id = str(uuid.uuid4())
        
        # Initiate dataset ingestion
        response = quicksight.create_ingestion(
            DataSetId=dataset_id,
            IngestionId=ingestion_id,
            AwsAccountId=account_id
        )
        
        # Return success response
        return {
            'statusCode': 200,
            'body': {
                'message': 'Dataset ingestion initiated successfully',
                'account_id': account_id,
                'dataset_id': dataset_id,
                'ingestion_id': ingestion_id,
                'ingestion_status': response['IngestionStatus'],
                'aws_request_id': context.aws_request_id
            }
        }
        
        
    except Exception as e:
        # Handle unexpected errors
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
