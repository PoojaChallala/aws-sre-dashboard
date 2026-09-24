AWS Fault-Tolerant Application

A fault-tolerant Flask web application deployed on AWS that demonstrates automatic recovery from EC2 instance failures using an Application Load Balancer and Auto Scaling. 

OVERVIEW

This project demonstrates how to deploy a Python Flask application on AWS with infrastructure designed to automatically recovery when an EC2 instance becomes unavailable. 

This application runs inside a Docker container on an EC2 instance. An Application Load Balancer distributes incoming HTTP traffic to the application, while an Auto Scaling Group monitors the EC2 environment and automatically launches a replacement instance when an existing instance is terminated or becomes unhealthy. 

The goal of the project was to build a simple, working example of cloud fault and automated recovery. 

FAULT-TOLERANCE DEMONSTRATION
1. A flask application runs inside a Docker container on an EC2 instance. 
2. The EC2 instance is registered with the Application Load Balancer's target group. 
3. The load balancer performs health checks to determine whether the application is healthy
4. The EC2 instance can be manually terminated to simulate an infrastructure failure.
5. The Auto Scaling Group detects that the desired capacity is no longer available. 
6. AWS automatically launches a replacement EC2 instance.
7. The new instance is registered with the target group after passing health checks. 
8. Application traffic can then be routed to the replacement instance.

APPLICATION

The flask application provides a lightweight monitoring dashboard displaying application-level metrics including: 
- Request count
- Response time
- Error count
- Application uptime

The dashboard provides a simple interface for observing the application while the underlying AWS infrastructure handles instance availability and recovery. 