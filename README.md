# NoorSecure-SecurityPro — A Cloud Security Reference Architecture

**NoorSecure-SecurityPro** is a professional-grade AWS cloud security architecture built to demonstrate secure multi-tier design, IAM best practices, KMS encryption, event-driven monitoring, and serverless authentication patterns. It uses AWS CloudFormation (modular multi-stack), GitHub version control, and real AWS services to mirror real-world security standards.

> 🛡️ Built by Said Noor — AWS Certified Solutions Architect + Security Specialty  
> 🔗 [LinkedIn Profile](https://www.linkedin.com/in/said-noor-710592100)

---

## 🌐 Architecture Overview

This project implements a modular, secure-by-default infrastructure with the following features:

- ✅ **3-tier VPC** across multiple AZs (public, private, and reserved subnets)
- ✅ **IAM least-privilege roles and policies**
- ✅ **CloudTrail + GuardDuty** with central logging and alerts
- ✅ **KMS-managed encryption** and tight key access control
- ✅ **S3 Static Web Hosting** secured with **CloudFront + ACM HTTPS**
- ✅ **Cognito User Pool** authentication with secure hosted UI
- ✅ **Lambda APIs** protected by IAM and integrated with Cognito
- ✅ **Event-driven alerts** via SNS, CloudWatch Alarms, and Lambda triggers
- ✅ **Separate CloudFormation stacks** for each layer of the architecture (IaC best practice)

---

## 🛠️ Technologies Used

- **AWS CloudFormation** – Infrastructure as Code (IaC)
- **Amazon VPC**, **IAM**, **KMS**, **S3**, **CloudFront**, **ACM**
- **AWS Cognito**, **Lambda**, **SNS**, **CloudTrail**, **CloudWatch**
- **AWS CloudShell CLI** for secure deployment
- **Python** – used in Lambda functions and helper scripts
- **Git + GitHub** – version control and recruiter-facing portfolio

---

## 🧠 Skills Demonstrated

- 🔐 Strong grasp of AWS cloud security architecture
- 👥 IAM policy design, least-privilege access, and federated auth
- 🔑 Advanced encryption using KMS (with tight key policies)
- 📜 Audit logging using CloudTrail + GuardDuty
- ☁️ Scalable S3 static hosting secured by CloudFront with HTTPS
- ⚙️ Hands-on experience with Infrastructure as Code (CloudFormation)
- 🧰 Modular multi-stack deployment approach
- 🧠 Knowledge aligned with **AWS Security Specialty (SCS-C02)** and **SAA-C03** certification exams

---

## 🚀 How to Deploy (via AWS CloudShell)

1. Open [AWS CloudShell](https://us-east-1.console.aws.amazon.com/cloudshell/home)
2. Clone the project:

```bash
git clone https://github.com/saidnoor-bot/NoorSecure-SecurityPro.git
cd NoorSecure-SecurityPro

