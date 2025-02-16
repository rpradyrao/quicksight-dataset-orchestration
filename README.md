# QuickSight Refresh Workflow

Amazon QuickSight's dataset refresh capabilities enable teams to maintain up-to-date business intelligence dashboards through scheduled refreshes and email notifications. However, modern data architectures often require advanced orchestration capabilities to automate and monitor these refresh operations across complex data workflows. Organizations frequently need to coordinate QuickSight dataset refreshes with broader data pipeline activities - such as initiating dependent transformations, synchronizing cross-account datasets, or integrating with existing monitoring systems.

Data teams implementing sophisticated refresh strategies typically require capabilities beyond standard QuickSight scheduling, including event-driven refreshes, programmatic monitoring, and granular refresh metrics. Common requirements include orchestrating sequential dataset refreshes, implementing custom retry logic, managing cross-account data synchronization, and integrating dataset refresh states with organizational monitoring solutions.

This article presents a sample cloud-native architectural pattern that leverages AWS Step Functions and AWS Lambda to implement QuickSight dataset refresh orchestration. The solution demonstrates how to build a serverless architecture that provides programmatic control over dataset refreshes while enabling comprehensive monitoring capabilities. By utilizing Step Functions' workflow management capabilities and Lambda's execution efficiency, the pattern enables reliable tracking and automated response handling for dataset refreshes at scale. The architecture can be extended to incorporate various AWS services such as AWS Glue, Amazon EventBridge, and custom Lambda functions to support complex data workflows. Teams can adapt this pattern to implement custom monitoring metrics, event-driven refresh triggers, and error handling mechanisms, providing a foundation for building resilient data pipeline orchestrations

The code in this repository helps you set up the following target architecture:

    

![QS_Orchestrate(3)](https://github.com/user-attachments/assets/abde5600-5f8b-48d7-8b51-79d1f2695d45)


    
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
