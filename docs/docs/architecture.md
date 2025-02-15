```markdown
# Architecture Overview

## Components

### 1. EventBridge (Trigger)
- Schedules workflow execution
- Passes dataset and account parameters

### 2. Step Functions Workflow
- Orchestrates the refresh process
- Handles state management
- Implements retry logic
- Manages timeouts

### 3. Lambda Functions
#### Initiator Lambda
- Starts QuickSight dataset ingestion
- Generates unique ingestion ID
- Returns initial status

#### Status Checker Lambda
- Monitors ingestion progress
- Retrieves detailed status
- Reports success/failure

### 4. QuickSight Dataset
- Target of refresh operation
- Provides status via API

### 5. CloudWatch
- Logs execution details
- Triggers alarms on failures
- Enables monitoring

### 6. SNS
- Sends notifications
- Enables external integrations

## Flow Diagram
![QS_Orchestrate(1)](https://github.com/user-attachments/assets/d10432b9-68c5-4329-b545-0e1cad045017)



## Design Considerations

1. **Reliability**
   - Automatic retries
   - Error handling
   - State persistence

2. **Scalability**
   - Serverless architecture
   - Concurrent executions
   - Resource optimization

3. **Security**
   - IAM roles and policies
   - Cross-account access
   - Audit logging

4. **Monitoring**
   - Execution tracking
   - Error reporting
   - Performance metrics
