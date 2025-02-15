# QuickSight Refresh Workflow

While Amazon QuickSight provides email notifications for dataset refresh failures, teams often need programmatic control over QuickSight dataset refresh for automation and monitoring purposes. Additionally, data teams frequently need to trigger downstream actions based on refresh states - such as initiating dependent data pipelines upon successful refresh, email notifications, triggering retry mechanisms on failures, or updating other systems about the refresh status. The lack of out-of-the-box programmatic monitoring capabilities makes it challenging for teams to integrate QuickSight dataset refreshes into their automated data workflows and orchestrate dependent processes effectively.

This cloud-native pattern implements a monitoring solution using AWS Step Functions to orchestrate the refresh workflow. The solution combines Step Functions' long-running workflow capabilities with AWS Lambda's execution efficiency to create a scalable, serverless architecture that can monitor dataset refreshes indefinitely. By separating the refresh initiation and status monitoring into distinct Lambda functions, the pattern provides reliable tracking and automated response capabilities for dataset refreshes across multiple QuickSight datasets and AWS accounts. The pattern delivers a workflow that extends QuickSight's native capabilities with programmatic control and integration options, ensuring reliable dataset refresh monitoring for organizations of any scale.

The code in this repository helps you set up the following target architecture:

    
![QS_Orchestrate(1)](https://github.com/user-attachments/assets/964cd654-6ef9-4d1e-9933-f2017b674a3d)


    
Components

    Amazon EventBridge (Refresh Scheduler)
    AWS Step Functions (Dataset Refresh Flow)
    AWS Lambda (Refresh Initiator & Status Checker Functions)
    Amazon QuickSight (Dataset)
    Amazon CloudWatch (Execution Logs & Alarms)
    Amazon SNS (Refresh Notifications)

Repository Structure

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
│   │   │   └── requirements.txt
│   │   └── status_checker/
│   │       ├── index.py
│   │       └── requirements.txt
│   │
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
    ├── testing.md
    └── images/
        └── architecture.png

```
