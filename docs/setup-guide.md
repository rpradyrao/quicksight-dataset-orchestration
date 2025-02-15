# Setup Guide

## Prerequisites
- AWS Account with QuickSight enabled
- QuickSight dataset ID
- IAM permissions to create:
  - Lambda functions
  - Step Functions state machine
  - IAM roles
  - CloudWatch alarms (optional)

## Deployment Options

### Option 1: AWS CloudFormation
1. Navigate to CloudFormation in AWS Console
2. Create new stack
3. Upload template: `src/cloudformation/template.yaml`
4. Fill in parameters:
   - AccountId: Your AWS account ID
   - DatasetId: Your QuickSight dataset ID

### Option 2: Manual Setup

#### Step 1: Lambda Functions
1. Create Initiator Lambda
   - Use code from: `src/lambda/initiator/index.py`
   - Python 3.9 runtime
   - Add QuickSight permissions

2. Create Status Checker Lambda
   - Use code from: `src/lambda/status_checker/index.py`
   - Python 3.9 runtime
   - Add QuickSight permissions

#### Step 2: Step Functions
1. Create state machine
   - Use definition from: `src/stepfunctions/state_machine.json`
   - Update Lambda ARNs in definition

## Testing

1. Test Lambda Functions:
```json
{
    "account_id": "YOUR_ACCOUNT_ID",
    "dataset_id": "YOUR_DATASET_ID"
}
