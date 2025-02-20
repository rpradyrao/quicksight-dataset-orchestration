# QuickSight Refresh Workflow

Amazon QuickSight's dataset refresh capabilities enable teams to maintain up-to-date business intelligence dashboards through scheduled refreshes and email notifications. However, modern data architectures often require advanced orchestration capabilities to automate and monitor these refresh operations across complex data workflows. Organizations frequently need to coordinate QuickSight dataset refreshes with broader data pipeline activities - such as initiating dependent transformations, synchronizing cross-account datasets, or integrating with existing monitoring systems.

Data teams implementing sophisticated refresh strategies typically require capabilities beyond standard QuickSight scheduling, including event-driven refreshes, programmatic monitoring, and granular refresh metrics. Common requirements include orchestrating sequential dataset refreshes, implementing custom retry logic, managing cross-account data synchronization, and integrating dataset refresh states with organizational monitoring solutions.

This article presents a sample cloud-native architectural pattern that leverages AWS Step Functions and AWS Lambda to implement QuickSight dataset refresh orchestration. The solution demonstrates how to build a serverless architecture that provides programmatic control over dataset refreshes while enabling comprehensive monitoring capabilities. By utilizing Step Functions' workflow management capabilities and Lambda's execution efficiency, the pattern enables reliable tracking and automated response handling for dataset refreshes at scale. The architecture can be extended to incorporate various AWS services such as AWS Glue, Amazon EventBridge, and custom Lambda functions to support complex data workflows. Teams can adapt this pattern to implement custom monitoring metrics, event-driven refresh triggers, and error handling mechanisms, providing a foundation for building resilient data pipeline orchestrations

The code in this repository helps you set up the following target architecture:

    

![QS_Orchestrate(3)](https://github.com/user-attachments/assets/abde5600-5f8b-48d7-8b51-79d1f2695d45)

1. Scheduler → Step Function

    EventBridge triggers Step Functions state machine execution
    
    Passes dataset_id and account_id as parameters
    
    Scheduled or on-demand trigger

2. Step Function → Lambda 1 (Refresh Initiator)

    Step Functions invokes Refresh Initiator Lambda
    
    Passes input parameters from scheduler
    
    Initiates workflow execution

3. Lambda 1 → QuickSight Dataset

    Lambda calls QuickSight API (refresh_dataset)
    
    Starts asynchronous dataset refresh
    
    Returns refresh initiation status

4. Step Function ⇄ Lambda 2 (Status Checker)

    Step Functions invokes Status Checker Lambda
    
    Lambda returns refresh status to Step Functions
    
    Repeated checks based on workflow configuration

5. Continues until success/failure/timeout

    Lambda 2 ⇄ QuickSight Dataset
    
    Lambda polls QuickSight API (describe_data_set_refresh_properties)
    
    Retrieves current refresh status
    
    Reports status back to workflow

6. Lambda & Step Function → CloudWatch

    Both services automatically log to CloudWatch
    
    Captures execution details, errors, and statuses
    
    Enables monitoring and troubleshooting

7. CloudWatch → SNS

    CloudWatch Alarm monitors for specific conditions
    
    Triggers SNS notification when conditions met
    
    Delivers success/failure notifications to subscribers

### Workflow Visualizations:

The workflow consists of the following states:
1. **InitiateIngestion**: Triggers the dataset refresh
2. **WaitForIngestion**: Waits for 60 seconds
3. **CheckIngestionStatus**: Polls for refresh status
4. **EvaluateStatus**: Makes decisions based on status
5. **IngestionSucceeded/Failed**: Terminal states


![Screenshot 2025-02-13 at 9 22 36 AM](https://github.com/user-attachments/assets/a9e0a959-6d18-4cea-acc6-1b1baacbe0f1)

    
### Components

    Amazon EventBridge (Refresh Scheduler)
    AWS Step Functions (Dataset Refresh Flow)
    AWS Lambda (Refresh Initiator & Status Checker Functions)
    Amazon QuickSight (Dataset)
    Amazon CloudWatch (Execution Logs & Alarms)
    Amazon SNS (Refresh Notifications)

### Repository Structure

```    
quicksight-refresh-workflow/
├── LICENSE
├── README.md
├── CONTRIBUTING.md
├── .gitignore
│
├── src/
│   ├── lambda/
│   │   ├── initiator/
│   │   │   ├── index.py
│   │   └── status_checker/
│   │       ├── index.py
│   ├── stepfunctions/
│   │   └── state_machine.json
│   │
│   └── cloudformation/
│       └── template.yaml
│
├── tests/
│   ├── events/
│      ├── initiator_event.json
│      ├── status_checker_event.json
│      ├── step_functions_input.json
│      ├── sample_responses.json
│
└── docs/
    ├── setup-guide.md
    ├── architecture.md  

```
