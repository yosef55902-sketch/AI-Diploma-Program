# Course 05 - Course Summary
## ملخص الدورة

This document provides a comprehensive text summary of all course materials.
هذا المستند يوفر ملخص نصي شامل لجميع مواد الدورة.

---


## Pptx Files



### 01

--- Slide 1 ---

أكـــــاديميــــة طــــويـــق
Scalable Data Science

--- Slide 2 ---

Automated Workflows in the Cloud
By: Dr. Afshan Hashmi

--- Slide 3 ---

Course Objectives:
Define cloud automation and its key components.
Design workflows using serverless architectures (e.g., AWS Step Functions, Azure Logic Apps).
Implement CI/CD pipelines for ML models in the cloud.
Automate data processing with cloud-native tools (e.g., Airflow, Lambda).
Evaluate cost/performance tradeoffs in workflow automation.

--- Slide 4 ---

Introduction to Automation in the Cloud
What are Automated Workflows?
Automated workflows are sequences of tasks and processes that are triggered and executed automatically using predefined rules or events in cloud environments.
They eliminate the need for manual intervention and enhance efficiency, scalability, and reliability.
Cloud Automation refers to the use of technology (scripts, tools, or services) to perform tasks in cloud environments automatically, with minimal or no human involvement.
Purpose of Cloud Automation:
Reduce Human Error
Automated systems follow exact instructions every time eliminating mistakes that can happen with manual tasks.
Save Time
Tasks like server setup, deployments, or monitoring can be completed in seconds or scheduled regularly.
Improve Scalability & Response Time
Automatically adjust resources (like adding more servers) based on demand, ensuring smooth performance.

--- Slide 5 ---

Common Examples:
Note: Tools like AWS CloudFormation, Terraform, Ansible, 
and CI/CD pipelines (Jenkins, GitHub Actions) play key roles in automating cloud environments.

--- Slide 6 ---

Key Components of Cloud Automation
These components work together to automate tasks in a cloud environment  like an intelligent to-do list that runs itself based on events and conditions.

1. Triggers: Events that start an automated workflow.
Example: A new file uploaded to cloud storage (like Google Drive or AWS S3) could trigger a workflow to process it.

2. Actions: The specific tasks performed automatically when a trigger occurs.
Example: After a file is uploaded, an email is sent or a backup is created.

3. Conditions: Logic or rules that determine whether certain actions should be executed.
Example: If the uploaded file is a PDF, then process it; otherwise, ignore it.

--- Slide 7 ---

Key Components of Cloud Automation
4. APIs & Connectors: Interfaces that connect different services and tools.
Example: Connecting Google Sheets to Slack or AWS to GitHub using REST APIs, webhooks, or prebuilt connectors.
5. Orchestration: The coordination of multiple actions across different systems in a defined sequence.
Example:After code is committed → test the code → deploy it → notify the team.
Putting It All Together:
Imagine this automated workflow:
Trigger: New file uploaded to Dropbox
Condition: File is a .csv
Action 1: Parse and analyze the file
Action 2: Upload results to Google Sheets
Action 3: Send summary via email
All coordinated through orchestration

--- Slide 8 ---

Tools for Automating Workflows in the Cloud
Cloud providers like AWS, Azure, and GCP offer a variety of tools to automate tasks, respond to events, and orchestrate services all without manual intervention.
Amazon Web Services (AWS)

--- Slide 9 ---

Tools for Automating Workflows in the Cloud
Microsoft Azure

--- Slide 10 ---

Tools for Automating Workflows in the Cloud
Google Cloud Platform (GCP)

--- Slide 11 ---

Real-World Examples of Cloud Automation
These examples show how cloud automation can simplify repetitive or time-sensitive tasks across different platforms.
Example 1: Daily File Backup
Trigger:Time-based — scheduled every day at 8 PM
Action:Automatically copy a file or database from the production environment to a backup storage location
Tools Used:
AWS Lambda – Executes the backup logic
S3 – Stores the backup
CloudWatch – Triggers Lambda on a schedule
 This helps ensure that data is regularly backed up without needing a person to do it manually.

--- Slide 12 ---

Real-World Examples of Cloud Automation
Example 2: Slack Notification for New GitHub Issue

Trigger:A new issue is opened on a GitHub repository
Action:Automatically send a message to a specific Slack channel with details of the new issue
 Tools Used:
Zapier (no-code)
Or Azure Logic Apps (workflow builder)
Or GCP Workflows for developers
 This keeps your team in the loop in real time without constantly checking GitHub.

--- Slide 13 ---

Real-World Examples of Cloud Automation
Example 3: Auto-Scaling EC2 Instances

Trigger:When CPU usage > 80% on current EC2 instances
Action:Automatically launch a new EC2 instance to handle the load
Tools Used:
AWS Auto Scaling – Adjusts the number of instances
CloudWatch Alarms – Monitors CPU usage and triggers scaling
This ensures performance under heavy load while saving costs when usage drops.

--- Slide 14 ---

Hands-On Exercise: Notify via Email When a File is Uploaded
Platform: AWS
Scenario Flow
File UploadA user uploads a file to an Amazon S3 bucket.
Trigger LambdaThe file upload triggers an AWS Lambda function through an S3 event.
Send Email NotificationThe Lambda function uses AWS SNS (Simple Notification Service) to send an email alert.

--- Slide 15 ---

Hands-On Exercise: Notify via Email When a File is Uploaded
import json
import boto3
def lambda_handler(event, context):
    # Get uploaded file name from the S3 event
    s3_info = event['Records'][0]['s3']['object']['key']
    
    # Create an SNS client
    sns = boto3.client('sns')
    
    # Send an email via SNS
    sns.publish(
        TopicArn='arn:aws:sns:region:acct-id:topic',  # Replace with your SNS topic ARN
        Message=f'New file uploaded: {s3_info}',
        Subject='Upload Notification'
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Notification sent!')
    }

--- Slide 16 ---

Hands-On Exercise: Notify via Email When a File is Uploaded
Explanation of Key Parts

--- Slide 17 ---

Best Practices for Automated Workflows
These practices ensure your automated workflows are secure, maintainable, and reliable.
Use Environment Variables

What it means: Instead of hardcoding sensitive data (like API keys, database URIs, file paths), use environment variables.

B. Why it matters:
Keeps your code cleaner
Makes deployments more flexible across dev, staging, and production
Enhances security by avoiding hardcoded secrets

Example: Instead of writing db_password = 'abc123', store it in os.environ['DB_PASSWORD'].

--- Slide 18 ---

Best Practices for Automated Workflows
2. Limit Permissions (Least-Privilege Principle)
What it means: Give your automation only the minimum permissions it needs to function.
Why it matters:
Reduces risk if a service or script is compromised
Prevents accidental changes to critical resources
Example: A Lambda function that only reads from S3 should not have write or delete permissions.

3. Monitor & Log All Actions
What it means: Track workflow actions and issues through logging and monitoring services.
Why it matters:
Helps in debugging and auditing
Ensures visibility into system health and workflow status
Tools:
AWS: CloudWatch
GCP: Stackdriver
Azure: Application Insights

--- Slide 19 ---

Best Practices for Automated Workflows
4. Integrate Error Handling
What it means: Plan for failures by writing code that can catch and handle errors gracefully.
Why it matters:
Avoids broken workflows and silent failures
Enables retries or alerts when something goes wrong
Example: Use try-except blocks in Python Lambda functions to catch API failures and log them or trigger alerts.

5. Modularize Logic
What it means: Break your workflows into small, reusable modules or steps.
Why it matters:
Easier to debug, test, and maintain
Encourages reusability of logic across multiple workflows
Example: Instead of one large function, have separate ones for validation, transformation, and sending data.

--- Slide 20 ---

Best Practices for Automated Workflows

--- Slide 21 ---

Summary
Cloud-based automated workflows help execute tasks like backups, notifications, and deployments without manual intervention.
Triggers (e.g., file upload, scheduled time) initiate actions such as sending emails or scaling infrastructure.
Common cloud services for automation include AWS Lambda, Azure Logic Apps, and Google Cloud Functions.
These workflows can connect multiple cloud services using APIs or orchestration tools like AWS Step Functions or GCP Workflows.
Automation improves efficiency, reduces human error, and ensures consistency across processes.
Best practices include setting up monitoring, logging, error handling, and using the principle of least privilege for security.
Tools like Zapier and IFTTT offer no-code automation for connecting third-party services easily.

--- Slide 22 ---

Reading and Resources
AWS Docs: https://docs.aws.amazon.com/lambda
Azure Logic Apps: https://learn.microsoft.com/en-us/azure/logic-apps
GCP Workflows: https://cloud.google.com/workflows/docs
Automate.io and Zapier (No-code tools)
"Cloud Automation Cookbook" by Nikit Swaraj (Packt)
YouTube: Cloud Academy, AWS Tutorials, Microsoft Learn

--- Slide 23 ---

الشراكات العالمية

--- Slide 24 ---

شــــــكــــرًا لكــــــم
THANK YOU

### 02

--- Slide 1 ---

أكـــــاديميــــة طــــويـــق
Scalable Data Science

--- Slide 2 ---

Cloud Collaboration Tools
By: Dr. Afshan Hashmi

--- Slide 3 ---

Course Objectives:
Understand what cloud collaboration tools are and why they are important.
Identify popular cloud collaboration platforms and their core features.
Compare different tools based on functionality, accessibility, and security.
Demonstrate the use of common cloud collaboration tools through practical examples.

--- Slide 4 ---

Introduction to Cloud Collaboration
What is Cloud Collaboration?
Cloud Collaboration refers to the practice of using cloud computing technologies that allow multiple people to:
Work together on documents, files, or projects
Access and edit content in real-time
From anywhere with an internet connection
Instead of storing files on a local device, cloud collaboration platforms store them on remote servers (the cloud), making it easy for teams to collaborate even if they are not in the same location.
Key Features of Cloud Collaboration:
Real-time Editing: Multiple users can edit the same document at the same time.
Automatic Saving & Versioning: Changes are saved automatically, and previous versions are often stored.
Remote Access: Files can be accessed anytime, anywhere.
File Sharing: Easy to share with teams or external stakeholders.
Integrated Communication: Chat, comments, and video calls often integrated into the tools.

--- Slide 5 ---

Why Use Cloud Collaboration Tools?
1. Supports Remote and Hybrid Work Models
With more people working from home or from different locations, cloud tools ensure everyone stays connected and productive.
2. Facilitates Teamwork Across Geographic Boundaries
Teams in different cities or countries can collaborate as if they were in the same room.
3. Enhances Productivity and Communication
Instant updates and seamless communication reduce misunderstandings and improve workflow.
Saves time no need to send files back and forth by email.

Examples of Cloud Collaboration Tools:
Google Workspace (Docs, Sheets, Drive)
Microsoft 365 (Word Online, OneDrive, Teams)
Slack with file sharing
Trello / Asana for task management
Zoom / Microsoft Teams for meetings and screen sharing

--- Slide 6 ---

Key Features of Cloud Collaboration Tools
Real-time Editing
Multiple users can edit the same document or file at the same time.
Changes appear instantly for everyone.
Example: Google Docs lets your team write, edit, and see updates live.
Version Control
Keeps a history of all changes made to a document.
You can track who edited what and when.
Option to revert to previous versions if needed.
 File Sharing
Share files securely with team members or external collaborators.
Set permissions: view-only, comment, or edit.
No need to email attachments just share a link.

--- Slide 7 ---

Key Features of Cloud Collaboration Tools
Commenting & Feedback
Leave inline comments directly on documents.
Tag teammates using @mention to notify them.
Makes feedback clear, organized, and action-oriented.
Integration
Works smoothly with other tools like:
Calendars (e.g., Google Calendar)
Project management (e.g., Trello, Asana)
Communication apps (e.g., Slack, Microsoft Teams)
Keeps everything connected in one place.
Security
Strong protection through:
User permissions (who can see or edit)
Access control (limit by team, device, or IP)
Data encryption (to keep content private and secure)

--- Slide 8 ---

Common Cloud Collaboration Tools
Cloud collaboration tools help teams work together in real time, share files, manage tasks, and communicate effectively especially in remote or hybrid work environments.
Here are some of the most widely used tools categorized by function:
1. Document Creation & File Sharing
Google Workspace
Includes: Google Docs, Sheets, Slides, and Drive.
Real-time editing, comments, version history.
Ideal for document collaboration and storage.
Microsoft 365
Includes: Word Online, Excel Online, PowerPoint, OneDrive.
Integrates with Microsoft Teams for smooth collaboration.
Strong enterprise-level support.
Dropbox
File storage and sharing platform.
Integrates with third-party apps for collaboration.
Good version control and file recovery.

--- Slide 9 ---

Common Cloud Collaboration Tools
Communication & Messaging
Slack
Team messaging app with channels and direct messages.
File sharing and integration with tools like Google Drive and Trello.
Real-time collaboration and notification system.
Microsoft Teams
Combines chat, video calls, file sharing, and collaboration in one place.
Deeply integrated with Microsoft 365.
Useful for team meetings and document co-authoring.
Zoom
Video conferencing and screen sharing.
Useful for online meetings, webinars, and virtual classes.
Can be integrated with other collaboration tools.

--- Slide 10 ---

Common Cloud Collaboration Tools
Project & Task Management
Trello
Visual task management using boards, lists, and cards.
Great for small teams and simple project tracking.
Easy drag-and-drop interface.
Asana
Task and project management tool.
Lets you assign tasks, set due dates, and track progress.
Integrates with email, Slack, Google Drive, etc.
ClickUp / Monday.com
All-in-one workspaces for tasks, docs, goals, and timelines.
Highly customizable workflows for teams.

--- Slide 11 ---

Common Cloud Collaboration Tools
Integrated Platforms
Notion
Combines note-taking, docs, databases, and task tracking.
Customizable and great for team knowledge bases.
Real-time collaboration with rich media support.
Airtable
Like a super-powered spreadsheet.
Combines database features with a user-friendly interface.
Good for project planning and content calendars.

--- Slide 12 ---

Common Cloud Collaboration Tools

--- Slide 13 ---

Key Technologies Behind Cloud Collaboration
These are the core technologies that make cloud collaboration fast, secure, and seamless.
 A. Real-Time Sync
Cloud collaboration tools rely on real-time synchronization to ensure all users see the same version of a document instantly.
Operational Transformation (OT)
A method used to resolve conflicts when multiple users are editing a document at the same time.
It ensures that all changes are merged smoothly, so nothing is overwritten.
Example: Google Docs uses OT to let multiple users type on the same document without issues.
WebSockets
A communication protocol that keeps a constant connection between the user’s device and the server.
Allows instant updates to be sent in both directions no need to refresh the page.
Used in live chats, collaborative editing, dashboards, etc.

--- Slide 14 ---

Key Technologies Behind Cloud Collaboration
B. Security & Compliance
Since cloud collaboration involves storing and transferring sensitive data, security is critical.
 Encryption
AES-256 (Advanced Encryption Standard) is used to protect data at rest (stored data).
TLS (Transport Layer Security) protects data in transit (data being transferred between devices and servers).
Access Controls
Tools implement Role-Based Access Control (RBAC):
Admin – full control
Editor – can modify content
Viewer – read-only access
Ensures only the right people can see or edit data.
Compliance Standards
Tools often follow global standards to protect user privacy and data:
GDPR – for data protection in the EU
HIPAA – for health-related data security in the U.S.
SOC 2 – for service organization controls (audits, privacy, etc.)

--- Slide 15 ---

Key Technologies Behind Cloud Collaboration
C. APIs & Integrations
APIs and integrations help cloud tools communicate with each other, improving efficiency and automation.
REST APIs (Representational State Transfer)
Allow external apps or systems to connect and exchange data.
Example: Connect Slack with Google Calendar to get meeting reminders in Slack.
Webhooks
Used to send real-time alerts between systems when certain events happen.
Example: A new issue is created in GitHub → a message is sent to your Slack channel automatically.

--- Slide 16 ---

Challenges and Considerations in Cloud Collaboration
While cloud collaboration tools offer many benefits, there are some challenges that teams and organizations must address:
1. Security Risks
What it is: Data stored in the cloud can be vulnerable to unauthorized access, breaches, or leaks.
Why it matters: Sensitive company or customer information may be exposed if proper security measures (like encryption and access control) aren't in place.
Example: Sharing a file with the wrong permissions can lead to accidental exposure.

2. Internet Dependency
What it is: Cloud tools rely heavily on internet connectivity.
Why it matters: If the internet is slow or unavailable, users may lose access to critical documents or live collaboration features.
Example: During a meeting, poor internet can disrupt file sharing or real-time updates.

--- Slide 17 ---

Challenges and Considerations in Cloud Collaboration
3. Compatibility Issues
What it is: Different tools or file formats might not work well together.
Why it matters: Users may face difficulties when collaborating across platforms or with older file versions.
Example: A document made in Microsoft Word might lose formatting when opened in Google Docs.

4. User Training
What it is: Employees may need to learn how to use new tools or adapt to cloud-based workflows.
Why it matters: Without proper training, productivity may drop, and users may resist adopting new systems.
Example: A team used to emailing files may take time to adjust to using shared online documents.

--- Slide 18 ---

Best Practices for Effective Collaboration
Effective collaboration using cloud tools requires not just the right platform, but also smart practices to ensure productivity, security, and alignment. Below are key best practices every team should follow:

1. Standardize Tools
Why it matters: Using too many tools creates confusion, duplicate work, and inefficiencies.
Best practice:
Choose one tool per function (e.g., only Asana or Trello for project management).
Establish an official toolset for communication, file storage, task tracking, etc.
Example: Use Google Workspace + Trello + Slack for your team, and ensure everyone sticks to them.

--- Slide 19 ---

Best Practices for Effective Collaboration
2. Set Permissions
Why it matters: Accidental edits or unauthorized access to sensitive data can be costly.
Best practice:
Set view-only, comment, or edit permissions based on role and responsibility.
Use folder-level controls in tools like Google Drive or OneDrive.
Example: Project plans can be editable by managers, while interns get view-only access.
3. Train Teams
Why it matters: Many powerful features go unused due to lack of knowledge.
Best practice:
Provide hands-on training or short video tutorials.
Highlight features like:
@mentions for collaboration,
Version history to recover previous work,
Shortcuts for productivity.
Example: Conduct a 15-minute weekly “Tool Tips” session.

--- Slide 20 ---

Best Practices for Effective Collaboration
4. Automate Workflows
Why it matters: Manual tasks waste time and increase the risk of errors.
Best practice:
Use tools like Zapier, Make (Integromat), or Power Automate to connect platforms.
Automate repetitive tasks, e.g.:
New form submission → Create a Trello card.
Slack message → Add to Google Calendar.
Example: Automatically send a daily standup reminder via Slack at 9:00 a.m.

5. Monitor Usage
Why it matters: Helps in auditing, troubleshooting, and enforcing accountability.
Best practice:
Use built-in audit logs, usage dashboards, and activity history.
Track who accessed/edited files, and monitor logins and sharing patterns.
Example: In Google Workspace Admin Console, check Drive activity reports to ensure compliance.

--- Slide 21 ---

Comparison table

--- Slide 22 ---

Case Studies in Cloud Collaboration
Real-world examples help demonstrate how cloud collaboration tools solve specific challenges. Here are two case studies:
A. Remote Software Team
Tools Used: GitHub + Slack + ZoomChallenge:
Team members are working remotely across different time zones, making communication and coordination difficult.
Solution:
Outcome: Smooth code development, clear communication, and stronger team alignment across time zones.

--- Slide 23 ---

Case Studies in Cloud Collaboration
B. Academic Research Group

Tools Used: Notion + ZoteroChallenge: Researchers need to manage shared papers, deadlines, and citations for collaborative writing and publishing.

Solution:
Outcome: Organized workflow, centralized research materials, 
and efficient citation management for academic writing.
.

--- Slide 24 ---

Summary
Cloud collaboration tools revolutionize how teams work and communicate.
They offer convenience, flexibility, and scalability.
Choosing the right tool depends on project needs, team size, and integration requirements.

--- Slide 25 ---

Reading and Resources
Google Workspace: https://workspace.google.com/
Microsoft 365: https://www.microsoft.com/microsoft-365
Trello: https://trello.com/
Slack: https://slack.com/
Notion: https://www.notion.so/

--- Slide 26 ---

شــــــكــــرًا لكــــــم
THANK YOU

### 03

--- Slide 1 ---

أكـــــاديميــــة طــــويـــق
Scalable Data Science

--- Slide 2 ---

Unit 5: Cloud Infrastructure & Production Deployment
Cloud Storage Fundamentals & Running Your First Cloud Analysis
By: Dr. Afshan Hashmi

--- Slide 3 ---

Course Objectives:

Define cloud storage and its core components.
Compare different cloud storage types (object, block, file).
Explain key cloud storage features (durability, availability, scalability).
Evaluate use cases for AWS S3, Azure Blob Storage, and Google Cloud Storage.
Set up a cloud-based analysis environment
Execute a basic data analysis workflow in the cloud
Compare cloud vs. local analysis performance
Optimize cloud resources for cost-effective analysis
Interpret and visualize cloud analysis results

--- Slide 4 ---

Introduction to Cloud Storage
What is Cloud Storage?
Cloud storage is a service model in which data is maintained, managed, backed up remotely, and made available to users over a network (typically the internet).
Explanation in simple terms:Instead of saving your files on a USB stick or your computer's hard drive, you save them on the internet, where they’re stored on remote servers and accessed via the web.
Key Characteristics:
Scalability: Grow storage on demand.
Durability: Data redundancy (e.g., 99.999999999% durability in AWS S3).
Accessibility: Available globally via APIs or web interfaces.
Pay-as-you-go: Only pay for what you use.
Analogy:"Like a virtual hard drive accessible from anywhere."

--- Slide 5 ---

How Does Cloud Storage Work?
Data is Sent to Data Centers Using the InternetWhen you upload a file (like a photo or document), it travels through the internet to a remote server (computer) located in a data center  a secure facility filled with powerful servers and storage systems.

Stored in Virtualized Pools of StorageOnce it arrives, your data is stored in what’s called a "virtualized storage pool" which means it's stored across many physical machines, but you see it as one unified storage space. Think of it like a virtual hard drive spread across many computers.
Accessed Using Web Interfaces, APIs, or AppsYou can access your data through:
Web interfaces (like Google Drive or Dropbox on a browser)
Mobile or desktop apps
APIs (Application Programming Interfaces) if you're integrating it with other software systems or applications.
Managed and Maintained by Cloud Service ProvidersThe infrastructure servers, security, backups, updates  is handled by companies like Amazon Web Services (AWS), Microsoft Azure, or Google Cloud.You don’t need to worry about hardware failures, power, or maintenance they take care of all that.

--- Slide 6 ---

Types of Cloud Storage
Simple Analogy:
Object storage = warehouse (you store items with tags).
File storage = filing cabinet.
Block storage = Lego blocks (fast and flexible).

--- Slide 7 ---

Benefits of Cloud Storage
Accessibility – Access Files from Anywhere
As long as you have an internet connection, you can access your files from any device, anywhere in the world.
Example: You can open your Google Docs or Dropbox files from your laptop, tablet, or phone  even while traveling.
Scalability – Easily Increase Storage as Needed
Need more space? Just click a few buttons  no need to buy hardware.
Cloud storage grows with you, making it ideal for both individuals and large businesses.
Durability & Redundancy – Data is Often Replicated Across Locations
Cloud providers copy your data across multiple data centers to prevent loss.
Even if one server crashes or there’s a natural disaster in one area, your data remains safe and available.
Cost-Effective – Pay Only for What You Use
No need to buy expensive hard drives upfront.
You pay monthly or yearly based on your actual usage  storage space, bandwidth, etc.
Automatic Backups – Data is Regularly Backed Up by the Provider
Most providers automatically back up your files behind the scenes.
This reduces the risk of losing important documents due to accidental deletion or system failure.

--- Slide 8 ---

Core Features of Cloud Storage
1. Durability
Durability means how well your data is protected from being lost or corrupted.
Cloud storage providers (like AWS, Google Cloud) use multiple copies across multiple data centers to make sure your files are safe.

Example: AWS S3 offers 99.999999999% durability (called “11 nines”)That’s like losing only 1 file every 10 million stored for 10,000 years!

2. Availability
Availability refers to how often the cloud service is accessible and running without interruption.
It’s measured as a percentage of uptime per year.
Example: AWS S3 Standard offers 99.99% availability,which means less than 1 hour of downtime per year (~53 minutes).

--- Slide 9 ---

Core Features of Cloud Storage
3. Storage Classes
Cloud providers offer different classes of storage depending on how often you need to access your data:
Example:In AWS S3, this is like:
S3 Standard (Hot)
S3 Standard-IA (Cold)
S3 Glacier / Glacier Deep Archive (Archive)

--- Slide 10 ---

Limitations of Cloud Storage
Requires Internet – No Access Without a Stable Connection
Cloud storage depends on an internet connection.
If you're in an area with poor or no internet (like during a power outage or while traveling in remote regions), you may not be able to access your files.
Ongoing Costs – Subscription or Pay-as-You-Go Model
Unlike buying a physical hard drive once, cloud storage typically follows a monthly or annual subscription model.
Costs can add up over time, especially for large storage needs or frequent access to data.
Security Concerns – Risk of Data Breaches
If not properly secured, cloud-stored data can be vulnerable to hacking, unauthorized access, or data leaks.
Users must rely on the provider’s security protocols and also take steps like enabling multi-factor authentication and using strong passwords.
 Latency – Slower Access for Large Files Compared to Local Storage
Uploading or downloading large files from the cloud can be slower than accessing files saved directly on your device.
This is especially noticeable when working with high-resolution videos, large datasets, or 3D files.

--- Slide 11 ---

Real-World Use Cases of Cloud Storage
Personal Use: Google Drive
What it is: A cloud-based storage service by Google.
How it's used: People use Google Drive to save documents, photos, videos, and other files.
Why it's useful: Files can be accessed from any device (phone, tablet, laptop) with internet access. It also allows for easy sharing and collaboration on documents in real time.

Business Use: Dropbox Business
What it is: A cloud storage solution tailored for teams and companies.
How it's used: Teams can share and manage files across different departments and locations.
Why it's useful: It offers advanced features like admin controls, file versioning, and integrations with other productivity tools, improving collaboration and productivity.

--- Slide 12 ---

Real-World Use Cases of Cloud Storage
Backup & Recovery: iCloud for iPhones
What it is: Apple’s cloud backup service.
How it's used: Automatically backs up iPhone data such as contacts, messages, app data, and photos.
Why it's useful: In case the phone is lost, damaged, or replaced, users can quickly restore all their data on a new device.

Web Hosting: Amazon S3
What it is: Amazon Simple Storage Service (S3), a part of AWS.
How it's used: Used by developers and companies to store and serve website assets like images, videos, scripts, and other static files.
Why it's useful: It's highly durable, scalable, and integrates easily with websites and applications. Plus, it allows files to be accessed globally with low latency.

--- Slide 13 ---

Key Cloud Storage Providers

--- Slide 14 ---

Cloud vs. Traditional Storage (Comparison Table)

--- Slide 15 ---

Introduction to Cloud Analysis
Definition: Performing data processing and analytics using cloud-based resources instead of local machines

Why Cloud Analysis?
Scalability: Handle datasets too large for local machines
Flexibility: Access specialized hardware (GPUs, TPUs)
Collaboration: Share results and environments easily

Common Use Cases:
Big data processing
Machine learning model training
Business intelligence dashboards

Demo: Show a real-world example (e.g., COVID-19 data analysis in the cloud)

--- Slide 16 ---

Setting Up Your Cloud Environment
Option 1: Cloud Notebooks
Google Colab
Free GPU access
Collaborative features
AWS SageMaker Notebooks
Integrated with AWS services
Enterprise-grade security
Option 2: Virtual Machines
AWS EC2
Choose instance types (CPU vs. GPU optimized)
Google Compute Engine
Pre-configured data science VMs
Activity: Students create a free-tier cloud notebook

--- Slide 17 ---

Running Your First Analysis
Sample Workflow: COVID-19 Data Analysis
Data Ingestion:
import pandas as pd
url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
df = pd.read_csv(url)
2. Data Processing:
# Filter and aggregate data
latest = df[df['date'] == df['date'].max()]
summary = latest.groupby('continent')['total_cases'].sum()
3. Visualization:
import matplotlib.pyplot as plt
summary.plot(kind='bar')
plt.title('Total COVID Cases by Continent')
plt.show()

--- Slide 18 ---

Performance Benchmarking
Exercise: Compare local vs. cloud runtime
Run analysis on local machine (time it)
Run same analysis in cloud notebook (time it)
Compare results

Sample Results:
Discussion: When does cloud analysis make sense?

--- Slide 19 ---

Cost Optimization
Cloud Cost Factors:
Compute time
Storage
Data transfer

Money-Saving Tips:
Use spot instances
Auto-shutdown unused resources
Right-size instances

Activity: Estimate costs using AWS/GCP pricing calculators

--- Slide 20 ---

Summary:
Cloud storage lets users store and access data over the internet.
Comes in object, file, and block storage types.
Offers flexibility, cost savings, and ease of use but needs internet and security awareness.
Commonly used in personal, academic, and business settings.
Cloud analysis enables scalable processing of large datasets using remote resources (GPUs/TPUs), overcoming local hardware limitations.
Performance benchmarks show 10x+ speedups for big data tasks.
Monitor resources to avoid over-spending
Use spot instances for 60-90% cost savings

--- Slide 21 ---

Resources & Further Reading
Free Cloud Credits: AWS Educate, Google Cloud Free Tier
Datasets: Google Cloud Public Datasets, AWS Open Data
Data Science on AWS” Authors: Chris Fregly & Antje Barth Publisher: O'Reilly (2021)
Google Cloud for Data Science Authors: Valliappa Lakshmanan & Jordan Tigani, Publisher: O'Reilly (2022)

--- Slide 22 ---

الشراكات العالمية

--- Slide 23 ---

شــــــكــــرًا لكــــــم
THANK YOU

### 04

--- Slide 1 ---

أكـــــاديميــــة طــــويـــق
Scalable Data Science

--- Slide 2 ---

cuDF: Understsanding performance
Correct the code
By: Dr. Afshan Hashmi

--- Slide 3 ---

Course Objectives:
Learners will be able to identify the performance issue
Learners will be able to Fix the issue in the code

--- Slide 4 ---

Avoiding Unnecessary to_pandas() Calls

Question: The following code converts a cuDF DataFrame to Pandas unnecessarily, causing performance issues. Correct the code to improve performance.
import cudf

df = cudf.DataFrame({'a': [1, 2, 3, 4], 'b': [5, 6, 7, 8]})

# Inefficient approach
df_pandas = df.to_pandas()
df_pandas['c'] = df_pandas['a'] + df_pandas['b']
df = cudf.DataFrame.from_pandas(df_pandas)

print(df)
Hint: Perform operations directly on the cuDF DataFrame.

--- Slide 5 ---

1. Avoiding Unnecessary to_pandas() Calls- Corrected code
By performing the addition directly on the cuDF DataFrame, we avoid converting it to Pandas, thus improving performance.
import cudf

df = cudf.DataFrame({'a': [1, 2, 3, 4], 'b': [5, 6, 7, 8]})

# Correct approach: Perform operations directly on the cuDF DataFrame
df['c'] = df['a'] + df['b']

print(df)

--- Slide 6 ---

2. Replacing apply() with Vectorized Operations

Question: The function applied in apply() is not GPU-optimized, forcing execution on the CPU. Modify the code to use vectorized operations.
Hint: Avoid apply() and use built-in cuDF vectorized operations.
import cudf

df = cudf.DataFrame({'a': [1, 2, 3, 4], 'b': [5, 6, 7, 8]})

# Inefficient approach
df['c'] = df.apply(lambda row: row['a'] + row['b'], axis=1)

print(df)

--- Slide 7 ---

2. Replacing apply() with Vectorized Operations- Corrected code
This approach avoids the use of apply() and leverages cuDF's built-in vectorized operations, which are much more efficient.
import cudf

df = cudf.DataFrame({'a': [1, 2, 3, 4], 'b': [5, 6, 7, 8]})

# Correct approach: Use vectorized operations
df['c'] = df['a'] + df['b']

print(df)

--- Slide 8 ---

3. Incorrect cuDF GroupBy Operation

Question: The following code attempts to use a Pandas-style aggregation on a cuDF DataFrame but fails. Correct it to work efficiently with cuDF.
Hint: apply() is not GPU-optimized for groupby. Use a built-in cuDF aggregation instead.
import cudf

df = cudf.DataFrame({'category': ['A', 'B', 'A', 'B'], 'values': [10, 20, 30, 40]})

# Incorrect approach
df_grouped = df.groupby('category').apply(lambda x: x['values'].sum())

print(df_grouped)

--- Slide 9 ---

3. Incorrect cuDF GroupBy Operation-Corrected code
Instead of using apply(), which is not optimized for groupby operations, we use the built-in sum() method for grouping and aggregation in cuDF..
import cudf

df = cudf.DataFrame({'category': ['A', 'B', 'A', 'B'], 'values': [10, 20, 30, 40]})

# Correct approach: Use a cuDF aggregation instead of apply()
df_grouped = df.groupby('category')['values'].sum()

print(df_grouped)

--- Slide 10 ---

4. Fixing Third-Party Library Compatibility Issue

Question: The following code tries to use Plotly directly with a cuDF DataFrame, which is not compatible. Modify it so that it works correctly.
import cudf
import plotly.express as px

df = cudf.DataFrame({'x': [1, 2, 3, 4], 'y': [10, 20, 30, 40]})

# Incorrect approach
fig = px.scatter(df, x='x', y='y')
fig.show()
Hint: Convert cuDF DataFrame to Pandas before passing it to Plotly.

--- Slide 11 ---

4. Fixing Third-Party Library Compatibility Issue-Corrected Code
import cudf
import plotly.express as px

df = cudf.DataFrame({'x': [1, 2, 3, 4], 'y': [10, 20, 30, 40]})

# Correct approach: Convert cuDF DataFrame to Pandas before passing to Plotly
df_pandas = df.to_pandas()
fig = px.scatter(df_pandas, x='x', y='y')
fig.show()
Since Plotly does not support cuDF DataFrames directly, we convert it to Pandas for visualization.

--- Slide 12 ---

5. Debugging Performance Issues in cuDF

Question: The following code processes a large cuDF DataFrame but runs unexpectedly slow. Identify and fix the performance issue.
Hint: Identify which function is causing CPU execution and replace it with a GPU-optimized alternative.
import cudf

df = cudf.DataFrame({'a': range(1, 1000001), 'b': range(1000001, 2000001)})

# Inefficient approach
df['c'] = df.apply(lambda row: row['a'] * 2 + row['b'] * 3, axis=1)

print(df.head())

--- Slide 13 ---

5. Debugging Performance Issues in cuDF-Corrected Code
import cudf

df = cudf.DataFrame({'a': range(1, 1000001), 'b': range(1000001, 2000001)})

# Correct approach: Use vectorized operations instead of apply
df['c'] = df['a'] * 2 + df['b'] * 3

print(df.head())
Here, we replace apply() with vectorized operations (df['a'] * 2 + df['b'] * 3), which are GPU-accelerated, ensuring that the operations run on the GPU for optimal performance.

--- Slide 14 ---

شــــــكــــرًا لكــــــم
THANK YOU

### 05

--- Slide 1 ---

أكـــــاديميــــة طــــويـــق
Scalable Data Science

--- Slide 2 ---

cuML for GPU-accelerated machine learning
By: Dr. Afshan Hashmi

--- Slide 3 ---

Course Objectives:

Understand GPU-Accelerated Machine Learning – Learn how to leverage RAPIDS cuML for high-performance machine learning on large datasets, comparing it with traditional CPU-based approaches.

Implement Efficient ML Models – Develop and optimize machine learning models using cuML, including regression, classification, and clustering, to achieve faster training and inference times.

Apply cuML to Real-World Problems – Gain hands-on experience in applying GPU-accelerated ML techniques to practical use cases such as financial modeling, image recognition, and natural language processing.

--- Slide 4 ---

Introduction to cuML(RAPIDS Machine Learning Library)
What is cuML?
cuML is an open-source GPU-accelerated machine learning library developed by NVIDIA as part of the RAPIDS AI framework. It provides highly optimized implementations of common machine learning algorithms using CUDA.

Why Use cuML?

Faster Computation: Leverages GPUs for parallel execution, significantly reducing training time.

Compatible with scikit-learn: Provides a similar API, making it easy to transition from CPU-based models.

Seamless Integration: Works well with cuDF (GPU-accelerated pandas) and other RAPIDS libraries.
cuML
Rapids Machine Learning Library

--- Slide 5 ---

cuML overview
cuML is a machine learning library developed by NVIDIA as part of the RAPIDS ecosystem.
Its main goal is to accelerate traditional machine learning algorithms using GPU computing.
cuML offers GPU-accelerated versions of many popular algorithms found in scikit-learn, such as linear regression, k-means clustering, and random forests.
It is especially useful for large datasets and real-time applications, where traditional CPU-based libraries may become slow or inefficient.
It uses CUDA, NVIDIA’s parallel computing platform, to achieve high performance.
A major advantage is its API similarity to scikit-learn, making it easy for developers to switch with minimal code changes.

--- Slide 6 ---

Significance of cuML
Traditional ML tools like scikit-learn use CPUs, which can be slow and inefficient for very large datasets.
cuML solves this issue by using GPU acceleration via NVIDIA CUDA, leading to much faster training and inference.
It's especially helpful in situations where real-time processing or big data is involved (e.g., streaming data or massive logs).
cuML can scale ML workflows that would otherwise be limited by CPU memory and speed.
It is particularly useful for data scientists and engineers who want faster experimentation and deployment cycles without changing much code.

--- Slide 7 ---

Installation of cuML
cuML is part of the RAPIDS ecosystem developed by NVIDIA, and it depends on specific GPU drivers and CUDA versions.
Recommended installation method is through Conda because it handles all the dependencies (like cudatoolkit) more smoothly.
conda install -c rapidsai -c nvidia -c conda-forge \
    cuml=24.02 python=3.10 cudatoolkit=11.8
-c rapidsai, -c nvidia, and -c conda-forge specify the channels to search for the packages.
cuml=24.02 specifies the version of cuML.
python=3.10 ensures compatibility with that Python version.
cudatoolkit=11.8 tells Conda to install the CUDA runtime compatible with your GPU.

--- Slide 8 ---

Installation of cuML
Pip installation is available but has limited support, especially regarding complex dependencies:
pip install cuml-cu11 --extra-index-url=https://pypi.nvidia.com
Before installation:
Ensure your system has an NVIDIA GPU.
CUDA drivers should be properly installed.
Best to test in Google Colab or a Docker container if unsure about system compatibility.

--- Slide 9 ---

cuML-Supported Algorithms
cuML provides GPU-accelerated implementations of various machine learning algorithms, including:

Linear Models: Linear Regression, Ridge Regression, Lasso Regression

Clustering: K-Means, DBSCAN

Dimensionality Reduction: PCA, t-SNE, Truncated SVD

Tree-based Models: Random Forest, Decision Trees

Other Models: Nearest Neighbors, Support Vector Machines, Gaussian Mixture Models

--- Slide 10 ---

Using cuML's Linear Regression
This is a simple demonstration of how to use cuML to train and predict using Linear Regression, leveraging the GPU for computation:
import cuml
from cuml.linear_model import LinearRegression
import cupy as cp

# Generate sample data
X = cp.random.rand(1000, 3)
y = cp.dot(X, cp.array([3.5, 2.0, 6.7])) + 1.2

# Create and train model
model = LinearRegression()
model.fit(X, y)

# Predict
preds = model.predict(X)
print(preds[:5])
Imports:
cuml.linear_model.LinearRegression: cuML's version of 
scikit-learn's LinearRegression, GPU-accelerated.
cupy: Like NumPy but for GPU arrays.

Generates 1000 rows and 3 feature columns of random 
data on the GPU.
Creates a target variable y using a linear equation. Basically:y = 3.5*x1 + 2.0*x2 + 6.7*x3 + 1.2

Creates and fits a linear regression model using GPU arrays.

Makes predictions and prints the first 5 results.

--- Slide 11 ---

Real-World Applications of cuML
Finance: Risk modeling, fraud detection, stock price prediction
Healthcare: Genomic analysis, patient diagnosis predictions
Retail: Customer segmentation, demand forecasting
Cybersecurity: Anomaly detection in network traffic
This Photo by Unknown Author is licensed under CC BY-SA-NC

--- Slide 12 ---

Importing cuML and Dependencies
cudf: A GPU-accelerated DataFrame library similar to pandas, optimized for NVIDIA GPUs.
cuml.linear_model.LinearRegression: GPU-accelerated linear regression model.
cuml.cluster.KMeans: GPU-accelerated K-Means clustering algorithm.
numpy and pandas: Used for handling arrays and data processing before converting them into GPU-optimized structures.
This setup ensures that machine learning workflows leverage GPU acceleration instead of CPU-based operations.

--- Slide 13 ---

cuML vs. Scikit-Learn Speed Comparison
Uses cudf.DataFrame and cudf.Series to transfer data to the GPU.


Measures and prints the execution time for both implementations.


Demonstrates the potential speedup of cuML over scikit-learn for large datasets.

--- Slide 14 ---

GPU-Accelerated K-Means Clustering
Implements GPU-based K-Means clustering, which is significantly faster than CPU-based implementations.

Uses cudf.DataFrame to store data in a GPU-compatible format.

Computes cluster centers efficiently using GPU-accelerated processing.

Helps in segmentation tasks, such as customer grouping in retail or anomaly detection.

--- Slide 15 ---

GPU-Accelerated Principal Component Analysis
Implements GPU-accelerated PCA, which reduces dimensionality faster than traditional PCA methods.

Uses cudf.DataFrame for efficient GPU memory handling
Helps in feature extraction and compression in large datasets.

Essential for preprocessing high-dimensional datasets in computer vision, bioinformatics, and NLP.

--- Slide 16 ---

Integrating cuML with Deep Learning (TensorFlow/PyTorch)
Shows how cuML can work alongside deep learning frameworks like PyTorch.

Moves data to GPU using .cuda(), but transfers it to CPU (.cpu().numpy()) before using cuML (since cuML does not support PyTorch tensors directly).

Enables hybrid machine learning and deep learning workflows, useful in reinforcement learning, AI-powered security, and fraud detection.

--- Slide 17 ---

Project : Predicting House Prices using cuML
Steps:
Load the dataset (California housing dataset from sklearn).
Preprocess the data and move it to cuDF for GPU processing.
Train a Linear Regression model using cuML.
Compare performance with Scikit-learn (CPU-based).
Evaluate the model's performance (MSE & Training Time).
For Full code click here

--- Slide 18 ---

Performance Tips in cuML
To get the most out of cuML's GPU acceleration.
 Since the whole idea behind cuML is faster ML on GPUs, following these tips ensures maximum efficiency:
Keep data in GPU memory:
Use cupy (for arrays) or cuDF (for DataFrames).
Transferring data back and forth between CPU and GPU slows down performance.
Avoid frequent CPU-GPU transfers:
Minimize operations like to_pandas() or cp.asnumpy(), which move data off the GPU.
Use RAPIDS Memory Manager:
For large-scale ML tasks, this helps manage GPU memory efficiently and avoid memory overflows.
Monitor GPU usage with nvidia-smi:
This command-line tool helps you track memory usage, running processes, and GPU load in real time.
These tips are essential for building high-performance machine learning pipelines using cuML, especially with large datasets or real-time applications.

--- Slide 19 ---

Advantages and Limitations of cuML
Advantages:

Massively Parallel Computation: Ideal for large datasets.

Easy Transition from scikit-learn: Similar API.

Optimized for NVIDIA GPUs: Provides huge speedups.

Limitations:

Requires NVIDIA GPU: Not useful for CPU-only environments.

Memory Constraints: GPU memory is limited compared to CPU RAM.

Limited Algorithm Support: Some ML models are not yet implemented in cuML.

--- Slide 20 ---

Comparison of cuML with Scikit-learn

--- Slide 21 ---

Recap
cuML provides GPU-accelerated versions of popular machine learning algorithms.
It offers significant performance improvements over traditional CPU-based libraries like scikit-learn.
The API is designed to be familiar to scikit-learn users, allowing for easy transition.
cuML is part of the RAPIDS ecosystem, enabling seamless integration with cuDF and other GPU tools.
Ideal for big data and real-time ML applications that demand speed and scalability.
A valuable tool for data scientists aiming to harness the power of NVIDIA GPUs for ML workloads.

--- Slide 22 ---

Practical Implementation
Click on the link below to go to Google COLAB
Click HERE

--- Slide 23 ---

الشراكات العالمية

--- Slide 24 ---

شــــــكــــرًا لكــــــم
THANK YOU

### 06

--- Slide 1 ---

أكـــــاديميــــة طــــويـــق
Scalable Data Science

--- Slide 2 ---

cuML: open-source GPU-accelerated machine learning library
By: Dr. Afshan Hashmi

--- Slide 3 ---

Course Objectives:

Understand GPU-Accelerated Machine Learning – Learn how to leverage RAPIDS cuML for high-performance machine learning on large datasets, comparing it with traditional CPU-based approaches.

Implement Efficient ML Models – Develop and optimize machine learning models using cuML, including regression, classification, and clustering, to achieve faster training and inference times.

Apply cuML to Real-World Problems – Gain hands-on experience in applying GPU-accelerated ML techniques to practical use cases such as financial modeling, image recognition, and natural language processing.

--- Slide 4 ---

Introduction to cuML(RAPIDS Machine Learning Library)
What is cuML?
cuML is an open-source GPU-accelerated machine learning library developed by NVIDIA as part of the RAPIDS AI framework. It provides highly optimized implementations of common machine learning algorithms using CUDA.

Why Use cuML?

Faster Computation: Leverages GPUs for parallel execution, significantly reducing training time.

Compatible with scikit-learn: Provides a similar API, making it easy to transition from CPU-based models.

Seamless Integration: Works well with cuDF (GPU-accelerated pandas) and other RAPIDS libraries.
cuML
Rapids Machine Learning Library

--- Slide 5 ---

cuML-Supported Algorithms
cuML provides GPU-accelerated implementations of various machine learning algorithms, including:

Linear Models: Linear Regression, Ridge Regression, Lasso Regression

Clustering: K-Means, DBSCAN

Dimensionality Reduction: PCA, t-SNE, Truncated SVD

Tree-based Models: Random Forest, Decision Trees

Other Models: Nearest Neighbors, Support Vector Machines, Gaussian Mixture Models

--- Slide 6 ---

Real-World Applications of cuML
Finance: Risk modeling, fraud detection, stock price prediction
Healthcare: Genomic analysis, patient diagnosis predictions
Retail: Customer segmentation, demand forecasting
Cybersecurity: Anomaly detection in network traffic
This Photo by Unknown Author is licensed under CC BY-SA-NC

--- Slide 7 ---

Importing cuML and Dependencies
cudf: A GPU-accelerated DataFrame library similar to pandas, optimized for NVIDIA GPUs.
cuml.linear_model.LinearRegression: GPU-accelerated linear regression model.
cuml.cluster.KMeans: GPU-accelerated K-Means clustering algorithm.
numpy and pandas: Used for handling arrays and data processing before converting them into GPU-optimized structures.
This setup ensures that machine learning workflows leverage GPU acceleration instead of CPU-based operations.

--- Slide 8 ---

cuML vs. Scikit-Learn Speed Comparison
Uses cudf.DataFrame and cudf.Series to transfer data to the GPU.


Measures and prints the execution time for both implementations.


Demonstrates the potential speedup of cuML over scikit-learn for large datasets.

--- Slide 9 ---

GPU-Accelerated K-Means Clustering
Implements GPU-based K-Means clustering, which is significantly faster than CPU-based implementations.

Uses cudf.DataFrame to store data in a GPU-compatible format.

Computes cluster centers efficiently using GPU-accelerated processing.

Helps in segmentation tasks, such as customer grouping in retail or anomaly detection.

--- Slide 10 ---

GPU-Accelerated Principal Component Analysis
Implements GPU-accelerated PCA, which reduces dimensionality faster than traditional PCA methods.

Uses cudf.DataFrame for efficient GPU memory handling
Helps in feature extraction and compression in large datasets.

Essential for preprocessing high-dimensional datasets in computer vision, bioinformatics, and NLP.

--- Slide 11 ---

Integrating cuML with Deep Learning (TensorFlow/PyTorch)
Shows how cuML can work alongside deep learning frameworks like PyTorch.

Moves data to GPU using .cuda(), but transfers it to CPU (.cpu().numpy()) before using cuML (since cuML does not support PyTorch tensors directly).

Enables hybrid machine learning and deep learning workflows, useful in reinforcement learning, AI-powered security, and fraud detection.

--- Slide 12 ---

Project : Predicting House Prices using cuML
Steps:
Load the dataset (California housing dataset from sklearn).
Preprocess the data and move it to cuDF for GPU processing.
Train a Linear Regression model using cuML.
Compare performance with Scikit-learn (CPU-based).
Evaluate the model's performance (MSE & Training Time).
For Full code click here

--- Slide 13 ---

Advantages and Limitations of cuML
Advantages:

Massively Parallel Computation: Ideal for large datasets.

Easy Transition from scikit-learn: Similar API.

Optimized for NVIDIA GPUs: Provides huge speedups.

Limitations:

Requires NVIDIA GPU: Not useful for CPU-only environments.

Memory Constraints: GPU memory is limited compared to CPU RAM.

Limited Algorithm Support: Some ML models are not yet implemented in cuML.

--- Slide 14 ---

Comparison of cuML with Scikit-learn

--- Slide 15 ---

Practical Implementation
Click on the link below to go to Google COLAB
Click HERE

--- Slide 16 ---

الشراكات العالمية

--- Slide 17 ---

شــــــكــــرًا لكــــــم
THANK YOU

### 07

--- Slide 1 ---

أكـــــاديميــــة طــــويـــق
Scalable Data Science

--- Slide 2 ---

Data visualization
With Seaborn and Matplotlib
By: Dr. Afshan Hashmi

--- Slide 3 ---

Course Objectives:
Learn the fundamentals of data visualization using Matplotlib and Seaborn.
Create static, animated, and interactive plots for data analysis.
Utilize Seaborn for statistical and enhanced visualizations.
Customize plots with themes, colors, and annotations.

--- Slide 4 ---

Matplotlib and Seaborn for Data Visualization
Data visualization is crucial in scalable data science for understanding trends, distributions, and relationships. 

Matplotliband Seaborn are two powerful Python libraries that provide extensive functionalities for creating insightful and high-quality visualizations.

--- Slide 5 ---

Matplotlib
Introduction to Matplotlib: Matplotlib is a fundamental library for creating static, animated, and interactive visualizations. It provides fine-grained control over plots, making it highly customizable.
Key Features:
Supports a wide range of plot types (line, bar, scatter, etc.).
Highly customizable (labels, colors, themes, annotations).
Integrates well with Jupyter Notebooks and other Python libraries.

--- Slide 6 ---

Using Matplotlib

--- Slide 7 ---

Seaborn
Creating Plots with Seaborn
Purpose: Seaborn is built on top of Matplotlib and provides a high-level interface for creating advanced statistical plots.
Key Features:
Simplifies the creation of complex visualizations (e.g., heatmaps, pair plots).
Enhances Matplotlib graphs with better default styles and color palettes.

--- Slide 8 ---

Using Seaborn

--- Slide 9 ---

Customizing Visuals
Customizing plots makes them more readable and visually appealing. You can modify labels, colors, themes, and annotations in both Matplotlib and Seaborn.

--- Slide 10 ---

Line and Bar Plots
Used to visualize trends over time and compare categorical data.

--- Slide 11 ---

Scatter and Box Plots
Scatter plots show relationships between two variables.
Example: Scatter Plot with Regression Line

--- Slide 12 ---

Box Plots
Box plots help analyze the distribution and outliers in a dataset.

--- Slide 13 ---

Heatmaps visualize correlations in datasets.

--- Slide 14 ---

Pair plots show pairwise relationships in multi-variable data.

--- Slide 15 ---

Conclusion
Matplotlib is great for fine-grained control over plots.

Seaborn simplifies statistical visualizations with beautiful themes.

Customization improves readability and storytelling in data science.

Different visualization types (scatter, box, heatmaps) provide insights into trends, distributions, and relationships.

These techniques are scalable, meaning they work efficiently with both small and large datasets.

--- Slide 16 ---

Practical Implementation
Click on the link below to go to Google COLAB
https://colab.research.google.com/drive/1Z9sV8qnk7--__x8OcKO1adtFJz82f4Bx

--- Slide 17 ---

شــــــكــــرًا لكــــــم
THANK YOU

### 08

--- Slide 1 ---

أكـــــاديميــــة طــــويـــق
Scalable Data Science

--- Slide 2 ---

Deploying GPU-accelerated data pipelines
By: Dr. Afshan Hashmi

--- Slide 3 ---

Course Objectives:

Understand the architecture and benefits of GPU-accelerated computing
Design efficient data pipelines for GPU processing
Implement GPU-accelerated data transformations
Optimize pipeline performance through benchmarking
Deploy GPU pipelines in production environments
Monitor and maintain GPU-accelerated systems

--- Slide 4 ---

Fundamentals of GPU Computing

--- Slide 5 ---

Introduction to GPU Architecture
What is a GPU?

GPU stands for Graphics Processing Unit.
Originally designed for rendering images and video.
Now widely used for parallel computation in scientific computing, deep learning, etc.

Originally, GPUs (Graphics Processing Units) were developed to handle the intensive mathematical calculations needed to render graphics and images. However, due to their highly parallel structure having thousands of lightweight cores they are now extensively used in fields beyond graphics.

--- Slide 6 ---

Applications of GPU
Scientific Computing: Tasks such as simulations, numerical methods, and modeling large datasets (e.g., weather forecasting, molecular dynamics) benefit from GPU parallelism.

Deep Learning: Training neural networks involves large matrix operations and backpropagation, which are efficiently handled by GPUs.

Other: Other applications include cryptography, financial modeling, medical imaging, real-time data analytics, and more.

--- Slide 7 ---

CPU vs GPU: Architectural Differences

--- Slide 8 ---

Key GPU Components
CUDA Cores: Execution units in NVIDIA GPUs responsible for computation.

Streaming Multiprocessors (SMs): Group of CUDA cores sharing resources.

Memory Hierarchy:
Global Memory: Large but slow, shared across all SMs.
Shared Memory: Faster, shared within a single SM.
Registers: Fastest, private to individual threads.
Constant & Texture Memory: Read-only, optimized for specific access patterns.

--- Slide 9 ---

CUDA cores
CUDA cores are the basic processing elements within NVIDIA GPUs. Think of them as tiny, simplified CPU cores that can execute thousands of operations in parallel. Here’s what makes them special:
CUDA stands for Compute Unified Device Architecture — a parallel computing platform developed by NVIDIA.
Each CUDA core can perform arithmetic and logic operations (like addition, multiplication) on data.
In a GPU, hundreds to thousands of CUDA cores work together to handle tasks that are divided into many small, independent parts — this is ideal for parallel processing (e.g., image processing, matrix multiplication, deep learning).
They reside within larger units called Streaming Multiprocessors (SMs), which group multiple CUDA cores to operate together efficiently.
Analogy: If a CPU is a few skilled workers doing one task at a time, a GPU with CUDA cores is like an army of helpers doing many tasks simultaneously.

--- Slide 10 ---

Streaming Multiprocessor (SM)
A Streaming Multiprocessor (SM) is a fundamental building block of an NVIDIA GPU. Each SM contains:
Multiple CUDA cores (the units that do computations),
Shared resources like registers, shared memory, and instruction schedulers.
The CUDA cores inside an SM work together, executing instructions in parallel. Threads running the same kernel are grouped into warps (typically 32 threads), and these warps are scheduled by the SM.
It’s Importance:
SMs allow massive parallelism, which is key to GPU acceleration.
The efficiency of your GPU program depends heavily on how well it utilizes the SM's shared resources and memory hierarchy.
Understanding SMs helps optimize thread and memory usage in CUDA programs.

--- Slide 11 ---

Memory Hierarchy
In GPU computing, memory hierarchy refers to the different types of memory available within 
the GPU and how they differ in speed, size, and scope. Understanding this hierarchy is crucial for
 writing efficient GPU code. Here's a breakdown of the key memory types:

--- Slide 12 ---

Importance of Memory Hierarchy
Performance is greatly influenced by how you use memory.

Registers and shared memory are fast but limited in size.

Global memory is abundant but slow, so minimizing access or coalescing it is key.

Organizing data and computation to match this hierarchy results in massive speedups.

--- Slide 13 ---

Memory Bandwidth & Latency
When working with GPUs, two critical performance concepts to understand are memory bandwidth and latency:
Memory Bandwidth
This is the maximum rate at which data can be transferred between the GPU’s memory and its processing cores.
Think of it like the width of a highway—the wider it is, the more cars (data) can travel at the same time.
GPUs are designed with very high bandwidth to move massive amounts of data quickly for parallel tasks like image processing or deep learning.
Memory Latency
Latency is the delay between issuing a memory request and receiving the data.
Imagine latency as the reaction time before a car even starts moving on the highway.
GPUs have relatively high latency compared to CPUs because they prioritize throughput (moving a lot of data fast), not instant response.

--- Slide 14 ---

Importance of Memory Bandwidth & Latency
Although GPUs have high bandwidth, latency can still hurt performance if your code makes many small, random accesses to global memory.

To optimize GPU code, you should:
Use shared memory when possible (it’s much faster).
Minimize transfers between the CPU (host) and GPU (device).
Ensure memory access is coalesced (threads access data in contiguous blocks).

--- Slide 15 ---

GPU Programming Models
These are three major frameworks or platforms for GPU programming:

CUDA, OpenCL, ROCm Comparison

--- Slide 16 ---

Data Parallelism vs Task Parallelism
These are two approaches to organizing computations for parallel execution:

Data Parallelism
The same operation is applied to multiple data elements simultaneously.
Perfectly suited for GPU architectures.
Example: Adding two vectors element-wise—each GPU thread handles one element.

Task Parallelism
Different tasks or functions run in parallel, often on separate threads.
More common in CPU-based parallelism or when operations are diverse.
Example: One thread reads data, another processes it, another saves it.

Why Its important:
GPUs are built for data parallelism with thousands of lightweight cores that work best when doing identical tasks on large data sets.
Task parallelism is more complex and less efficient on GPUs but works well on CPUs.

--- Slide 17 ---

Kernel Execution Model
This model explains how a GPU executes a program, especially under CUDA or similar frameworks.

Host vs Device
Host: Your CPU and RAM — responsible for launching GPU tasks.
Device: The GPU — does the heavy lifting of parallel computation.
A CPU (host) sends instructions to the GPU (device), usually in the form of a function called a kernel.
 Kernel

A kernel is a function that runs on the GPU.
When launched, it's executed simultaneously by many threads.

--- Slide 18 ---

Kernel Execution Model
Thread Hierarchy
To organize so many threads, CUDA uses a three-level hierarchy:
Threads — Individual units of execution.
Blocks — A group of threads.
Grid — A collection of blocks.
This makes it easy to scale computations across thousands of threads.
Calculating Thread ID
Each thread needs a unique index to access its specific portion of data.

int thread_id = blockIdx.x * blockDim.x + threadIdx.x;

This formula is used in CUDA programming to uniquely identify each GPU thread when running a kernel.
Here's what each term means:
threadIdx.x: The index of the thread within its block.
blockDim.x: The number of threads in each block.
blockIdx.x: The index of the block within the grid.

--- Slide 19 ---

GPU Hardware Exploration
Use terminal commands to explore GPU properties.
NVIDIA Systems:
This shows:
Current GPU usage (e.g., memory usage, temperature)
Active processes using the GPU
GPU model, driver version, and compute capabilities

--- Slide 20 ---

Data Pipeline Design for GPU Acceleration

--- Slide 21 ---

Pipeline Design Principles
Data Flow Patterns for GPU Acceleration
Data pipelines consist of stages where data flows through various processes. In the context of GPU acceleration, understanding how data moves between these stages is key to optimizing performance.
Batch Processing:
Process large chunks of data in parallel, suited for workloads where all data is available at once (e.g., deep learning model training).
GPUs excel at processing large batches efficiently because they are designed for parallelism.
Streaming Processing:
Continuously process data as it becomes available (e.g., real-time analytics).
GPUs are less suited for streaming due to potential latency and challenges in maintaining real-time throughput.
Hybrid Models:
Some applications use a combination of batch and streaming (e.g., video processing) where frames are processed in batches while streaming.

--- Slide 22 ---

Memory Management Strategies
Efficient memory management is crucial for leveraging GPU capabilities:
Global Memory:
Large, but slower compared to other types of memory.
Shared across all threads.
Minimize transfers between host and device to reduce bottlenecks.
Shared Memory:
Faster memory within a single streaming multiprocessor (SM).
Use shared memory for temporary data that is accessed frequently by threads in the same block.
Constant Memory:
Used for read-only data that doesn't change during kernel execution.
Great for storing constants like model parameters in deep learning.
Memory Coalescing:
Ensures that memory accesses by threads in a warp are coalesced, meaning they are combined into fewer transactions for efficient access.

--- Slide 23 ---

Common Pipeline Operations
GPU-Accelerated ETL Operations
ETL (Extract, Transform, Load) operations are commonly used to preprocess data for analysis or machine learning.
Extract:
Load data from external sources (e.g., databases, files).
GPUs can accelerate extraction, especially for tasks like parsing large datasets or loading images.
Transform:
Feature transformations (e.g., scaling, encoding, normalization).
GPUs speed up data transformation by using parallelization to apply these transformations across large datasets quickly.
Load:
Insert the processed data into storage.
While the loading process itself is typically CPU-bound, GPUs can speed up post-processing for loading tasks that involve computation (e.g., aggregation, sorting).

--- Slide 24 ---

Feature Engineering Transformations
Parallelization of Feature Engineering:GPUs can process features in parallel, allowing fast calculations of statistical features (e.g., mean, variance, correlations) or encoding tasks like one-hot encoding for categorical variables.
Dimensionality Reduction:
Techniques like PCA or t-SNE can be accelerated by leveraging GPU computation power.
a. Principal Component Analysis (PCA)
PCA is a statistical technique used to transform a dataset into a set of orthogonal (uncorrelated) components, ranked by variance. This allows you to reduce the dataset's dimensionality while preserving the most important information.
b. t-SNE
t-SNE is another technique used for dimensionality reduction, particularly for visualizing high-dimensional data by mapping it to a lower-dimensional space (usually 2D or 3D). It's effective in preserving the local structure of the data, making it suitable for exploratory data analysis.

--- Slide 25 ---

Why GPUs Are Beneficial for These Tasks
Parallel Processing: Both PCA and t-SNE involve operations that can be parallelized, such as matrix multiplications or distance calculations. GPUs can handle these tasks in parallel across multiple cores, reducing the time complexity of the algorithms.
Speed: GPUs are designed to process large amounts of data in parallel, making them much faster than CPUs for operations like encoding, feature transformations, and matrix decompositions.
Scalability: Using GPUs makes it possible to scale up the feature engineering process for larger datasets, allowing data scientists to process datasets that wouldn't be feasible with CPU-based methods.

In summary, parallelization of feature engineering tasks and dimensionality reduction techniques can be greatly accelerated by using GPUs. Whether it's calculating statistical features, encoding categorical variables, or applying dimensionality reduction algorithms like PCA and t-SNE, GPUs provide significant performance improvements, making them a valuable tool in the data preprocessing pipeline, especially for large datasets.

--- Slide 26 ---

Data Augmentation Techniques
Data Augmentation Techniques
Data augmentation is a key technique in machine learning and deep learning that involves creating new, slightly modified versions of existing data to improve the generalization ability of models. This is particularly crucial when dealing with limited datasets, as augmentation can synthetically increase the dataset size and variability without the need for additional data collection.
With the ever-increasing size of datasets and the complexity of augmentation methods, GPUs have become essential in speeding up the process, ensuring that training pipelines remain efficient and scalable.

Image Augmentation:
GPUs are widely used for accelerating image augmentations such as flipping, cropping, rotating, and color adjustment.
Text Augmentation:
Parallel transformations like tokenization or paraphrasing can be sped up on GPUs.
Audio Augmentation:
Techniques like pitch shifting, noise addition, and time warping can be done in parallel using GPU acceleration.

--- Slide 27 ---

GPU Advantages:
Audio transformations often involve FFTs (Fast Fourier Transforms), spectrogram generation, and convolution all operations that benefit from GPU parallelism.
Libraries like TorchAudio, Kapre (Keras), and NVIDIA NeMo support GPU-accelerated audio preprocessing and augmentation.
Parallel batch processing of audio clips on the GPU dramatically reduces the time required for real-time augmentation during model training.
Faster processing of large batches.
On-the-fly augmentation without pre-generating and storing augmented data.
Scalability in high-throughput data pipelines.

By accelerating image, text, and audio augmentations using GPUs, data scientists and ML engineers can achieve faster model convergence, better generalization, and more efficient training workflows.

--- Slide 28 ---

Data Augmentation Techniques
GPU Advantages:

Audio transformations often involve FFTs (Fast Fourier Transforms), spectrogram generation, and convolution all operations that benefit from GPU parallelism.
Libraries like TorchAudio, Kapre (Keras), and NVIDIA NeMo support GPU-accelerated audio preprocessing and augmentation.
Parallel batch processing of audio clips on the GPU dramatically reduces the time required for real-time augmentation during model training.
Faster processing of large batches.
On-the-fly augmentation without pre-generating and storing augmented data.
Scalability in high-throughput data pipelines.

By accelerating image, text, and audio augmentations using GPUs, data scientists and ML engineers can achieve faster model convergence, better generalization, and more efficient training workflows.

--- Slide 29 ---

Data Augmentation Techniques
GPU Advantages:

Audio transformations often involve FFTs (Fast Fourier Transforms), spectrogram generation, and convolution all operations that benefit from GPU parallelism.
Libraries like TorchAudio, Kapre (Keras), and NVIDIA NeMo support GPU-accelerated audio preprocessing and augmentation.
Parallel batch processing of audio clips on the GPU dramatically reduces the time required for real-time augmentation during model training.
Faster processing of large batches.
On-the-fly augmentation without pre-generating and storing augmented data.
Scalability in high-throughput data pipelines.

By accelerating image, text, and audio augmentations using GPUs, data scientists and ML engineers can achieve faster model convergence, better generalization, and more efficient training workflows.

--- Slide 30 ---

Case Studies
1 Image Preprocessing Pipeline for Deep Learning
Before feeding images into deep learning models, they must undergo a sequence of preprocessing steps to ensure consistency, improve learning efficiency, and enhance model accuracy. The image preprocessing pipeline plays a critical role in optimizing model training and performance.

Preprocessing Steps:
Resizing, normalization, and augmentation of image datasets.
GPU can significantly speed up these tasks, especially during training when large datasets are used.
Tools:
Libraries like OpenCV, TensorFlow, or PyTorch use GPU acceleration for image transformations.

--- Slide 31 ---

Case Studies
2. Financial Time-Series Feature Extraction
Financial time-series data consists of chronologically ordered data points representing values over time, such as stock prices, currency exchange rates, or trading volumes. Feature extraction in this context involves transforming raw time-series data into meaningful variables (features) that can be used by machine learning or deep learning models for forecasting, anomaly detection, and strategy development.
Feature Engineering in Financial Data:
Extract features like moving averages, volatility, momentum indicators, and statistical features.
GPU Acceleration:
Using parallel processing to speed up the computation of these features, especially for large datasets spanning over years of market data.

--- Slide 32 ---

Case Studies
3. Genomic Data Processing Pipeline
A genomic data processing pipeline is a structured sequence of computational steps used to analyze raw DNA or RNA sequencing data, typically obtained from next-generation sequencing (NGS) platforms. The goal is to transform raw reads into meaningful biological insights, such as identifying genetic variants, understanding gene expression, or detecting mutations.
Processing Genomic Data:
Tasks include aligning DNA sequences, performing variant calling, and DNA sequence analysis.
GPU Optimization:
The large size of genomic datasets benefits from GPU acceleration during sequence alignment and genomic feature extraction.

--- Slide 33 ---

CUDA Implementation
Memory Allocation and Transfers
Host (CPU) vs Device (GPU) memory.
Types of memory:
cudaMalloc(), cudaFree() – device memory
cudaMemcpy() – host-device transfers
Avoid excessive cudaMemcpy() calls to prevent bottlenecks.
float* d_data;
cudaMalloc(&d_data, size * sizeof(float));
cudaMemcpy(d_data, h_data, size * sizeof(float), cudaMemcpyHostToDevice);
Kernel Design Best Practices
Kernel: GPU function executed in parallel by multiple threads.
Best practices:
Use grid-stride loops.
Minimize divergence in warps.
Prefer shared memory for local thread blocks.
Avoid bank conflicts in shared memory.
__global__ void scale(float* data, float scale, int n) {
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    if (i < n) data[i] *= scale;
}

--- Slide 34 ---

CUDA Implementation
Streams and Concurrency
CUDA Streams = pipelines that allow overlapping data transfer and kernel execution.
Enable asynchronous execution.
Use cudaStreamCreate() and cudaMemcpyAsync().
cudaStream_t stream;
cudaStreamCreate(&stream);
cudaMemcpyAsync(d_data, h_data, size * sizeof(float), cudaMemcpyHostToDevice, stream);
Where,
d_data: destination pointer in device (GPU) memory.
h_data: source pointer in host (CPU) memory.
size * sizeof(float): number of bytes to copy.
cudaMemcpyHostToDevice: direction of data transfer.
stream: CUDA stream in which the copy should be scheduled.

--- Slide 35 ---

Frameworks
RAPIDS is a GPU-accelerated data science ecosystem based on CUDA.
cuDF: DataFrame-like operations (like pandas but on GPU)
cuML: GPU-accelerated ML algorithms (like scikit-learn)
cuGraph: Graph algorithms (like NetworkX but GPU-based)
TensorFlow Data API with GPU
TensorFlow pipelines can be GPU-accelerated using tf.data API and efficient tf.function.
PyTorch DataLoader Optimizations
Use num_workers > 0 and pin_memory=True in DataLoader.
Move batches to GPU using .to(device).

--- Slide 36 ---

CPU Vs GPU accelerated Approach

--- Slide 37 ---

Performance Optimization

--- Slide 38 ---

Performance OptimizationBenchmarking and Profiling1 Importance of Benchmarking and ProfilingBenchmarking helps measure performance under specific workloads.Profiling allows fine-grained analysis of code execution.Goals:Identify performance bottlenecksUnderstand memory and compute usageImprove throughput and resource utilization2 NVIDIA Nsight ToolsNsight Systems: System-wide profiling (CPU + GPU interactions)Nsight Compute: Kernel-level analysisVisual interface for timeline, API calls, memory usage, etc.Sample Use (Nsight Compute)nv-nsight-cu-cli ./my_cuda_appUse with flags for specific metrics.

--- Slide 39 ---

Performance Optimization contd..Benchmarking and Profiling3 CUDA Profiler MetricsOccupancy: Ratio of active warps to max possibleMemory Throughput: Global, shared, L2 cache bandwidthInstruction Throughput: How fast instructions are issuedWarp Execution Efficiency: % of threads active in warpsTools: nvprof (deprecated), ncu, Nsight GUI4 Identifying BottlenecksCompute-bound: Focus on kernel optimizationMemory-bound: Address access patterns and bandwidthLatency-bound: Look into kernel launch, synchronization delays

--- Slide 40 ---

Optimization Techniques
1 Memory Access PatternsCoalesced Access: Consecutive threads access consecutive memory addressesAvoid strided or unaligned access
// Good: Coalesced
int idx = threadIdx.x + blockDim.x * blockIdx.x;
a[idx] = b[idx];

// Bad: Strided
int idx = threadIdx.x + blockDim.x * blockIdx.x;
a[idx] = b[idx * 2];
2 Kernel Fusion
Combine multiple small kernels into one to reduce memory access and kernel launch overhead
Reduces global memory transactions
Use shared memory to combine operations within a single kernel

--- Slide 41 ---

Optimization Techniques contd..
3 Asynchronous Execution
Use streams to overlap computation and data transfer
Enable concurrency with cudaMemcpyAsync and multiple streams
Example:

cudaMemcpyAsync(dst, src, size, cudaMemcpyHostToDevice, stream)
my_kernel<<<blocks, threads, 0, stream>>>(...)

4 Multi-GPU Strategies
Data Parallelism: Split data across GPUs
Model Parallelism: Split model/layers across GPUs
Use NCCL (NVIDIA Collective Communication Library) for efficient communication
PyTorch Example (Data Parallelism):

from torch.nn import DataParallel
model = DataParallel(model)

--- Slide 42 ---

Deployment Strategies
Deployment Environments
Cloud GPU instances (AWS, GCP, Azure)
On-premise GPU clusters
Edge deployment considerations
Orchestration and Scaling
Kubernetes with GPU support
Workload scheduling
Auto-scaling strategies

--- Slide 43 ---

Cloud GPU Instances (AWS, GCP, Azure)
AWS GPU Instances:
P4/P3 (Tesla T4/V100) – Inference & Training
G5 (A10G) – Graphics & ML
EC2 Spot Instances for cost savings
GCP GPU Options:
T4, V100, A100 on Google Compute Engine
TPU v4 Pods for large-scale training
Azure GPU Offerings:
NCv3 (V100), ND (A100)
Azure ML Pipelines for MLOps

--- Slide 44 ---

On-Premise GPU Clusters
An on-premise GPU cluster is a group of GPU-equipped servers physically located and maintained within an organization's own data center or facility. These clusters are networked together and configured to run parallel computing tasks, typically for machine learning, deep learning, scientific simulations, or high-performance computing (HPC).

NVIDIA DGX Systems (A100, H100)
Kubernetes + GPU Operator for cluster management
Storage Considerations:
NVMe for fast I/O
Distributed FS (Lustre, CephFS)

--- Slide 45 ---

On-Premise GPU Clusters Advantages & Challenges
Advantages
Full Control: You can configure hardware/software to meet specific needs.
Data Security: Sensitive data stays within your network, reducing external threats.
No Ongoing Cloud Costs: Pay upfront for hardware—no recurring charges like cloud providers.
Challenges
High Initial Cost: Upfront investment in hardware and infrastructure.
Maintenance Overhead: Requires skilled IT staff for updates, hardware failures, and scaling.
Scalability: Adding new nodes requires physical setup and configuration.

--- Slide 46 ---

Edge Deployment Considerations
Deploying AI models on edge devices means running them directly on hardware that's close to the data source (like cameras, sensors, or IoT devices), rather than on centralized cloud servers. This brings unique challenges and opportunities.
NVIDIA Jetson: Embedded AI Platforms
NVIDIA Jetson boards are small yet powerful GPU-accelerated devices designed for edge AI. Key models include:
Jetson Orin:
Most powerful in the Jetson family
Suitable for high-throughput edge AI (e.g., real-time object detection with deep models)
Jetson Xavier:
Balance of performance and efficiency
Used in smart cities, robotics, drones
Jetson Nano:
Entry-level, ideal for simple AI applications and prototypes

--- Slide 47 ---

Edge Deployment Considerations
Latency & Bandwidth Constraints
Edge deployment must handle real-time requirements and limited connectivity:
Low Latency: Inference needs to be quick (e.g., in autonomous vehicles or surveillance).
Limited Bandwidth: Can't rely on cloud APIs—must process data locally.
Offline Capability: Devices often operate with intermittent or no internet.

--- Slide 48 ---

Model Optimization Techniques
Running models efficiently on edge hardware requires reducing model size and inference time:
a. Quantization
Convert model weights/activations from FP32 → FP16 or INT8
Reduces model size and speeds up inference
Minimal accuracy drop with good calibration
# Example in PyTorch
torch.quantization.convert(model, dtype=torch.qint8)
b. TensorRT (NVIDIA)
NVIDIA’s inference optimizer and runtime for deep learning models
Converts and optimizes models (from PyTorch, TensorFlow, ONNX)
Supports:
Layer fusion
Precision calibration (FP16/INT8)
Dynamic batching
Kernel auto-tuning
# Convert ONNX to TensorRT engine
trtexec --onnx=model.onnx --saveEngine=model.trt --fp16

--- Slide 49 ---

Model Optimization Techniques
Kubernetes with GPU Support
Key Components:
NVIDIA GPU Operator (automates driver install)
Node Feature Discovery (NFD) for GPU detection
Example YAML for GPU Pod:

--- Slide 50 ---

Model Optimization Techniques
Workload Scheduling

GPU-Aware Scheduling:
Kubernetes Device Plugins
Gang Scheduling (for multi-GPU jobs)
Example: Kubeflow for ML Workloads

Auto-Scaling Strategies

Cluster Autoscaler + GPU Nodes
Horizontal Pod Autoscaler (HPA) for Inference Workloads

--- Slide 51 ---

Monitoring and Maintenance of GPU-Accelerated SystemsGPU Health MonitoringEssential Metrics to Track:Temperature (GPU Core Temp)Power draw (Power Consumption)ECC Memory ErrorsFan speed (Fan Speed %)
Alert Thresholds Table:

--- Slide 52 ---

Model Optimization TechniquesGrafana Dashboard Example1. GPU Utilization Heatmap2. Memory Bandwidth Timeline3. Error Rate Monitoring
Performance Metrics Collection
Key Metrics:
GPU Utilization (utilization.gpu)
Memory Usage (memory.used/memory.total)
SM Occupancy
PCIe Throughput
Monitoring Stack:
Prometheus + Grafana Setup

--- Slide 53 ---

Error Handling and recovery
Common GPU Errors:
CUDA_ERROR_ILLEGAL_ADDRESS
CUBLAS_STATUS_ALLOC_FAILED
NVML_ERROR_THERMAL_VIOLATION
OOM (Out-of-Memory), CUDA kernel crashes, driver timeouts
Recovery Strategies:
Automated job retries with checkpointing
Fallback strategies (e.g., lower batch size)
Logging/alerting (Sentry, ELK Stack)

--- Slide 54 ---

Cost Optimization
1. GPU Utilization Tracking
Goal: Maximize ROI by avoiding idle resources
Methods:
Real-time dashboards (Grafana)
Historical analysis (e.g., peak vs. off-peak usage)
Optimization:
Dynamic scaling (Kubernetes, Slurm)
Multi-tenancy (shared GPUs for small jobs)
2. Spot Instance Strategies
Cloud-Specific Tactics:
AWS: Spot Blocks for critical jobs
GCP: Preemptible VMs + checkpointing
Azure: Low-priority VMs with fault tolerance
Best Practices:
Diversify instance types
Hybrid on-demand/spot fleets

--- Slide 55 ---

Cost Optimization contd..
3.  Mixed-Precision Techniques
Mixed-precision computing means using different numerical formats (like FP32, FP16, INT8) within the same model or computation to improve performance and reduce memory usage, without sacrificing much accuracy.
In mixed-precision training:
Weights and activations are stored in FP16
Accumulation (e.g., gradients, losses) is done in FP32 for numerical stability
How It Saves Costs:
Faster training → lower compute time
Implementation:
NVIDIA AMP (Automatic Mixed Precision)
TF32 (TensorFloat-32) for matrix ops
Caveats:
Verify model stability (gradient scaling)

--- Slide 56 ---

Academic References
"Efficient GPU Resource Management" (MLSys 2023)
NVIDIA "Best Practices for GPU Operations" Whitepaper
AWS "Cost Optimization for ML Workloads" Guide

--- Slide 57 ---

الشراكات العالمية

--- Slide 58 ---

شــــــكــــرًا لكــــــم
THANK YOU

### 09

--- Slide 1 ---

أكـــــاديميــــة طــــويـــق
Scalable Data Science

--- Slide 2 ---

Distributed ML with Spark MLlib
By: Dr. Afshan Hashmi

--- Slide 3 ---

Course Objectives:

Understand the fundamentals of distributed computing
Gain hands-on experience with Spark MLlib, 
Explore and implement supervised and unsupervised machine learning algorithms 
Learn how to build, tune, and evaluate ML models 
Develop the ability to optimize performance and resource

--- Slide 4 ---

Introduction to Distributed Machine Learning
What is Distributed Machine Learning?
Distributed Machine Learning (Distributed ML) is a technique where the training and processing of machine learning models are spread across multiple computers (also called nodes or machines) instead of relying on just one machine.

Simple Analogy: Imagine trying to build a Lego city. If one person does all the work, it takes a long time. But if 10 people build different sections at the same time, the city is completed much faster. Distributed ML works the same way—with machines instead of people.

--- Slide 5 ---

Why Use Distributed ML?
In today's world, machine learning models often deal with:
Massive datasets (like millions of images or billions of rows of user data).
Complex models (like deep neural networks with millions of parameters).
Trying to process these on a single machine would:
Be extremely slow.
Require more memory and power than the machine has.
Risk data loss if the machine fails.
That’s why we distribute the work across many machines, enabling efficient training and processing.

--- Slide 6 ---

Key Benefits of Distributed ML

--- Slide 7 ---

How Does It Work?
Distributed ML typically uses:

Data Parallelism:Each machine trains on a different portion of the data using the same model, then synchronizes the results (like weights).

Model Parallelism:A single large model is split across machines; each machine trains a part of the model.

Hybrid Parallelism:Combination of both data and model parallelism.

--- Slide 8 ---

Popular Tools & Frameworks

--- Slide 9 ---

Real-World Examples
Google Translate: Trained across thousands of machines using data from multiple languages.

Self-Driving Cars: Models trained with distributed frameworks using video feeds from millions of driving hours.

Amazon & Netflix: Distributed recommendation systems trained using huge datasets of user preferences.

--- Slide 10 ---

Introduction to Apache Spark
What is Apache Spark?
Apache Spark is an open-source, distributed computing system designed for fast and scalable data processing. It provides a unified engine that supports both batch and real-time analytics over large datasets, making it a go-to solution for Big Data processing and machine learning pipelines.

 Key Features:
High-Speed Processing: Performs in-memory computations (RAM instead of disk), which makes it up to 100x faster than traditional big data systems like Hadoop MapReduce.

Ease of Use: Offers APIs in Python (PySpark), Java, Scala, and R.

Versatility: Supports diverse workloads – ETL, streaming, graph processing, SQL, and machine learning – all within one framework.

--- Slide 11 ---

Core Components of Apache Spark

--- Slide 12 ---

Why Use Apache Spark?
Designed for high-volume data workloads.
Works with multiple cluster managers: Hadoop YARN, Apache Mesos, Kubernetes, or standalone.
Integrates with data lakes, databases, cloud storage, and streaming platforms.
Example Use Case:
Scenario: A bank wants to detect fraudulent transactions in real-time.
Use Spark Streaming to ingest transaction data from Kafka.
Apply Spark MLlib to classify transactions using a trained fraud detection model.
Store and query results using Spark SQL.

--- Slide 13 ---

Spark MLlib Overview
What is MLlib?
MLlib (Machine Learning Library) is Apache Spark’s scalable machine learning library. It provides a wide range of machine learning algorithms and utilities that are distributed across clusters, making it highly efficient for handling large datasets.
MLlib is designed to scale easily with big data, enabling developers and data scientists to build and deploy models on massive datasets without managing distributed systems manually.
Built on Spark Core (RDDs/DataFrames).
Supports:
Classification, Regression, Clustering (e.g., Logistic Regression, K-Means).
Feature Engineering (PCA, Tokenization).
Pipelines (end-to-end ML workflows).

MLlib vs. Other Libraries

--- Slide 14 ---

What Can You Do with MLlib?
MLlib supports:

--- Slide 15 ---

Supported Languages
You can use MLlib with multiple languages:

Scala – Native and most optimized.

Python (PySpark) – Popular among data scientists and Python developers.

Java – For enterprise-grade applications.

R – For statistical computing and analysis (via SparkR or Sparklyr).

--- Slide 16 ---

Key Features of MLlib
1. Scalable and Distributed Algorithms
All algorithms are parallelized across clusters using Spark’s distributed processing engine.
Allows training models on terabytes of data without running into memory issues.
2. ML Pipelines (Inspired by Scikit-learn)
MLlib uses a high-level Pipeline API to create machine learning workflows.
Components include:
Transformers (e.g., StandardScaler)
Estimators (e.g., LogisticRegression)
Evaluators (e.g., BinaryClassificationEvaluator)
Enables chaining together multiple stages: preprocessing → training → evaluation → tuning.
3. Tight Integration with Spark SQL and DataFrames
MLlib supports DataFrame-based APIs, making it easier to preprocess structured data.
You can perform SQL queries, data wrangling, and ML model training within the same environment.

--- Slide 17 ---

Advantages of MLlib
Handles Big Data Efficiently – Can process data that wouldn’t fit into memory on a single machine.
Unified Stack – Integrates well with other Spark components like Spark SQL and Streaming.
Easy to Scale – Just add more nodes to the cluster to improve performance.

When to Use MLlib?
You need to apply machine learning on big datasets (millions of records).
You want end-to-end pipelines for data ingestion, transformation, modeling, and evaluation.
You need scalability and distributed computing without managing the complexity of setting it up yourself.

--- Slide 18 ---

MLlib Architecture – A Deep Dive
Apache Spark MLlib is built to streamline the end-to-end machine learning pipeline in a distributed, scalable, and high-performance environment.

Raw Data → DataFrame → Feature Transformation → ML Model → Evaluation → Prediction
This pipeline resembles a real-world machine learning workflow and consists of the following stages:

--- Slide 19 ---

Main Components of MLlib Architecture
DataFrames & Pipelines

DataFrames: Core data structure in Spark (like Pandas DataFrame but distributed).
Enables efficient, distributed computations.
Supports schema, data types, and SQL-like querying.
Pipeline API: Allows chaining multiple stages (like Scikit-learn):
Pipeline(stages=[Stage1, Stage2, ..., StageN])
Manages both data preprocessing and model training in a unified structure.

--- Slide 20 ---

Main Components of MLlib Architecture
2. Feature Transformers
Transformers convert raw data into features usable by ML algorithms:
assembler = VectorAssembler(inputCols=["age", "income"], outputCol="features")
indexer = StringIndexer(inputCol="gender", outputCol="gender_index")

--- Slide 21 ---

Main Components of MLlib Architecture
from pyspark.ml.classification import LogisticRegression
lr = LogisticRegression(featuresCol="features", labelCol="label")
3. Machine Learning Algorithms
MLlib supports a wide variety of scalable ML algorithms:

--- Slide 22 ---

Main Components of MLlib Architecture
from pyspark.ml.evaluation import BinaryClassificationEvaluator
evaluator = BinaryClassificationEvaluator(labelCol="label", metricName="areaUnderROC")
4. Evaluators
Used to evaluate model performance:

--- Slide 23 ---

MLlib Architecture

--- Slide 24 ---

Commonly Used Algorithms in MLlib

--- Slide 25 ---

Hands-on Example:MLlib Taxi: Scalable Trip Time ForecastingClick here for the labhttps://drive.google.com/file/d/1nsrMt-wQYqho_nNg9pxqLz6JhMh42n0l/view?usp=share_link

--- Slide 26 ---

Summary:

--- Slide 27 ---

Academic References
MLlib Official Documentation
Databricks Learning Resources
[Book] Advanced Analytics with Spark – O’Reilly
PySpark Examples GitHub Repo

--- Slide 28 ---

الشراكات العالمية

--- Slide 29 ---

شــــــكــــرًا لكــــــم
THANK YOU

### 10

--- Slide 1 ---

أكـــــاديميــــة طــــويـــق
Scalable Data Science

--- Slide 2 ---

cuDF: GPU-accelerated Data Manipulation
Overview and Comparison with Pandas
By: Dr. Afshan Hashmi

--- Slide 3 ---

Course Objectives:
This course aims to equip learners with GPU-accelerated data analysis skills using cuDF, Pandas. Students will learn how to efficiently manipulate, clean, and analyze large datasets
Course Learning Outcomes:
1. Understand GPU-accelerated computing and how cuDF differs from Pandas for big data processing.2. Perform efficient data analysis using cuDF, including data cleaning, aggregation, and transformation.

--- Slide 4 ---

Introduction to cuDF
What is cuDF?
cuDF is a GPU DataFrame library for loading, joining, aggregating, filtering, and otherwise manipulating data.
GPU-accelerated library for data manipulation.
Part of the RAPIDS ecosystem.
Why use cuDF?
Leverage GPU power for faster data processing.
Designed for large datasets.

--- Slide 5 ---

Key Features of cuDF
GPU-accelerated DataFrame operations.
Similar API to Pandas for ease of use.
Seamless integration with other RAPIDS libraries (cuML, cuGraph).
Support for CSV, Parquet, and ORC file formats.

--- Slide 6 ---

cuDF vs Pandas
Performance Comparison:
cuDF is faster for large datasets due to GPU acceleration.
Pandas is better for small datasets (CPU overhead).
API Similarity:
cuDF mimics Pandas API for easy adoption.
Memory Management:
cuDF uses GPU memory; Pandas uses CPU memory.

--- Slide 7 ---

Set Up:Running with an NVIDIA GPU
NVIDIA® T4 GPU accelerates diverse cloud workloads, including high-performance computing, deep learning training and inference, machine learning, data analytics, and graphics.

--- Slide 8 ---

Data Analysis Using Pandas
Dataset used:
https://data.rapids.ai/datasets/nyc_parking/nyc_parking_violations_2022.parquet

--- Slide 9 ---

Data Analysis Using Pandas

--- Slide 10 ---

Data Analysis Using Pandas
To find the most common parking violation per U.S. state, based on vehicle registration, we used Pandas. We analyzed a dataset with state and violation data, using GroupBy and value_counts to determine the top offense for each state.
Method chaining is used  to combine a series of operations into a single statement

--- Slide 11 ---

Most common parking violation per U.S. state, based on vehicle registration

--- Slide 12 ---

Identifying the vehicle body types that most commonly receive parking violations is a key area of analysis
Output

--- Slide 13 ---

To find out the parking violation across the day of the week
A dictionary is created to map numerical weekday values (0-6) to their corresponding names.
The "Issue Date" column is converted to a datetime format (datetime64[ms]), enabling date-based operations.
.dt.weekday extracts the day of the week as an integer (0-6).
.map(weekday_names) converts this integer into the corresponding weekday name (e.g., 0 -> "Monday").
The data is grouped by "issue_weekday" (day of the week).
The number of violations ("Summons Number") is counted for each weekday.
.sort_values() sorts the results in ascending order to show which day had the fewest to the most violations.

--- Slide 14 ---

OUTPUT
A noticeable decrease in parking violations occurs during weekends, likely due to reduced weekday traffic in New York City.

--- Slide 15 ---

Starting with  cuDF.Pandas
To demonstrate the performance benefits of cudf.pandas, we will re-execute the previously used Pandas code.

 To accurately simulate a typical workflow, where cudf.pandas is loaded at the beginning, we have restarted the kernel prior to this execution.

--- Slide 16 ---

Pandas Vs  cuDF.Pandas
It is clear that Pandas has taken 7.01 seconds for the same task while cuDF Pandas has taken 1.3 seconds

--- Slide 17 ---

Pandas Vs  cuDF.Pandas
It is clear that Pandas has taken 884 milli-seconds for the same task while cuDF Pandas has taken only  27.2milli-seconds

--- Slide 18 ---

Pandas Vs  cuDF.Pandas
It is clear that Pandas has taken 8.51 seconds for the same task while cuDF Pandas has taken 297 milli-seconds

--- Slide 19 ---

Quiz TimeAnalyze Violations by Day of the Week and Vehicle Type

--- Slide 20 ---

Quiz Time- Solution1. Analyze Violations by Day of the Week and Vehicle Type

--- Slide 21 ---

Quiz Time2. Find the Top 5 Most Common Parking Violations

--- Slide 22 ---

Quiz Time- Solution2. Find the Top 5 Most Common Parking Violations

--- Slide 23 ---

Quiz Time3. Identify States with the Highest Number of Violations

--- Slide 24 ---

Quiz Time4. Find the Monthly Trend of Parking Violations

--- Slide 25 ---

Quiz Time- Solution4. Find the Monthly Trend of Parking Violations

--- Slide 26 ---

Quiz Time5.Find the Most Common Violation for Each Vehicle Type

--- Slide 27 ---

Quiz Time- Solution5.Find the Most Common Violation for Each Vehicle Type

--- Slide 28 ---

RECAP
GPU-Accelerated DataFrames – cuDF is a Pandas-like DataFrame library that runs on NVIDIA GPUs, enabling high-speed data processing.

Pandas-Compatible API – cuDF supports most Pandas functions (read_parquet(), groupby(), merge(), etc.), making it easy to transition from CPU-based Pandas workflows.

 Efficient Large-Scale Data Processing – cuDF is optimized for millions to billions of rows, outperforming Pandas in data manipulation, filtering, and aggregation.

Best Use Cases for cuDF – Ideal for big data processing, ETL (Extract, Transform, Load) tasks, and data preparation before feeding into deep learning models.

--- Slide 29 ---

Practical Implementation
Go To Google Colab

--- Slide 30 ---

الشراكات العالمية

--- Slide 31 ---

شــــــكــــرًا لكــــــم
THANK YOU

### 11

--- Slide 1 ---

أكـــــاديميــــة طــــويـــق
Scalable Data Science

--- Slide 2 ---

Unit 5: Cloud Infrastructure & Production Deployment
Introduction to Cloud Computing
By: Dr. Afshan Hashmi

--- Slide 3 ---

Course Objectives:

Define cloud computing and its key characteristics.
Compare different cloud service models (IaaS, PaaS, SaaS).
Explain the benefits and challenges of cloud computing.
Identify major cloud providers (AWS, Azure, GCP) and their core services.
Demonstrate setting up a basic cloud instance (e.g., AWS EC2, Google Compute Engine).

--- Slide 4 ---

Introduction to Cloud Computing
Cloud computing is the delivery of computing services—such as servers, storage, databases, networking, software, analytics, and intelligence—over the Internet ("the cloud") to offer faster innovation, flexible resources, and economies of scale.

Key Characteristics:
On-Demand Self-Service: Users can provision computing resources as needed without human intervention from the provider.

Broad Network Access: Available over the network and accessed through standard mechanisms (e.g., laptops, phones).

Resource Pooling: Multiple customers are served from the same physical resources, which are dynamically assigned.

Rapid Elasticity: Capabilities can scale up or down quickly.

Measured Service: Usage is monitored and billed based on consumption.

--- Slide 5 ---

Cloud Service Models:

--- Slide 6 ---

IaaS (Infrastructure as a Service)
IaaS is one of the primary cloud computing service models.It provides virtualized computing 
resources over the internet, such as virtual machines (VMs), storage, and networking. With IaaS, 
users can rent infrastructure on demand instead of buying and maintaining physical servers.
Key Features:
Users get complete control over the operating system and applications.
It is highly scalable and ideal for quickly growing businesses.
Pay-as-you-go pricing model—only pay for what you use.
Examples:
Amazon EC2 (Elastic Compute Cloud)
Google Compute Engine
Microsoft Azure Virtual Machines
Use Cases:
Hosting websites and applications
Test and development environments
Data backup and recovery
High-performance computing

--- Slide 7 ---

PaaS (Platform as a Service)
PaaS (Platform as a Service) is a category of cloud computing services that provides a platform allowing customers to develop, run, and manage applications without dealing with the complexity of building and maintaining the underlying infrastructure (like servers, storage, or networks).
Key Features of PaaS:
Development Tools: Integrated development environments (IDEs), version control, and debugging tools.
Middleware: Pre-built components that enable communication between different parts of the application.
Database Management: Built-in database services for storage, queries, and analytics.
Scalability: Automatically scales applications based on demand.
Deployment Automation: Simplifies and speeds up app deployment and updates.
Examples:
Google App Engine – Allows developers to build and host applications in Google-managed data centers.
Heroku – A platform that supports several programming languages and simplifies app deployment.

--- Slide 8 ---

SaaS (Software as a Service)
SaaS (Software as a Service) is a cloud computing model in which software applications are delivered over the internet and accessed through a web browser, rather than being installed on individual devices. This means users don’t have to worry about infrastructure, platform management, or software updates everything is handled by the service provider.

Key Features of SaaS:
Accessible via browser: No installation needed; runs on any device with internet access.
Subscription-based: Typically paid monthly or annually.
Automatic updates: The provider manages upgrades and maintenance.
Scalable: Easily add or remove users as needed.

Examples:
Google Workspace: Gmail, Docs, Sheets, Drive—all available in-browser.
Microsoft 365: Cloud versions of Word, Excel, PowerPoint.
Salesforce: CRM software accessed over the web.

--- Slide 9 ---

Cloud Deployment Models
These define how cloud services are made available to users. There are three main types:
 1. Public Cloud
Services are provided over the public internet.
Anyone can use them—individuals or organizations.
Managed by third-party providers like:
Amazon Web Services (AWS)
Microsoft Azure
Google Cloud Platform (GCP)
Example: Hosting a website on AWS that anyone can visit.
.

--- Slide 10 ---

Cloud Deployment Models
2. Private Cloud
Used by a single organization only.
Can be hosted on-premises or by a third party.
Offers greater control and security.
Best for organizations with strict regulatory or data privacy needs.
Example: A bank using a private cloud to store customer data securely

3.Hybrid Cloud
Combination of public and private clouds.
Allows data and applications to move between the two environments.
Offers flexibility:
Keep sensitive data in the private cloud
Use the public cloud for less sensitive tasks or to handle peak loads
Example: A company runs payroll apps in a private cloud but uses public cloud resources to process reports during tax season.
.

--- Slide 11 ---

Benefits of Cloud Computing
Cost Efficiency – Cloud computing reduces the capital expense of buying hardware and software. You pay only for the services you use (pay-as-you-go), making it economical, especially for startups and small businesses.

Scalability – It allows businesses to scale resources up or down as needed. Whether you're running a small website or a large e-commerce platform, cloud services adjust to your demands instantly.

Flexibility and Mobility – Users can access data and applications from anywhere with internet access. This supports remote work, real-time collaboration, and increased productivity.

Disaster Recovery – Cloud providers typically offer built-in backup and disaster recovery solutions, reducing downtime and data loss in case of unexpected failures.
Security and Compliance Options – Most cloud platforms offer robust security features such as encryption, identity access management, and compliance certifications (e.g., HIPAA, GDPR).
.

--- Slide 12 ---

Why Use Cloud Computing?
Benefits:
Cost Efficiency: No upfront hardware costs.
Scalability: Instantly handle traffic spikes (e.g., Black Friday sales).
Reliability: 99.9% uptime SLAs.
Global Reach: Deploy in multiple regions (e.g., AWS’s 25+ geographic regions).

Challenges:
Security concerns (shared responsibility model).
Vendor lock-in.
Latency for real-time applications.

Case Study:
How Airbnb scaled using AWS: Migrated from physical servers to cloud for global scalability.
.

--- Slide 13 ---

Major Cloud Providers Details
.

--- Slide 14 ---

Real-World Use Cases
Hosting Websites and Apps: Platforms like AWS and Azure host millions of web applications for scalability and availability.
Data Storage and Backup: Services like Google Drive, Dropbox, or AWS S3 provide safe, scalable cloud storage.
Big Data Analytics: Companies use cloud tools (e.g., Google BigQuery, AWS Redshift) to analyze vast amounts of data efficiently.
AI and Machine Learning Deployment: Cloud platforms enable training, deployment, and scaling of ML models (e.g., Google Vertex AI, Azure ML).
Content Delivery: Streaming platforms like Netflix and YouTube use Content Delivery Networks (CDNs) in the cloud to deliver content smoothly to global users.
.

--- Slide 15 ---

Summary:
Cloud computing delivers computing services (e.g., storage, servers, software) over the internet to enable scalability, flexibility, and cost-efficiency.
It features on-demand self-service, broad network access, resource pooling, rapid elasticity, and measured service.
Service models include:
IaaS (Infrastructure as a Service): Offers virtual machines and storage (e.g., AWS EC2).
PaaS (Platform as a Service): Provides development tools and frameworks (e.g., Heroku).
SaaS (Software as a Service): Delivers software via web browsers (e.g., Google Workspace).
Deployment models are:
Public cloud (shared across multiple users),
Private cloud (exclusive to one organization),
Hybrid cloud (mix of public and private).
Benefits include cost savings, ease of scalability, remote access, disaster recovery, and strong security options.
Common use cases include hosting websites, storing and analyzing big data, deploying AI/ML models, and streaming content.

--- Slide 16 ---

Resources & Further Reading
Cloud Computing: Concepts, Technology & Architecture by Thomas Erl
A foundational book explaining core cloud concepts, service models, and architectures.
Cloud Computing: Principles and Paradigms by Rajkumar Buyya et al.
Covers academic and practical perspectives on cloud deployment models, services, and research trends.
AWS, Azure & Google Cloud Official Documentation
Authoritative, real-world references for learning IaaS, PaaS, SaaS implementations.
AWS | Azure | GCP
Architecting the Cloud by Michael J. Kavis
A hands-on guide for IT professionals designing and deploying scalable cloud architectures.

--- Slide 17 ---

الشراكات العالمية

--- Slide 18 ---

شــــــكــــرًا لكــــــم
THANK YOU

### 12

--- Slide 1 ---

أكـــــاديميــــة طــــويـــق
Scalable Data Science

--- Slide 2 ---

Model Training on Large Datasets
By: Dr. Afshan Hashmi

--- Slide 3 ---

Course Objectives:
Understand the challenges of training models on large datasets
Apply best practices for handling large data efficiently
Choose the right tools and infrastructure (e.g., distributed computing, cloud-based ML, GPUs)
Optimize training using batching, sampling, and efficient data loading techniques

--- Slide 4 ---

Introduction to Large-Scale Model Training
Why Large-Scale Training Matters
Modern datasets exceed single-machine memory (e.g., TB-scale images, logs)
Need for faster iteration in production ML systems
Regulatory/compliance requirements for model reproducibility
Key Challenges
When to Scale?
Dataset > 10GB (in-memory limits)
Training time > 4 hours on single machine
Need for frequent retraining (streaming data)

--- Slide 5 ---

Strategies for Efficient Training
1.Data Sampling and Mini-Batching
These are techniques used to efficiently train machine learning models, especially when dealing with large datasets that can't fit into memory all at once.
A. Train on mini-batches instead of full data
Why?
Training on the entire dataset (full batch) at once consumes a lot of memory and can be very slow.
Instead, we split the dataset into mini-batches (small chunks of data) and feed one batch at a time to the model.
Benefits:
Lower memory usage.
More frequent updates to model weights → faster convergence.
Enables parallelization and efficient GPU usage.

--- Slide 6 ---

Strategies for Efficient Training
B. Use stratified sampling to maintain class balance
What is it?
When creating mini-batches, stratified sampling ensures that each batch has the same class distribution as the overall dataset.
Why is it important?
Prevents the model from being biased toward majority classes.
Ensures better generalization and more stable training especially in imbalanced datasets.
C. Common in TensorFlow and PyTorch: batch_size in DataLoader
Both TensorFlow and PyTorch use the concept of mini-batches during training.
You define the batch_size (number of samples per batch) when creating a data loader.
Efficient training strategies like mini-batching and stratified sampling help manage memory usage, speed up training, and improve model performance,especially when working with large or imbalanced datasets.

--- Slide 7 ---

Strategies for Efficient Training
2.Data Generators / Streaming
This strategy is about loading only the data you need, when you need it, instead of loading everything into memory at once — perfect for large datasets.
Why Use It?
When your dataset is too large to fit into RAM, you:
Don’t load the whole dataset into memory.
Instead, stream data on the fly — this is called lazy loading.
This technique is commonly implemented through data generators or custom dataset loaders.
How It Works:
You write or use a generator function that:
Loads a small piece of the data (e.g., an image or a batch of rows).
Processes it (if needed).
Yields it to the model for training or prediction.

--- Slide 8 ---

Strategies for Efficient Training
Popular Frameworks & Tools
TensorFlow – tf.data API
tf.data.Dataset can load and preprocess data efficiently using generators, lazy loading, and pipelines.
Example:
import tensorflow as tf

def generator():
    for file in image_files:
        yield load_image(file), load_label(file)

dataset = tf.data.Dataset.from_generator(generator)
dataset = dataset.batch(32).prefetch(tf.data.AUTOTUNE)

--- Slide 9 ---

Strategies for Efficient Training
PyTorch – Dataset and DataLoader
Create a custom Dataset class with __getitem__ to load only one item at a time.
DataLoader then wraps this to handle mini-batches, shuffling, and multiprocessing.
from torch.utils.data import Dataset, DataLoader

class MyDataset(Dataset):
    def __init__(self, file_paths):
        self.file_paths = file_paths

    def __len__(self):
        return len(self.file_paths)

    def __getitem__(self, idx):
        data = load_data(self.file_paths[idx])
        label = load_label(self.file_paths[idx])
        return data, label

dataset = MyDataset(file_paths)
loader = DataLoader(dataset, batch_size=32, shuffle=True)

--- Slide 10 ---

Strategies for Efficient Training
Dask – For Large Tabular Data
Dask DataFrames are like Pandas, but they load and process data in chunks (partitions).
Ideal for big tabular data that doesn’t fit into memory.
import dask.dataframe as dd

df = dd.read_csv('large_dataset.csv')
filtered = df[df['label'] == 1]
result = filtered.compute()
Using generators or streaming:
Saves memory by not loading the full dataset.
Works great for large image/text/tabular datasets.
Frameworks like TensorFlow, PyTorch, and Dask provide built-in support for this.

--- Slide 11 ---

Strategies for Efficient Training
3. Using Cloud & Distributed Resources
When your model or dataset is too large to train efficiently on a single machine (like your laptop), you can turn to cloud platforms and distributed computing to scale up training.

Why Use Cloud and Distributed Resources?
To train faster by using powerful cloud GPUs or TPUs.
To scale horizontally (i.e., use multiple machines) for very large datasets or deep learning models.
To save time and avoid limitations of local hardware.

Popular Cloud Training Platforms

Google Cloud AI Platform
Offers managed services for training ML models.
Supports TensorFlow, PyTorch, XGBoost, etc.
You can train using GPUs/TPUs on the cloud without managing infrastructure.

--- Slide 12 ---

Strategies for Efficient Training
b). AWS SageMaker
End-to-end ML service on Amazon Cloud.
Train, tune, deploy, and monitor models.
Built-in support for distributed training and pre-built ML containers.
Key feature: "Bring Your Own Model" or use built-in algorithms.


c). Databricks (with Spark + MLlib)
Ideal for big data + machine learning workflows.
Combines Apache Spark for distributed data processing with MLlib for scalable ML algorithms.
Great for tabular data, recommendation systems, etc.

--- Slide 13 ---

Strategies for Efficient Training
Distributed Training Frameworks
a. Horovod
Open-source framework from Uber.
Allows distributed training across GPUs and nodes.
Works with TensorFlow, PyTorch, and MXNet.
Use case: Train deep learning models across many GPUs/nodes in parallel.
b.  PyTorch DDP (Distributed Data Parallel)
Native PyTorch module for distributed training.
Replicates your model across multiple GPUs/machines.
Each replica handles a portion of the data.
torch.nn.parallel.DistributedDataParallel(model)

--- Slide 14 ---

Strategies for Efficient Training
4. Model Checkpointing
Checkpointing means saving your model’s progress (usually the learned weights) at different stages during training so you don’t lose all your work if something goes wrong (e.g., crash, power loss).

Why is it Important?
Avoids restarting from the beginning if training is interrupted.
Helps you resume training from the last saved point.
You can save the best version of your model (based on validation accuracy or loss).
Useful for long training jobs that can take hours or days.

What Does a Checkpoint Store?
Typically includes:
Model architecture (optional, if not already defined in code)
Weights/parameters (learned during training)
Optimizer state (so training resumes smoothly)

--- Slide 15 ---

Strategies for Efficient Training
4. Model Checkpointing
When to Save Checkpoints?
After every epoch
After every N batches
When validation loss improves
At fixed time intervals
Examples in Code
TensorFlow / Keras:
from tensorflow.keras.callbacks import ModelCheckpoint

checkpoint_cb = ModelCheckpoint("model_checkpoint.h5", save_best_only=True)
model.fit(X_train, y_train, epochs=10, callbacks=[checkpoint_cb])
save_best_only=True means it saves only when the model improves on validation set.

--- Slide 16 ---

Strategies for Efficient Training
4. Model Checkpointing
PyTorch:
torch.save(model.state_dict(), 'model_checkpoint.pth')  # to save

model.load_state_dict(torch.load('model_checkpoint.pth’)) # to load
You can wrap this in a condition like:
if epoch % 5 == 0:
    torch.save(model.state_dict(), f'model_epoch_{epoch}.pth')

--- Slide 17 ---

Strategies for Efficient Training
5. Using GPU/TPU Acceleration

Training machine learning (especially deep learning) models can be very slow on regular CPUs. GPUs and TPUs are specialized hardware that speed up training significantly by handling computations in parallel.
What are GPUs and TPUs?

GPU (Graphics Processing Unit) – Designed to handle thousands of parallel computations. Great for deep learning, especially for tasks like matrix multiplication (used heavily in neural networks).

TPU (Tensor Processing Unit) – Custom hardware developed by Google for fast TensorFlow operations. Even faster for certain tasks like large-scale training and inference.

--- Slide 18 ---

Strategies for Efficient Training
5. Using GPU/TPU Acceleration
Popular Frameworks & Tools for GPU/TPU Use
cuML (from NVIDIA RAPIDS)
A GPU-accelerated ML library.
Offers scikit-learn-like API with much faster performance using CUDA.
Example:
from cuml.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train, y_train)
TensorFlow / PyTorch with CUDA
Both TensorFlow and PyTorch can automatically use the GPU if available.
PyTorch example:
device = "cuda" if torch.cuda.is_available() else "cpu"
model = MyModel().to(device)
TensorFlow example:
# Automatically uses GPU if available
model.fit(X_train, y_train)

--- Slide 19 ---

Strategies for Efficient Training
Additional Tricks to Speed Up Training
6. Batch Normalization
Normalizes inputs to each layer, which stabilizes and accelerates training.
Helps in faster convergence and can allow higher learning rates.
Example (Keras):
from tensorflow.keras.layers import BatchNormalization
model.add(BatchNormalization())
7. Mixed Precision Training
Uses 16-bit (half) precision instead of 32-bit floats.
Speeds up training and reduces memory usage while maintaining accuracy.
Especially effective on NVIDIA GPUs with Tensor Cores or TPUs.
from tensorflow.keras import mixed_precision
mixed_precision.set_global_policy('mixed_float16')

--- Slide 20 ---

Strategies for Efficient Training
Additional Tricks to Speed Up Training
PyTorch Example:
from torch.cuda.amp import GradScaler, autocast
scaler = GradScaler()
for data in dataloader:
    with autocast():
        outputs = model(inputs)
        loss = loss_fn(outputs, targets)
    scaler.scale(loss).backward()
    scaler.step(optimizer)
    scaler.update()

--- Slide 21 ---

Memory-Efficient Data Type
When working with large datasets, every byte matters. Using smaller data types can significantly reduce memory usage which speeds up processing and allows you to train models more efficiently.
Why Optimize Data Types?
Lower memory usage
Faster data loading and processing
Less strain on RAM or GPU memory
Helps prevent "out of memory" errors

Common Optimizations:

--- Slide 22 ---

Memory-Efficient Data Type
Reducing Categorical Memory with category
df['color'] = df['color'].astype('category')
If you have a column with many repeated string values (like "red", "blue", "green"), converting it to category can save tons of memory.
Example: Memory Comparison
# Before
df.memory_usage(deep=True)

# After downcasting
df['price'] = pd.to_numeric(df['price'], downcast='float')
df['count'] = pd.to_numeric(df['count'], downcast='integer')

df.memory_usage(deep=True)

--- Slide 23 ---

Memory-Efficient Data Type
Benefits of changing Data Type

--- Slide 24 ---

Toolkits and Libraries Overview

--- Slide 25 ---

Tool-by-Tool Explanation:
Dask / Joblib
Dask: Allows you to work with large tabular datasets by parallelizing operations across CPUs or clusters.
Joblib: Commonly used to parallelize loops or cache functions in scikit-learn.
Spark MLlib
Part of Apache Spark, designed for distributed ML.
Ideal when working with very large datasets stored in Hadoop or data lakes.
cuML (NVIDIA RAPIDS)
GPU-powered version of scikit-learn APIs.
Speeds up classical ML algorithms (e.g., k-means, PCA, logistic regression) using NVIDIA GPUs.
TFRecords (TensorFlow)
A binary file format for storing large datasets (e.g., images, text).
Used with tf.data for efficient streaming during training.
PyTorch Lightning
High-level wrapper over PyTorch.
Helps you structure your code for clean, scalable, and reproducible training.
Handles logging, checkpointing, and training loops automatically.
Petastorm
Developed by Uber.
Lets you read large Parquet files efficiently into PyTorch or Spark.
Supports streaming from remote storage like S3.

--- Slide 26 ---

Tool-by-Tool Explanation:
Dask / Joblib
Dask: Allows you to work with large tabular datasets by parallelizing operations across CPUs or clusters.
Joblib: Commonly used to parallelize loops or cache functions in scikit-learn.
Spark MLlib
Part of Apache Spark, designed for distributed ML.
Ideal when working with very large datasets stored in Hadoop or data lakes.
cuML (NVIDIA RAPIDS)
GPU-powered version of scikit-learn APIs.
Speeds up classical ML algorithms (e.g., k-means, PCA, logistic regression) using NVIDIA GPUs.
TFRecords (TensorFlow)
A binary file format for storing large datasets (e.g., images, text).
Used with tf.data for efficient streaming during training.
PyTorch Lightning
High-level wrapper over PyTorch.
Helps you structure your code for clean, scalable, and reproducible training.
Handles logging, checkpointing, and training loops automatically.
Petastorm
Developed by Uber.
Lets you read large Parquet files efficiently into PyTorch or Spark.
Supports streaming from remote storage like S3.

--- Slide 27 ---

Case Studies & Benchmarks
Case Study 1: Recommendation Systems at Netflix
Scale: 100TB+ user interaction data
Solution: Spark ALS with model sharding
Outcome: 8x faster training vs. single-node

Case Study 2: Computer Vision at Tesla
Scale: Millions of auto-labeled images
Solution: PyTorch + Horovod on GPU cluster
Trick: Gradient compression for cross-region sync
Performance Benchmarks

--- Slide 28 ---

Challenges & Future Trends
Current Challenges
Straggler Problem: Slow workers delay synchronization
Data Skew: Uneven partition sizes hurt parallelism
Debugging Complexity: Hard to trace distributed failures

Emerging Solutions
Zero Redundancy Optimizer (ZeRO): Memory optimization
Serverless ML: AWS SageMaker, Google Vertex AI
Quantum ML: Early experiments with QPUs

--- Slide 29 ---

Summary
Efficient training = smart data handling + parallelism + resource optimization
Tools like Dask, Spark, cuML, and cloud platforms are essential
Don’t load full data into memory—stream, batch, or partition it
Evaluate models iteratively with checkpoints and logging

--- Slide 30 ---

Resources & Further Reading
Dask ML Docs
cuML GitHub
Spark MLlib Guide
Efficient Data Loading with PyTorch
"Designing Machine Learning Systems" - Chip Huyen
"Distributed Machine Learning Patterns" - Yuan Tang

--- Slide 31 ---

الشراكات العالمية

--- Slide 32 ---

شــــــكــــرًا لكــــــم
THANK YOU

### 13

--- Slide 1 ---

أكـــــاديميــــة طــــويـــق
Scalable Data Science

--- Slide 2 ---

cuDF: Understsanding performance and visualization
Analyzing Performance by profiling utilities
By: Dr. Afshan Hashmi

--- Slide 3 ---

Course Objectives:
To introduce the fundamentals of cudf.pandas and its role in accelerating data processing using GPUs.
To equip learners with profiling techniques for optimizing performance and identifying GPU vs. CPU execution in data workflows.
To explore data visualization techniques using third-party libraries like Plotly with cudf.pandas.

--- Slide 4 ---

Numba: Just-In-Time (JIT) Compilation for Speeding Up Python Code
Numba is a Python library that accelerates code execution using JIT compilation.

Converts Python code into machine code at runtime for improved performance.

It is particularly useful for speeding up numerical computations without requiring extensive rewrites of Python code.

Numba works well with NumPy, allowing array operations to be executed much faster.

Key Features:
Easy to use with minimal code changes.
Supports CPU and GPU acceleration.
Compatible with NumPy, SciPy, and other Python libraries.

--- Slide 5 ---

Why Use Numba?
Benefits:
Speed: Dramatically improves performance of numerical computations.
Simplicity: Requires only a decorator to optimize functions.
Flexibility: Works with existing Python code and libraries.
Use Cases:
Scientific computing.
Data analysis.
Machine learning and deep learning.

--- Slide 6 ---

How JIT Compilation Works
JIT Compilation Explained
Traditional Python code is interpreted line-by-line, causing slower execution.
Numba compiles functions into machine code just before execution, leading to significant speedups.
Uses LLVM (Low-Level Virtual Machine) for optimizing execution.

--- Slide 7 ---

How Numba Works

--- Slide 8 ---

Performance with & without numba
Without Numba: The function runs in pure Python, which is slower due to interpreter overhead.
With Numba: The function is compiled to machine code, resulting in significantly faster execution.

--- Slide 9 ---

Numba Modes
1. nopython Mode:
Ensures the function is fully compiled to machine code.
No Python objects are allowed.
Example:


2. object Mode:
Allows Python objects but is slower.
Used as a fallback when no python mode fails.

--- Slide 10 ---

Limitations of Numba
Challenges:

Works best with numerical computations.
Limited support for non-NumPy Python features.
Requires careful handling of data types.

When Not to Use:

For non-numerical or highly dynamic Python code.

--- Slide 11 ---

Summary
Numba accelerates Python code using JIT compilation.
Works best with loops and numerical computations.
NumPy operations are highly optimized with Numba.
Simple to use: Just add @jit(nopython=True) decorator.
Helps in high-performance computing, scientific computing, and machine learning workloads.

--- Slide 12 ---

Practical Implementation
Click on the link below to go to Google COLAB
https://colab.research.google.com/drive/10_sbDJlV6zeSHAnHY_EWTf9t488Vn0Hz#scrollTo=210h8e44YxPQ

--- Slide 13 ---

الشراكات العالمية

--- Slide 14 ---

شــــــكــــرًا لكــــــم
THANK YOU

### 14

--- Slide 1 ---

أكـــــاديميــــة طــــويـــق
Scalable Data Science

--- Slide 2 ---

Scaling Scikit-learn with Joblib and Dask
By: Dr. Afshan Hashmi

--- Slide 3 ---

Course Objectives:

Understand the limitations of scikit-learn when working with large datasets or complex pipelines.
Learn how to implement parallel computing in scikit-learn using Joblib for efficient local computation.
Explore the capabilities of Dask for distributed computing and scaling machine learning workflows beyond a single machine.
Apply parallel and distributed techniques to real-world machine learning tasks such as cross-validation and hyperparameter tuning.
Compare and contrast the features, use cases, and performance of Joblib and Dask in different scenarios.
Develop best practices for profiling, optimizing, and monitoring machine learning workflows using Joblib and Dask.

--- Slide 4 ---

Introduction
Scikit-learn is one of the most widely used machine learning libraries in Python, offering simple and efficient tools for data mining and analysis. However, when working with large datasets or computationally intensive models, the need arises to scale scikit-learn’s operations. Two popular tools for parallelizing and scaling scikit-learn workflows are Joblib and Dask.

--- Slide 5 ---

Why Scaling is Needed in Scikit-learn
Limited Scope for Big Data: Scikit-learn is optimized for small to medium datasets; it can struggle with memory and computation when working with large-scale data.
Lack of Built-in Parallelism: Most machine learning algorithms in scikit-learn are not parallelized by default, so they may not fully utilize multi-core processors.
Intensive Tasks: Operations such as grid search for hyperparameter tuning, cross-validation, and complex pipelines require significant computation, which slows down with growing data.
Need for External Tools: To overcome these limitations, external libraries like Joblib (for parallel processing) and Dask (for distributed computing) are used.

--- Slide 6 ---

2. Parallel Processing with Joblib
Joblib is a library used by scikit-learn under the hood for parallel execution, especially during tasks like cross-validation and hyperparameter tuning.
Explanation:
Joblib is a Python library that enables parallel computing by running tasks across multiple CPU cores.
In scikit-learn, many operations (like GridSearchCV, cross_val_score, and some model training) use Joblib internally.
When you see a parameter like n_jobs in scikit-learn, that's where Joblib often comes into play:
n_jobs=1: runs on a single core.
n_jobs=-1: uses all available cores for parallel processing.
This parallelism is especially useful in computationally intensive tasks like:
Cross-validation (splitting data multiple times and training models)
Hyperparameter tuning (testing multiple combinations of parameters)

--- Slide 7 ---

from joblib import Parallel, delayed
import math

results = Parallel(n_jobs=4)(delayed(math.sqrt)(i) for i in range(10))
print(results)
a. Basic Usage :Using Joblib to parallelize square root computation
b. Integration with Scikit-learn: Many scikit-learn functions use Joblib via the n_jobs parameter:
from sklearn.ensemble import RandomForestClassifier

# Create a random forest classifier using 4 cores
model = RandomForestClassifier(n_jobs=4)

--- Slide 8 ---

from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier()
param_grid = {'n_estimators': [100, 200], 'max_depth': [10, 20]}

# GridSearchCV with all cores utilized for parallelism
grid = GridSearchCV(model, param_grid, cv=5, n_jobs=-1)
grid.fit(X, y)
c. Grid Search Example

--- Slide 9 ---

Benefits of Using Joblib with Scikit-learn
Easy to Use:Joblib integrates seamlessly with scikit-learn. In most cases, you simply need to add a parameter like n_jobs=-1 to enable parallel processing.
Efficient on Local Machines:It’s optimized for multi-core CPUs, making it perfect for shared-memory systems (like your laptop or workstation) without requiring any complex setup.
Scikit-learn Native Support:Most scikit-learn estimators, including RandomForestClassifier, GridSearchCV, and cross_val_score, natively support Joblib. That means no extra work is needed to enable parallelism.

--- Slide 10 ---

Distributed Computing with Dask
Dask is a powerful Python library designed to handle large computations across multiple cores, CPUs, or even clusters of machines.
Here’s a breakdown:
Dask vs Joblib: While Joblib runs tasks in parallel on your local machine, Dask can distribute those tasks across multiple machines or clusters—making it more suitable for very large datasets or heavy tasks.
Lazy Evaluation: Dask does not execute operations immediately. It builds a task graph and only runs it when needed—this saves memory and allows for optimization.
Task Scheduling: Dask manages complex chains of operations and efficiently decides what task to run next using a smart scheduler.
Out-of-Core Computation: Dask can handle data that doesn't fit into RAM by processing chunks of data at a time.

--- Slide 11 ---

Integration with Scikit-learn:
You can swap out Joblib’s backend to Dask with a single line of code (with joblib.parallel_backend('dask'):), allowing tools like GridSearchCV and cross_val_score to run in a distributed environment.
Dask-ML extends this even further, offering scalable versions of ML tools like GridSearchCV.

Installing Dask
pip install dask[complete] dask-ml

--- Slide 12 ---

c. Using Dask with Scikit-learn
Dask provides a drop-in replacement for joblib to allow distributed execution:
import joblib
from dask.distributed import Client
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier

client = Client()

with joblib.parallel_backend('dask'):
    scores = cross_val_score(RandomForestClassifier(), X, y, cv=5)
print(scores)
d. Dask-ML Integration
Dask-ML is a scalable machine learning library that complements scikit-learn.
from dask_ml.model_selection import GridSearchCV
from sklearn.ensemble import GradientBoostingClassifier

search = GridSearchCV(GradientBoostingClassifier(), {'n_estimators': [100, 200]}, cv=5)
search.fit(X, y)

--- Slide 13 ---

Benefits of Using Dask with Scikit-learn
Works on Distributed Clusters: Unlike Joblib, which is limited to a single machine, Dask allows you to run your ML tasks across multiple machines or a cloud cluster—this is ideal for big data environments.
Handles Larger-than-Memory Datasets: With Dask's support for out-of-core computations, you can work with datasets that don’t fit into your system’s RAM. This is a game-changer when dealing with massive datasets in production.
Provides Better Control Over Computation: Dask builds and executes task graphs, offering detailed insights into each step of the computation. This makes performance monitoring, optimization, and debugging more effective—especially using the Dask dashboard.
These benefits make Dask a strong companion for scaling and distributing your scikit-learn models.

--- Slide 14 ---

Comparison Table: Joblib vs Dask

--- Slide 15 ---

Performance Optimization TechniquesChoosing the Right Approach
Memory Management
Use Dask arrays/dataframes for out-of-core computation
Persist frequently used data in memory

--- Slide 16 ---

Performance Optimization Techniques
Data Locality
Co-locate computation with data
Minimize data transfer between workers
Batch Size Tuning
Balance between parallelism and overhead
Experiment with chunks parameter in Dask
from dask.diagnostics import Profiler, ResourceProfiler, visualize

with Profiler() as prof, ResourceProfiler() as res:
    # Your computation here
    pass

visualize([prof, res])
Monitoring Performance

--- Slide 17 ---

Best Practices for Scaling Scikit-learn with Joblib and Dask
The Best Practices section provides recommendations to ensure efficient and optimal use of Joblib and Dask for parallelizing and distributing scikit-learn tasks.
Use n_jobs=-1 to Utilize All Cores with Joblib:
When using Joblib for parallelization, setting n_jobs=-1 will use all available cores on your local machine, speeding up tasks like training models or performing cross-validation.
Example: If you're working with GridSearchCV or a large RandomForest, this ensures you're fully utilizing your CPU resources.
Monitor Resource Usage When Using Dask:
Dask can use distributed systems, which may consume a lot of CPU and memory. Monitoring these resources ensures you don’t overload your machine or cluster, potentially causing issues like slow performance or crashes.
Dask's dashboard helps visualize these metrics and track resource usage in real time.

--- Slide 18 ---

Best Practices for Scaling Scikit-learn with Joblib and Dask
Profile Small Datasets Locally Before Moving to Distributed Systems:
Before scaling to a distributed environment with Dask, it’s a good practice to test on smaller datasets. This helps you optimize your code and identify any performance bottlenecks without dealing with the complexities of a distributed system.
Start with local parallelism using Joblib, then scale up to Dask when needed.
Use Dask’s Dashboard for Debugging and Performance Monitoring:
Dask provides a dashboard that is a great tool for monitoring computations, checking for issues in task scheduling, and observing resource usage.
It offers a visual way to identify inefficiencies in your distributed computations, ensuring that you can fine-tune the performance and handle large datasets more efficiently.
Combine Both Tools When Needed:
In some cases, using both Joblib and Dask together may provide the best solution. For instance:
Use Joblib for parallelism in small to medium-sized tasks that fit into memory.
Use Dask for larger-than-memory tasks, especially when scaling to distributed clusters.

--- Slide 19 ---

Common Pitfalls in Distributed Computing
1. Over-parallelization
More workers doesn’t always mean better performance!
Too many workers can lead to communication overhead.
Example: 100 workers fighting over a small task can slow things down.
Best practice: Match the number of workers to your task size and hardware.

2. Small Chunks = High Scheduling Overhead
Breaking data into too many tiny pieces can overload the scheduler.
Each task has scheduling and communication cost.
Thousands of micro-tasks can bottleneck the system.
Best practice: Use moderately sized partitions.

--- Slide 20 ---

Common Pitfalls in Distributed Computing
3. Large Chunks = Memory Issues
Huge data chunks may not fit in memory, causing crashes or slowdowns.
You might see out-of-memory (OOM) errors.
Best practice: Split your dataset into manageable chunks based on your RAM.
4. Ignoring Data Locality
Moving data between workers unnecessarily wastes time.
Operations should happen where the data lives.
If you ignore locality, you'll pay in network transfer time.
Best practice: Let the framework optimize for locality or use persist() intelligently.
5. Not Persisting Data
Recomputing the same results repeatedly = wasted computation.
If you don't cache intermediate results, Spark/Dask will recompute every time.
Best practice: Use .persist() or .cache() after expensive computations.

--- Slide 21 ---

Debugging Tips
client.get_worker_logs()
View logs from each worker to debug what went wrong.
Helps identify errors on specific nodes.
Dask Dashboard
Real-time visual tool to monitor:
Tasks
Memory usage
CPU usage
Helps pinpoint bottlenecks.
Start with a Small Subset
Always test logic on a tiny sample of data first.
Reduces complexity and makes errors easier to track.
Use compute(scheduler='single-threaded')
Forces Dask to run in serial (non-parallel) mode.
Easier to debug step-by-step like regular Python code.
# Example for debugging
result = dask_df.sum().compute(scheduler='single-threaded')

--- Slide 22 ---

Practical Examples and Code SnippetsExample 1: Parallel Grid Search
from sklearn import datasets
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
from dask.distributed import Client
from sklearn.externals.joblib import parallel_backend

client = Client()

iris = datasets.load_iris()
parameters = {'kernel': ('linear', 'rbf'), 'C': [1, 10]}

with parallel_backend('dask'):
    clf = GridSearchCV(SVC(), parameters, n_jobs=-1)
    clf.fit(iris.data, iris.target)

--- Slide 23 ---

Practical Examples and Code SnippetsExample 2: Out-of-Core Random Forest
import dask.array as da
from dask_ml.ensemble import RandomForestClassifier

# Create or load large dataset
X = da.random.random((1e6, 100), chunks=(1000, 100))
y = da.random.randint(0, 2, size=1e6, chunks=1000)

model = RandomForestClassifier(n_estimators=100)
model.fit(X, y)

--- Slide 24 ---

Practical Examples and Code SnippetsExample 3: Custom Parallel Function
from joblib import Parallel, delayed
from dask.distributed import Client

def process_chunk(chunk):
    # Process each chunk
    return chunk.mean()

client = Client()

# Large array
data = da.random.random((1e6,), chunks=1e5)

# Process in parallel
results = Parallel(n_jobs=-1)(delayed(process_chunk)(chunk) 
                             for chunk in data.to_delayed())

--- Slide 25 ---

Summary:

--- Slide 26 ---

Academic References
Official Documentation
joblib documentation
Dask documentation
Dask-ML documentation
Tutorials and Guides
Scaling scikit-learn with Dask
Parallel Processing in Python
Books
"Python for Data Analysis" by Wes McKinney (creator of pandas)
"High Performance Python" by Micha Gorelick and Ian Ozsvald

--- Slide 27 ---

الشراكات العالمية

--- Slide 28 ---

شــــــكــــرًا لكــــــم
THANK YOU


## Pdfs

### 15

--- Slide 1 ---

أكـــــاديميــــة طــــويـــق
Scalable Data Science

--- Slide 2 ---

cuDF: Understsanding performance and visualization
Analyzing Performance by profiling utilities
By: Dr. Afshan Hashmi

--- Slide 3 ---

Course Objectives:
To introduce the fundamentals of cudf.pandas and its role in accelerating data processing using GPUs.
To equip learners with profiling techniques for optimizing performance and identifying GPU vs. CPU execution in data workflows.
To explore data visualization techniques using third-party libraries like Plotly with cudf.pandas.

--- Slide 4 ---

Understanding the Basics
When dealing with large datasets, processing speed is crucial. That's where GPUs (Graphics Processing Units) come in, as they're designed for parallel processing, which significantly accelerates data manipulation. However, not all operations can be performed on a GPU. This is where cudf.pandas and its profiling utilities become very useful. Here's a breakdown:

pandas: pandas is a popular Python library for data manipulation and analysis, primarily designed for CPU processing.

cuDF: cuDF is a GPU-accelerated DataFrame library, designed to perform similar operations as pandas but on a GPU, leading to much faster processing for large datasets.

3.   cudf.pandas: cudf.pandas acts as an accelerator for pandas. It attempts to execute pandas-like operations on the GPU whenever possible, and if an operation isn't supported by the GPU, it falls back to the CPU.

--- Slide 5 ---

Understanding Performance in cudf.pandas
cudf.pandas provides profiling utilities to help you analyze the performance of your code when working with GPU-accelerated data frames. 

These tools help determine which parts of your code ran on the GPU (which is faster for large data processing) and which parts still ran on the CPU (which may be a bottleneck).

--- Slide 6 ---

Why Profiling is Important:
Identifying Bottlenecks:
If parts of your code are still running on the CPU, those sections can become performance bottlenecks, slowing down the overall process.
The profiling utilities help you pinpoint these CPU-bound sections.
Optimizing Performance:
By knowing which parts of your code are using the GPU and which are using the CPU, you can optimize your code to maximize GPU utilization.
This may involve rewriting certain operations to be more GPU-friendly or minimizing data transfers between the CPU and GPU.
Understanding Execution:
The profiler gives you a clear picture of how your code is being executed, which is valuable for understanding and improving its performance.

--- Slide 7 ---

The Goal: Accelerating pandas with GPU Power
Core Functionality:
At its heart, cudf.pandas aims to leverage the parallel processing capabilities of GPUs to drastically speed up data manipulation tasks that are traditionally handled by the pandas library on CPUs.

It acts as a bridge, attempting to translate your familiar pandas code into equivalent operations that can be executed on the GPU.

Performance Gains:
For large datasets, GPU acceleration can result in significant performance improvements, often orders of magnitude faster than CPU-based processing.

The largest gains are seen in operations that can be performed in parallel.

--- Slide 8 ---

The Insight: Profiling for Performance Analysis
Understanding Execution Flow:
The profiling tools within cudf.pandas provide crucial insights into how your code is actually being executed.
They reveal which portions of your data processing pipeline are being handled by the GPU and which are falling back to the CPU.

Identifying Bottlenecks:
By highlighting CPU-bound operations, the profiler helps you pinpoint potential performance bottlenecks.
These bottlenecks can arise from operations that are not yet supported on the GPU or from inefficient data transfers between the CPU and GPU.
Measuring Success:
The tools allow you to measure how effectively the GPU is being utilized. 
This gives you concrete data to understand the performance gains you are receiving.

--- Slide 9 ---

The Action: Optimization and Efficiency
Targeted Optimization:
Armed with the information from the profiler, you can strategically optimize your code to maximize GPU utilization.
This may involve restructuring data manipulations, using GPU-compatible functions, or minimizing data transfers.
Workflow Enhancement:
By optimizing your code for GPU acceleration, you can significantly improve the efficiency of your data processing workflows.
This translates to faster processing times, reduced resource consumption, and improved overall productivity.
Maximizing Potential:
For anyone working with large datasets and seeking to maximize the performance of their cudf.pandas workflows, the profiling utilities are indispensable. They provide the necessary visibility and insights to unlock the full potential of GPU acceleration.

--- Slide 10 ---

Profiling with cudf.pandas
Profiling utilities allow you to analyze execution time and resource usage helping  in optimizing code by identifying CPU-bound operations.
Loading the Extension
To use profiling features, the cudf.pandas extension must be loaded.




Colab Note
If running in Google Colab, the first time you use the profiler, it may take more than 10 seconds due to Colab's debugger interacting with Python’s sys.settrace function.
If it runs slow initially, run the cell again, and it should work fine.

--- Slide 11 ---

Profiling per function
Pandas.profile gives the detail about each function

--- Slide 12 ---

Profiling per line
Pandas.line.profile gives the detail about each line of code

--- Slide 13 ---

Using Third-Party Libraries with cudf.pandas
The cudf.pandas module in RAPIDS supports interoperability with third-party Python libraries like Plotly, Matplotlib, Seaborn, and Scikit-learn. 

This means you can pass cuDF DataFrames (which are optimized for GPU processing) to these libraries just like you would with standard Pandas DataFrames.

--- Slide 14 ---

Visualization with Plotly.express

--- Slide 15 ---

Visualizing which states have more pickup trucks as compared to other vehicles?

--- Slide 16 ---

Top 10 Most Common Violations

--- Slide 17 ---

Visualisation of Top 10 Most Common Violations

--- Slide 18 ---

Visualisation of Traffic violation by state

--- Slide 19 ---

Recap
Understanding cudf.pandas – It enables Pandas-like operations while leveraging GPU acceleration for faster data processing.
Third-Party Library Compatibility – cudf.pandas allows seamless integration with libraries like Plotly but requires converting cuDF DataFrames to Pandas before visualization.
Profiling with cudf.pandas.profile – Profiling tools help identify whether operations run on the CPU or GPU, allowing for optimization.
Optimizing Performance – When using GPU-accelerated pandas libraries, functions like apply() can sometimes result in CPU execution if the applied function is not GPU-compatible. In such cases, if possible, replacing apply() with equivalent vectorized GPU operations can lead to significant performance improvements.
GPU vs. CPU Execution – Operations like groupby(), mean(), and arithmetic calculations are GPU-optimized, while functions like apply() may require manual optimization.
Reducing to_pandas() Calls – Avoid unnecessary conversions from cuDF to Pandas to prevent performance bottlenecks in large datasets.
Best Practices for cuDF Optimization – Use built-in cuDF functions, avoid explicit loops, and prefer vectorized operations for efficient data processing.
Debugging Performance Issues – Profiling reports help pinpoint slow operations, guiding developers to replace inefficient CPU-based functions with GPU-accelerated alternatives.

--- Slide 20 ---

Practical Implementation
Click on the link below to go to Google COLAB
https://colab.research.google.com/drive/1T_IhHxkapwa6vTlOompAo5oHzCYFXDmM - scrollTo=pyVNtGUhtFs5

--- Slide 21 ---

شــــــكــــرًا لكــــــم
THANK YOU

### 16

--- Page 1 ---

Big Data Concepts
& Challenges

--- Page 2 ---

What is Big Data?
Data sets so large or complex that traditional data processing applications are insufficient.
Key Insight: "Big" is relative to:
Processing capabilities
Storage technologies
Analysis techniques
Time constraintsBig Data Concepts & Challenges
Introduction to Big Data
Historical Perspective:
1970s: Megabytes were "big"
1990s: Gigabytes were "big"
2010s: Terabytes became common
2020s: Petabytes and beyond

--- Page 3 ---

Big Data Concepts & Challenges
The 5 Vs of Big Data
Volume: Enormous amounts of data
Example: YouTube users upload 500+ hours of video every minute
Velocity: Speed at which data is generated and processed
Example: Stock market generates terabytes of data per trading day
Variety: Different types and formats of data
Structured, semi-structured, unstructured
Veracity: Trustworthiness and quality of data
Noise, abnormalities, biases
Value: Usefulness and insights derived from data
Transforming data into actionable intelligence

--- Page 4 ---

Big Data Concepts & Challenges
Volume: Scale Matters
Typical Big Data Volumes:
Facebook: 4+ petabytes of new data per day
Large Hadron Collider: 1 petabyte per second (filtered down)
Internet Archive: 45+ petabytes
Human Genome: ~200 gigabytes per sequenced genome
Storage Units:
1 Terabyte (TB) = 1,000 Gigabytes
1 Petabyte (PB) = 1,000 Terabytes
1 Exabyte (EB) = 1,000 Petabytes
1 Zettabyte (ZB) = 1,000 Exabytes
Global Data Sphere: Expected to reach 175 zettabytes by 2025

--- Page 5 ---

Big Data Concepts & Challenges
Velocity: Speed of Data
Real-time Data Generation:
IoT sensors: Millisecond updates
Social media: 500 million tweets per day
Financial markets: Microsecond trading data
Telecommunications: Call data records
Processing Requirements:
Batch processing: Process data in scheduled intervals
Stream processing: Continuous analysis of data in motion
Near real-time: Seconds to minutes latency
Real-time: Sub-second latency

--- Page 6 ---

Big Data Concepts & Challenges
Variety: Diverse Data Types
Structured Data (20% of all data):
Relational databases
CSV files
Financial transactions
Sensor readings with fixed format
Semi-structured Data:
JSON, XML
Email
Web logs
Unstructured Data (80% of all data):
Text documents
Audio, video, images
Social media content
Scientific data (genomics, weather)

--- Page 7 ---

Big Data Concepts & Challenges
Variety: Diverse Data Types
Semi-structured Data:
JSON Example

--- Page 8 ---

Big Data Concepts & Challenges
Veracity: Data Quality Challenges
Data Quality Issues:
Missing values
Duplicate records
Inconsistent formats
Measurement errors
Sampling biases
Implications:
"Garbage in, garbage out"
60% of data scientists' time spent cleaning data
Data quality directly impacts model reliability
Approaches:
Data validation at ingestion
Statistical anomaly detection
Data provenance tracking
Automated data quality monitoring

--- Page 9 ---

Big Data Concepts & Challenges
The Breaking Points of Traditional Systems
Storage Limitations:
Single machine storage capacity
Backup and recovery time
Storage access bottlenecks
Compute Limitations:
Single machine CPU/memory capacity
Algorithm complexity scaling
I/O bottlenecks
Design Limitations:
Schema rigidity
Network limitations
Management complexity

--- Page 10 ---

The Shift: From scaling up to scaling out

--- Page 11 ---

Big Data Concepts & Challenges
Distributed Storage Fundamentals
Core Concepts:
Data partitioning/sharding
Replication
Consistency models
Failure detection and recovery
Design Goals:
Scalability
Availability
Durability
Performance
Consistency
Trade-offs:
The CAP theorem
Consistency vs. latency
Storage vs. compute separation
Performance vs. cost

--- Page 12 ---

Big Data Concepts & Challenges
The CAP Theorem
Consistency:
All nodes see the same data at the same time
Reads return most recent write
Availability:
Every request receives a response
No guarantee that response contains most recent write
Partition Tolerance:
System continues to operate during network partitions
The Theorem:
You can only guarantee 2 out of 3 properties
In distributed systems, partition tolerance is required
Therefore, choose between consistency and availabilityCAP = Consistency, Availability, Partition Tolerance

--- Page 13 ---

Big Data Concepts & Challenges
Distributed Processing Concepts
Characteristics:
Process large volumes of data
High throughput, high latency
Typically scheduled at intervals
Key Concepts:
Data partitioning
Parallel processing
Fault tolerance
Checkpointing
Programming Models:
MapReduce
Bulk Synchronous Parallel (BSP)
Directed Acyclic Graphs (DAGs)Common Use Cases:
ETL processes
Data warehousing
Complex analytics
Model training

--- Page 14 ---

Big Data Concepts & Challenges
Stream processing vs. Batch Processing

--- Page 15 ---

Phases:
Map: Transform and filter data (record → key-value pairs) 1.
Shuffle: Group by key 2.
Reduce: Aggregate results for each key 3.
Advantages:
Simple programming model
Automatic parallelization
Built-in fault tolerance
Horizontal scalability
Big Data Concepts & Challenges
The MapReduce Paradigm

--- Page 16 ---

Example: Customer Purchase Analysis
Imagine we have a large dataset of customer transactions that
we want to analyze to find the total spending by country.Big Data Concepts & Challenges
The MapReduce Paradigm
Input
Map Phase
key-value pairsShuffle Phase
sorts and groups all values by
key (country)
Reduce Phase
calculates the total Final Output

### 17

--- Page 1 ---

AI Diploma

--- Page 2 ---

Semester One | Course ThreeScalable Data Science 
with Python

--- Page 3 ---

ROADMAP
SCALABLE DATA SCIENCE WITH PYTHON
Week 1: Foundations of
Scalable Computing
Objective: Master the fundamentals
of Python data tools and
understand core principles of
scalable data processing.
Week 2: Distributed
Computing Frameworks
Objective: Learn to implement
and utilize distributed computing
frameworks to process data
beyond single-machine
capabilities.Week 3: Large-Scale Data
Processing & GPU
Acceleration
Objective: Develop skills in GPU-
accelerated data processing using
RAPIDS, CuPy, and cuDF alongside
traditional distributed computing tools.
Week 4: Machine
Learning at Scale
Objective: Apply scalable
approaches to train and deploy
machine learning models on large
datasets using GPU acceleration.Week 5: Cloud Infrastructure &
Production Deployment
Objective: Configure and utilize cloud services
for scalable data processing and implement
end-to-end data science pipelines in production
environments.
Capstone Projects &
Advanced Optimizations
Objective:  Learn more advanced
optimizations methods for handling
big data and course summary with
capstone project March 9-13, 2025
March 16-20, 2025April 27-May 1, 2025April 6-10, 2025
April 13-17, 2025April 20-24, 2025
Eid Vacation Mid-term exam
Semester Final Exam

--- Page 4 ---

Semester One | Course ThreeScalable Data Science with Python
Unit 1 : Foundations of
Scalable Computing

--- Page 5 ---

Introduction to
Data Science

--- Page 6 ---

Introduction to Data Science
What is Data Science?

--- Page 7 ---

Introduction to Data Science
What is Data Science?
Data Science is a combination of multiple disciplines that uses statistics, data analysis, and
machine learning to analyze data and to extract knowledge and insights from it.
Key Components:
Statistics and Mathematics
Domain Expertise
Programming and Database Knowledge
Communication and Visualization Skills

--- Page 8 ---

Introduction to Data Science
The Data Science Lifecycle
Data Science Lifecycle is a step-by-step demonstration of how machine learning and other analytical methods are used to generate insights
and predictions from data to achieve a business goal.
Business Understanding: Define objectives and requirements
Data Acquisition: Collect raw data from various sources
Data Preparation: Clean, transform, and prepare data for analysis
Exploratory Data Analysis: Understand patterns, and relationships
Modeling: Develop predictive or descriptive models
Evaluation: Assess model performance and validate results
Deployment: Implement solutions in production environments
Monitoring: Track performance and maintain systems

--- Page 9 ---

Introduction to Data Science
Data - Terms & Concepts
Data Acquisition
The process of collecting and gathering raw data from various sources. 
This includes data capture from sensors, web scraping, database queries, API calls, or surveys...
Data acquisition focuses on obtaining the raw materials needed for analysis.
Data Analysis
The process of inspecting, cleaning, transforming, and modeling data to discover useful information,
draw conclusions, and support decision-making. 
Data analysis typically follows a structured approach to examine what happened (descriptive), why it
happened (diagnostic), what might happen (predictive), and what actions to take (prescriptive).
Data Mining
A specific subset of data analysis that focuses on discovering patterns, anomalies, correlations, and
dependencies in large datasets using automated or semi-automated techniques. 
Data mining applies algorithms specifically designed to extract hidden patterns that might not be
apparent through standard analysis techniques.

--- Page 10 ---

Introduction to Data Science
Data - Terms & Concepts
Data Processing
The conversion of raw data into a more useful format. 
This includes cleaning, normalization, transformation, and aggregation to prepare data for analysis.
Data Wrangling (or Data Munging)
The process of cleaning, structuring, and enriching raw data into a desired format for better decision
making. 
This addresses inconsistencies, missing values, and formatting issues.
Data Exploration
The initial investigation of data to discover patterns, spot anomalies, test hypotheses, and check
assumptions using summary statistics and visualizations.

--- Page 11 ---

Introduction to Data Science
Data Science vs. Business Intelligence
 Business Intelligence 
The strategies and technologies used for data analysis of business information, focusing on historical
data to provide insights into past performance and guide business planning.

--- Page 12 ---

Introduction to Data Science
What are Data Scientists?
 Not computer scientists
But should know about databases, data structures, algorithms, etc.
Not mathematicians
But should know about optimization, stochastic, etc.
Not statisticians
But should know about regression, statistical tests, etc.
Not domain experts
But must work together with them

--- Page 13 ---

Introduction to Data Science
The Scale Challenge
Billions of sensors have been collecting data for decades
DNA sequencing lab, where massive amounts of genetic
data are generated from sequencing machines.

--- Page 14 ---

Introduction to Data Science
The Scale Challenge
Billions of sensors have been collecting data for decades
large-scale radio telescope array used for astronomical
observations, collecting vast amounts of raw radio
frequency data from space

--- Page 15 ---

Introduction to Data Science
The Scale Challenge
Billions of sensors have been collecting data for decades
Social network graph, Mapping connections and
interactions on platforms like Twitter, Handling billions
of interactions.

--- Page 16 ---

Introduction to Data Science
The Scale Challenge
Billions of sensors have been collecting data for decades
Satellite and drone for monitor crop health and predict yields.

--- Page 17 ---

Introduction to Data Science
The Scale Challenge
- With so much driven by data, it’s important that data
scientists work responsibly and for the greater good

--- Page 18 ---

Introduction to Data Science
The Scale Challenge
Modern data science faces increasing challenges with data volume:
Global data creation projected to exceed 180 zettabytes by coming years.
Single organizations routinely collect terabytes of data daily.
Traditional tools break down with large-scale datasets.
Complex computations become resource-intensive.
This course focuses on tools and techniques to overcome these scaling
challenges.

--- Page 19 ---

Introduction to Data Science
Scaling Dimensions in Data Science
Vertical Scaling (Scale Up): Increasing resources on a single machine
More RAM, faster CPUs, specialized hardware (GPUs)
Horizontal Scaling (Scale Out): Distributing across multiple machines
Cluster computing, distributed processing frameworks
Algorithm Efficiency: Optimizing computational approaches
Better algorithms, approximation methods, dimensionality reduction
Data Architecture: Smart data organization and storage
Databases, data lakes, caching strategies

--- Page 20 ---

Introduction to Data Science
Important Terms in Scaling 
CPU (Central Processing Unit):
The "brain" of your computer
Handles most of the general calculations and tasks
Really good at doing a few complex tasks one after another
Like a small team of very smart workers who can handle any task but work on one thing at a time
Example: Running your operating system, opening applications, browsing the internet
GPU (Graphics Processing Unit):
Originally designed for creating images and videos
Excellent at doing many simple calculations all at once
Like a large team of specialized workers who can do the same task simultaneously on different data
Perfect for data science because analyzing data often involves repeating the same calculation on many data points
Example: Rendering video games, training AI models, processing large datasets

--- Page 21 ---

Introduction to Data Science
Important Terms in Scaling 
RAM (Random Access Memory)
The "workspace" or "short-term memory" of your computer
Temporarily stores data that the CPU and GPU are actively using
Allows for quick access to information without retrieving it from storage
Like a desk where you keep documents you're currently working on
Example: Holding the application data while you're using it, storing the data you're analyzing until the
computer is turned off or the task is complete
In data science:
CPU handles the overall program flow and complex operations
GPU accelerates calculations when working with large datasets
RAM determines how much data you can work with at once before needing to access storage
When you run out of RAM, everything slows down dramatically because the computer must use much slower
storage (like your hard drive) as a substitute.

--- Page 22 ---

Introduction to Data Science
Vertical Scaling (Scale Up): 
Increasing resources on a single machine
Hardware Upgrades:
RAM Expansion
Upgrading from 16GB to 64GB or 128GB RAM
Allows processing larger datasets entirely in memory
CPU Improvements
Adding more CPU cores (e.g., upgrading from a 4-core to a
32-core processor) Using higher clock speed processorsGPU Acceleration
Adding specialized NVIDIA Tesla or AMD Instinct GPUs
Upgrading from consumer GPUs to data center GPUs
with more VRAM
Storage Enhancements
Switching from HDD to SSD or NVMe storage
Using RAID configurations for parallel read/write operations

--- Page 23 ---

Introduction to Data Science
Vertical Scaling (Scale Up): 
Increasing resources on a single machine
Software Optimizations for Vertical Scaling
Multi-threading
Optimizing code to use all available CPU cores
Memory-Efficient Algorithms
Using algorithms designed for minimal memory footprintGPU-Accelerated Libraries
Using CuPy instead of NumPy for array operations
Using cuDF instead of pandas for DataFrame operations

--- Page 24 ---

Introduction to Data Science
Vertical Scaling (Scale Up): 
Increasing resources on a single machine
Limitations of Vertical Scaling:
Physical constraints (maximum RAM supported by motherboard)
Hardware limits (maximum available configurations)
Vertical scaling is often the simplest approach but eventually hits physical and economic limits,
which is when horizontal scaling becomes necessary.

--- Page 25 ---

Introduction to Data Science
Horizontal Scaling (Scale Out): 
Distributing across multiple machines
Computing Clusters
Hadoop Clusters
Setting up a network of commodity servers running
HDFS and MapReduce
Example: Processing petabytes of log files using 100+
connected machines
Each node handles a portion of the data, enabling parallel
processingSpark Clusters
Deploying Apache Spark across multiple machines
Example: Running distributed machine learning with MLlib
across a 20-node cluster
Allows in-memory distributed processing with fault
tolerance
Dask Clusters
Scaling Python workflows across multiple machines
Example: Distributing pandas operations over a cluster to
process DataFrames larger than a single machine's memory
Maintains familiar Python APIs while distributing computation

--- Page 26 ---

Introduction to Data Science
Horizontal Scaling (Scale Out): 
Distributing across multiple machines
Cloud-Based Solutions
AWS EMR (Elastic MapReduce)
Dynamically scaling clusters based on workload
Example: Spinning up 500 nodes for an intensive
overnight ETL job, then scaling down to save costs
Pay only for resources used during peak processingGoogle Dataproc/BigQuery
Serverless distributed computing
Example: Analyzing billions of rows without managing
infrastructure
Scales automatically based on query complexity

--- Page 27 ---

Introduction to Data Science
Horizontal Scaling (Scale Out): 
Distributing across multiple machines
Database Scaling
Sharding
Splitting databases across multiple servers by partitioning
keys
Example: Distributing customer data geographically, with
North American customers on one server cluster,
European on another
Each machine handles queries for its specific data
partitionReplication
Creating copies of data across multiple nodes
Example: Maintaining read-replicas to handle high-volume
analytical queries without impacting transaction
processing
Improves read performance while providing redundancy

--- Page 28 ---

Introduction to Data Science
Horizontal Scaling (Scale Out): 
Distributing across multiple machines
Practical Implementations
Data-Parallel Processing
Breaking a dataset into chunks processed on separate
machines
Example: Using PySpark to distribute CSV parsing across
50 nodes, each handling 2% of the total records
Results are combined after parallel processingModel-Parallel Training
Distributing large machine learning models across multiple
GPUs/machines
Example: Training massive language models where model
parameters don't fit in a single GPU's memory
Different layers or components of the model run on
different hardware

--- Page 29 ---

Introduction to Data Science
What About Training LLMs ?!

--- Page 30 ---

Introduction to Data Science
Why Python for Data Science?
Python has become the de facto language for data science due to:
Readability and simplicity: Easy to learn and use
Extensive ecosystem: Rich libraries for data analysis and ML
Community support: Large, active community and resources
Versatility: Used across the entire data pipeline
Industry adoption: Widely used in production environments
Integration capabilities: Works well with other languages/systems

--- Page 31 ---

Introduction to Data Science
Python Ecosystem for Data Science
NumPy: Numerical computing with multi-dimensional arrays
Pandas: Data manipulation and analysis
Matplotlib/Seaborn: Data visualization
Scikit-learn: Machine learning algorithms
SciPy: Scientific computing and technical computing
Statsmodels: Statistical models and tests

--- Page 32 ---

Introduction to Data Science
Scaling Python: Core Technologies
NumPy: Efficient numerical operations with vectorization.
Pandas: Data manipulation and aggregation with optimized C
backends
Dask: Parallel computing library that scales Python
PySpark: Python API for Apache Spark distributed computing
Ray: Distributed computing framework for scaling Python
RAPIDS: GPU-accelerated data science (CuPy, cuDF)
Numba: JIT compiler for numeric Python functions

--- Page 33 ---

Introduction to Data Science
Libraries -Numpy
A popular math library in Python for Machine Learning is ‘numpy’.
import  numpy as np
Numpy.org : NumPyis the fundamental package for scientific computing with Python.
•
•
•
•a powerful N-dimensional array object
sophisticated (broadcasting) functions
tools for integrating C/C++ and Fortran code
useful linear algebra, Fourier transform, and random number capabilitiesKeyword to import a library Keyword to refer to library by an alias (shortcut) name

--- Page 34 ---

Introduction to Data Science
Libraries -Numpy
Numpy’s main object is a multi-dimensional array. 
Creating a NumpyArray as a Vector:
Creating a NumpyArray as a Matrix :data = np.array( [ 1, 2, 3 ] )
data = np.array( [ [ 1, 2, 3 ], [ 4, 5, 6 ], [ 7, 8, 9 ] ] )Value is: array( [ 1, 2, 3 ] )
Value is: array( [ 1, 2, 3 ],           
[ 4, 5, 6 ], [ 7, 8, 9 ] )Outer Dimension Inner Dimension (rows)Numpyfunction to create a numpyarray

--- Page 35 ---

Introduction to Data Science
Libraries -Numpy
data = np.ones( (2, 3), dtype=np.int )data = np.zeros( ( 2, 3 ), dtype=np.int )Numpyfunction to create an array of zeros
Value is: array( [ 0, 0, 0 ],
[ 0, 0, 0 ] )
Value is: array( [ 1, 1, 1 ],
[ 1, 1, 1 ] )rowscolumns
Numpyfunction to create an array of onesdata type (default is float)
Creating an array of Ones :
And many more functions: size, ndim, reshape, arange, …Creating an array of Zeros :

--- Page 36 ---

Introduction to Data Science
Libraries -Numpy
A popular library for importing and managing datasets in Python for Machine Learning is ‘pandas’.
Used for: 
•Data Analysis 
•Data Manipulation
•Data Visualizationimport pandas as pd
PyData.org : high-performance, easy-to-use data structures and data analysis tools for the
Python programming language.Keyword to import a library Keyword to refer to library by an alias (shortcut) name

--- Page 37 ---

Introduction to Data Science
Pandas –Indexed Arrays
Pandas are used to build indexed arrays (1D) and matrices(2D),
where columns and rows are labeled (named) and can be accessed via the labels (names). 
1
4
82
5
93
6
104
7
11o n e
two
threex 1
1
4
8x 2
2
5
9x 3
3
6
10x 4
4
7
11raw dataRow (samples)
index
Panda Indexed MatrixColumns (features)
index

--- Page 38 ---

Introduction to Data Science
Pandas –Series and Data Frames
Pandas Indexed Arrays are referred to as Series(1D) and Data Frames(2D).
Series is a 1D labeled (indexed) array and can hold any data type, and mix of data types.
s = pd.Series( data, index=[ ‘x1’, ‘x2’, ‘x3’, ‘x4’ ] )
df= pd.DataFrame( data, index=[‘one’, ‘two’], columns=[ ‘x1’, ‘x2’, ‘x3’, ‘x4’ ] )Data FrameSeries Raw data
Row Index LabelsColumn Index Labels
Column Index LabelsData Frame is a 2D labeled (indexed) matrix and can hold any data type, and mix of data
types.

--- Page 39 ---

Introduction to Data Science
Pandas –Selecting
Selecting One Column
x1 = df[ ‘x1’ ]
x1 = df[ [ ‘x1’, ‘x3’ ] ]1
4
8
1
4
83
6
10x1 = df.ix[ :, ‘x1’:’x3’ ]1
4
82
5
93
6
10Selects column labeled x1 for all rows 
columns•Selecting Multiple Columns
Selects columns labeled x1 and x3 for all rows  
And many more functions: merge, concat, stack, …Slicing functionrows (all)Selects columns labeled x1 through x3 for all rows  Note: df[‘x1’:’x3’ ] this python syntax does not work!

--- Page 40 ---

Introduction to Data Science
Libraries -Matplotlib
A popular library for plotting and visualizing data in Python
import  matplotlib.pyplot as plt
matplotlib.org: Matplotlibis a Python 2D plotting library which produces publication quality
figures in a variety of hardcopy formats and interactive environments across platforms. Keyword to import a library Keyword to refer to library by an alias (shortcut) name  
Used for:
Histograms
Plots
Bar Charts
Scatter Plots
...etc

--- Page 41 ---

Introduction to Data Science
Matplotlib - Plot
The function plot , plots a 2D graph.
Example:plt.plot( x, y )
8
6
4
2
1 2X Function to plot
3Y X values to plot
Y values to plot
plt.plot( [ 1, 2, 3 ], [ 4, 6, 8 ] )   # Draws plot in the background
plt.show() # Displays the plot

--- Page 42 ---

Introduction to Data Science
Matplotlib - Plot
Add Labels for X and Y Axis and Plot Title (caption)
plt.plot( [ 1, 2, 3 ], [ 4, 6, 8 ] )
plt.xlabel( “X Numbers”  )
plt.ylabel( “Y Numbers”  )
plt.title( “My Plot of X and Y”)
plt.show()# Label on the X-axis
# Label on the Y-axis
# Title for the Plot8
1 2 3
X Numbers6
4
2My Plot of X and YY Numbers

--- Page 43 ---

Introduction to Data Science
Matplotlib–Multiple Plots and Legend
You can add multiple plots in a Graph 
plt.plot( [ 1, 2, 3 ], [ 4, 6, 8 ], label=‘ 1st Line’ )
plt.plot( [ 1, 2, 3 ], [ 2, 4, 6 ], label=‘2nd Line’ )
plt.xlabel( “X Numbers” )
plt.ylabel( “Y Numbers” )
plt.title( “My Plot of X and Y”)
plt.legend()
plt.show()# Plot for 1
# Plot for 2Line
Line8
6
4
2
1 2 3
X NumbersMy Plot of X and Y
---- 1st Line
---- 2nd Linest
nd
# Show Legend for the plotsY Numbers

--- Page 44 ---

Introduction to Data Science
Matplotlib–Bar Chart
The function bar, plots a bar graph.
plt.plot( [ 1, 2, 3 ], [ 4, 6, 8 ] ) # Plot for 1stLine8
6
4
2
1 2 3plt.bar()
plt.show()# Draw a bar chart
And many more functions: hist, scatter, …

--- Page 45 ---

Introduction to Data Science
Resources

### 18

--- Page 1 ---

Distributed
Computing Principles

--- Page 2 ---

What is Distributed Computing?
Computing paradigm where components on networked computers communicate and coordinate to
achieve a common goal.
In everyday terms:
Solving big problems by dividing them among multiple computers that work together
DISCUSSION 
Think about it: What systems do you use daily that rely on distributed computing? (Social media, email,
streaming services, online banking...)Distributed Computing Principles
Introduction to Distributed Computing

--- Page 3 ---

Distributed Computing Principles
Introduction to Distributed Computing

--- Page 4 ---

What is Distributed Computing?
Computing paradigm where components on networked computers communicate and coordinate to
achieve a common goal.
In everyday terms:
Solving big problems by dividing them among multiple computers that work together
DISCUSSION 
Think about it: What systems do you use daily that rely on distributed computing? (Social media, email,
streaming services, online banking...)Distributed Computing Principles
Introduction to Distributed Computing

--- Page 5 ---

Distributed Computing Principles
The Evolution of Distributed Computing

--- Page 6 ---

Distributed Computing Principles
Why Distributed Computing Exists

--- Page 7 ---

Core Building Blocks
Nodes & Clusters:
Node: Individual computer/server in the network
Cluster: Collection of nodes working together
Example: Spark cluster with 1 master node, 20 worker nodesDistributed Computing Principles
Fundamental Concepts in Distributed Systems
Partitioning & Sharding:
Dividing data across multiple nodes
Strategies: range-based, hash-based, directory-based
Replication
Creating redundant copies of data
Types: full replication, partial replication, master-slave,
peer-to-peer

--- Page 8 ---

1. Master-Worker (Master-Slave)
Central coordinator assigns tasks to workers
Pros: Simple management, centralized control
Cons: Single point of failure at master
Examples: Hadoop MapReduce, traditional RDBMS replication
2. Peer-to-Peer:
All nodes have equal roles and responsibilities
Pros: No single point of failure, high resilience
Cons: Complex coordination, eventual consistency challenges
Examples: BitTorrent, blockchain networks, Cassandra
3. Hybrid Approaches:
Mixing centralized and decentralized elements
Examples: Kafka (distributed but with ZooKeeper coordination)
Distributed Computing Principles
Three Main Architecture Patterns:

--- Page 9 ---

Data Preprocessing
at Scale

--- Page 10 ---

Distributed Computing Principles
The Data Preprocessing Challenge
The 80/20 Rule of Data Science
80% of time spent on data preparation
20% of time spent on actual analysis and modeling
What Makes Preprocessing at Scale Different?
Can't load all data into memory
Can't manually inspect all records
Performance bottlenecks are amplified
New failure modes emerge
Each operation has cost implications

--- Page 11 ---

Distributed Computing Principles
The Data Science Pipeline at Scale
Traditional (Small Data) Pipeline:
Big Data Reality:
Why can't we simply apply the same preprocessing techniques used for small data to big data scenarios?

--- Page 12 ---

Distributed Computing Principles
Preprocessing Challenges That Scale With Data Volume

--- Page 13 ---

Distributed Computing Principles
Data Validation at Scale: Ensuring Quality Input
Data Validation Strategies:
Schema Validation
Ensuring data adheres to expected structure
Handling schema drift and evolution
Tools: Great Expectations, Deequ, tf.data validation
Statistical Profiling
Automatically analyzing distributions and patterns
Identifying potential issues before processing
Example: Column statistics, correlation analysis
Anomaly Detection
Finding unusual patterns or outliers
Prevents corrupted data from affecting downstream analysis
Methods: Statistical tests, clustering, isolation forests

### 19

--- Page 1 ---

Introduction To GPU Acceleration Basics
Understanding CPU vs. GPU Architecture
The Central Processing Unit (CPU)
Key Characteristics:
Few powerful cores (typically 4-64)
Optimized for sequential processing
Large cache memory
Complex control units for branch prediction
Designed for low-latency operations
General-purpose processing

--- Page 2 ---

Introduction To GPU Acceleration Basics
Understanding CPU vs. GPU Architecture
The Graphics Processing Unit (GPU)
Key Characteristics:
Many simple cores (thousands)
Optimized for parallel processing
Smaller cache per core
Simpler control units
Designed for high-throughput operations
Specialized for mathematical operations

--- Page 3 ---

Introduction To GPU Acceleration Basics
CPU vs. GPU: Core Architecture Comparison

--- Page 4 ---

Introduction To GPU Acceleration Basics
When to Use CPU vs. GPU
CPU Excels At:
Tasks requiring complex decision-making
Sequential processes with many branches
Operations on small datasets that fit in cache
Tasks with unpredictable memory access patterns
Single-threaded applicationsGPU Excels At:
Highly parallel computations
Mathematically intensive operations
Working with large datasets
Regular, predictable memory access patterns
SIMD (Single Instruction, Multiple Data) operations

--- Page 5 ---

Introduction To GPU Acceleration Basics
The Evolution of GPU Computing
1990s - Early GPUs:
Dedicated hardware for rendering graphics
Fixed function pipeline
Limited to graphics applications
Early 2000s - Programmable Shaders:
Introduction of programmable elements
Still primarily for graphics
2006-2007 - GPGPU Emerges:
General-Purpose computing on GPUs
NVIDIA introduces CUDA
AMD introduces Stream (later OpenCL)2010s - AI Renaissance:
GPUs become essential for deep learning
NVIDIA's cuDNN library
Specialized hardware (Tensor Cores)
2020s - Specialized Computing:
AI-optimized GPU architectures
Multi-GPU systems
GPU acceleration in cloud computing

--- Page 6 ---

Introduction To GPU Acceleration Basics
GPU Computing Performance Growth
CPU performance growth slowed to ~1.1x per year
GPU performance continues to grow at ~1.5x per year
By 2025, GPUs projected to be 1000x faster than when first introduced for computing

--- Page 7 ---

Introduction To GPU Acceleration Basics
Modern GPU Architecture
Key Components:
Streaming Multiprocessors (SMs): The basic processing blocks
CUDA Cores: Individual processing units within SMs
Tensor Cores: Specialized for matrix multiplication (AI workloads)
Memory Hierarchy:
Global Memory (VRAM):
Main large storage accessible by all components
Highest capacity but slowest access
Shared Memory:
Fast memory shared between threads in the same block
Enables thread communication and serves as programmable cache
L1/L2 Cache:
Automatic buffer storage that reduces memory access times
L1 is private to each SM; L2 is shared across the GPU
Registers:
Ultra-fast storage for individual thread variables
Fastest but very limited capacity; private to each thread

--- Page 8 ---

Introduction To GPU Acceleration Basics
CUDA Programming Model
CUDA (Compute Unified Device Architecture):
Parallel computing platform and API by NVIDIA
Allows developers to use GPUs for general-purpose processing
C/C++ language extensions
Provides both low-level and high-level APIs
Key Concepts:
Host (CPU) and Device (GPU)
Kernel functions
Thread hierarchy
Memory hierarchy
CUDA Thread Hierarchy:
Thread: Individual execution unit 
Block: Group of threads that can communicate via shared memory 
Grid: Collection of blocks that execute the same kernel

--- Page 9 ---

Introduction To GPU Acceleration Basics
Why Use GPU Acceleration in Data Science?
Speed: 10-100x faster for suitable algorithms
Scalability: Process larger datasets
Energy Efficiency: More computations per watt
Cost Effectiveness: Cheaper than CPU clusters for many workloads
Real-time Analytics: Enable interactive analysis of large datasets

--- Page 10 ---

Introduction To GPU Acceleration Basics
Common Algorithms Accelerated by GPUs
Machine Learning:
Linear/Logistic Regression
Gradient Boosting Machines (XGBoost, LightGBM)
Neural Networks and Deep Learning
Support Vector Machines
K-Means Clustering

--- Page 11 ---

Introduction To GPU Acceleration Basics
Python GPU Ecosystem Overview
Low-level: CUDA Python, PyCUDA
Array computation: CuPy, PyTorch, TensorFlow
Data processing: RAPIDS (cuDF, cuML)
Specialized: H2O4GPU, Numba, JAX
Distributed: Dask-CUDA, RAPIDS + Dask

--- Page 12 ---

Introduction To GPU Acceleration Basics
Practical Considerations for GPU Computing
Entry-level (Development & Testing):
NVIDIA GTX/RTX Consumer Cards (e.g., RTX 3080, RTX 4090)
8-24 GB VRAM
$700-$2,000
Professional (Data Science Workstations):
NVIDIA RTX A-series or previous Quadro series
16-48 GB VRAM
$2,000-$6,000
High-Performance (Server/Cloud):
NVIDIA Tesla/A100/H100
40-80 GB VRAM
$8,000-$30,000+

--- Page 13 ---

Hands-On Code
GPU Acceleration Libraries for Python

--- Page 14 ---

Activity: Checking Your Hardware
Open your laptops and follow these instructions based on your operating system:"
For Mac Users:
Click the Apple menu and select "About This Mac" 1.
You'll see a summary of your CPU 2.
Click "System Report..." then "Graphics/Displays" for GPU details 3.
For Windows Users:
Press Win + X and select "Device Manager"
Expand "Display adapters" to see your GPU(s)
Expand "Processors" to see your CPU
For more detailed information:
Type "dxdiag" in the search bar and run it
Check the "System" tab for CPU info and "Display" tab for GPU details
