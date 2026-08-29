# 🚀 LeadPilot AI — Autonomous AI Sales Employee

> **Understand Leads. Reason About Intent. Take Action. Remember Everything.**

[![Google ADK](https://img.shields.io/badge/Google-ADK-blue)](https://google.github.io/adk-docs/)
[![Gemini](https://img.shields.io/badge/AI-Gemini-orange)](https://ai.google.dev/)
[![Cloud Run](https://img.shields.io/badge/Google%20Cloud-Cloud%20Run-blue)](https://cloud.google.com/run)
[![Firestore](https://img.shields.io/badge/Database-Cloud%20Firestore-orange)](https://firebase.google.com/docs/firestore)
[![Streamlit](https://img.shields.io/badge/UI-Streamlit-red)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3.x-yellow)](https://www.python.org/)

---

## 🌐 Live Demo

### **LeadPilot AI — Live Application**

👉 https://leadpilot-460215870720.asia-south1.run.app/

LeadPilot is deployed on **Google Cloud Run** with persistent state maintained using **Google Cloud Firestore**.

---

# 🎯 Overview

LeadPilot AI is an **autonomous AI sales employee** designed to automate the lead-management workflow from customer requirement to next action.

Traditional sales systems often stop at collecting or qualifying a lead. LeadPilot goes further.

It can:

- Understand a natural-language customer requirement
- Extract important lead information
- Evaluate purchase intent
- Score the lead from 0–100
- Classify the lead as HOT, WARM, or COLD
- Search property inventory
- Match properties against customer requirements
- Persist lead information in Cloud Firestore
- Schedule a follow-up
- Prepare personalized outreach
- Maintain persistent business memory
- Present the complete workflow through a hosted dashboard

The key idea is:

> **LeadPilot does not just answer a sales request. It reasons about what should happen next and uses tools to move the lead toward conversion.**

---

# 💡 The Problem

Sales teams receive customer leads through websites, forms, advertisements, phone calls, social media, and messaging platforms.

After receiving a lead, a salesperson may need to manually:

1. Read and understand the requirement
2. Determine whether the customer is serious
3. Assign a lead priority
4. Search available inventory
5. Identify matching products/properties
6. Update a CRM
7. Schedule a follow-up
8. Prepare customer communication

This creates fragmented workflows and delays.

A highly interested customer can be lost simply because the next action was not taken quickly enough.

---

# 🚀 Our Solution

LeadPilot converts this fragmented process into an autonomous agentic workflow.

### Traditional workflow

```text
Customer
   ↓
Salesperson
   ↓
Manual Qualification
   ↓
Manual Inventory Search
   ↓
CRM Update
   ↓
Manual Follow-Up
   ↓
Manual Outreach
LeadPilot workflow
Customer Requirement
        ↓
AI Understanding
        ↓
Lead Scoring
        ↓
HOT / WARM / COLD
        ↓
Inventory Search
        ↓
Property Matching
        ↓
Persistent Memory
        ↓
Follow-Up Scheduling
        ↓
Personalized Outreach
        ↓
Next Best Action
🤖 Why LeadPilot Is an AI Agent

LeadPilot is designed as an agentic system, rather than a simple chatbot.

The agent can determine which tools are required to complete a workflow.

The implemented tool workflow includes:

search_properties()
        ↓
save_lead()
        ↓
schedule_followup()
        ↓
execute_outreach()

The agent therefore follows the pattern:

UNDERSTAND
     ↓
REASON
     ↓
DECIDE
     ↓
ACT
     ↓
OBSERVE
     ↓
REMEMBER
     ↓
FOLLOW UP

The objective is to minimize unnecessary human intervention while keeping humans involved when authorization or real-world execution is genuinely required.

🧠 Core Capabilities
1. Lead Understanding

LeadPilot accepts natural-language requirements.

Example:

Hi, I'm Rahul Sharma.

I'm looking for a 2 BHK apartment in Pune,
preferably Baner or Wakad.

My budget is around ₹80 lakh and I want
possession within six months.

The agent extracts:

Customer:
Rahul Sharma

Location:
Pune

Preferred Areas:
Baner / Wakad

Configuration:
2 BHK

Budget:
₹80 Lakh

Possession Requirement:
Within 6 Months
2. AI Lead Scoring

LeadPilot evaluates the quality and urgency of the lead.

Example:

Lead Score: 88 / 100

Classification: HOT

The score is based on factors such as:

Specific requirements
Budget clarity
Location preference
Purchase timeline
Configuration
Purchase intent
3. Intelligent Property Matching

The property-search tool identifies inventory that matches the customer's requirements.

Example:

Customer Requirement
--------------------
2 BHK
Pune
Baner / Wakad
Budget ≤ ₹80 Lakh
Possession ≤ 6 Months

Matching property:

Baner Heights

Location:
Baner, Pune

Configuration:
2 BHK

Price:
₹78 Lakh

Possession:
5 Months

The property is within the customer's specified budget and possession timeline.

4. Persistent Memory

LeadPilot uses Google Cloud Firestore as persistent business memory.

The system can persist information such as:

Customer Profile
Lead Requirements
Lead Score
Lead Classification
Property Match
Follow-Up State

This allows important business state to persist beyond a single model interaction.

Example
Lead
 ↓
LeadPilot
 ↓
Firestore
 ↓
Customer Profile
Qualification
Property Match
Follow-Up
5. Autonomous Follow-Up

For a qualified lead, LeadPilot can schedule the next action.

Example:

FOLLOW-UP STATUS: SCHEDULED

When:
24 Hours

Purpose:
Coordinate Site Visit

Lead:
Rahul Sharma

This transforms the system from a reactive chatbot into a workflow-oriented AI agent.

6. Personalized Outreach

LeadPilot prepares a personalized communication based on the lead's requirements and selected property.

Example:

Hi Rahul Sharma,

Based on your requirement for a 2 BHK in Pune
around ₹80 lakh, we found a strong match:

Baner Heights
₹78 Lakh
Baner, Pune
Possession: 5 Months

Would you like to schedule a site visit?

— LeadPilot AI
Demo limitation

The outreach functionality in this hackathon implementation is simulated.

It prepares and records the outreach action but does not send a real WhatsApp, SMS, or email to a customer.

🏗️ System Architecture
                         CUSTOMER
                            │
                            │
                  Natural Language Lead
                            │
                            ▼
                 ┌──────────────────────┐
                 │     LEADPILOT AI     │
                 │                      │
                 │   Google ADK Agent   │
                 │       + Gemini       │
                 │                      │
                 │ Lead Understanding   │
                 │ Lead Scoring         │
                 │ Decision Making      │
                 └──────────┬───────────┘
                            │
                ┌───────────┼────────────┐
                │           │            │
                ▼           ▼            ▼
       ┌─────────────┐ ┌────────────┐ ┌──────────────┐
       │  Property   │ │ Save Lead  │ │  Follow-Up   │
       │   Search    │ │    Tool    │ │     Tool     │
       │    Tool     │ │            │ │              │
       └──────┬──────┘ └─────┬──────┘ └──────┬───────┘
              │              │               │
              ▼              │               │
       Property Match        │               │
                             ▼               ▼
                      ┌──────────────────────────┐
                      │     Cloud Firestore      │
                      │                          │
                      │   Persistent Business    │
                      │          Memory          │
                      └────────────┬─────────────┘
                                   │
                                   ▼
                         Personalized Outreach
                                   │
                                   ▼
                         ┌───────────────────┐
                         │   Cloud Run UI    │
                         │    Streamlit      │
                         └───────────────────┘
🔄 Complete Agent Workflow
             ┌──────────────────┐
             │ Customer Request │
             └────────┬─────────┘
                      │
                      ▼
             ┌──────────────────┐
             │ Understand Lead  │
             └────────┬─────────┘
                      │
                      ▼
             ┌──────────────────┐
             │ Score & Classify │
             └────────┬─────────┘
                      │
                      ▼
             ┌──────────────────┐
             │ Search Inventory │
             └────────┬─────────┘
                      │
                      ▼
             ┌──────────────────┐
             │ Match Property   │
             └────────┬─────────┘
                      │
                      ▼
             ┌──────────────────┐
             │ Save Lead        │
             └────────┬─────────┘
                      │
                      ▼
             ┌──────────────────┐
             │ Schedule Follow- │
             │ Up               │
             └────────┬─────────┘
                      │
                      ▼
             ┌──────────────────┐
             │ Prepare Outreach │
             └────────┬─────────┘
                      │
                      ▼
             ┌──────────────────┐
             │    Next Action   │
             └──────────────────┘
🛠️ Technology Stack
Technology	Role
Gemini	Natural-language understanding and reasoning
Google ADK	Agent development framework
Python	Agent and application implementation
Cloud Firestore	Persistent business memory
Cloud Run	Production hosting
Streamlit	Web dashboard
Google Cloud	Cloud infrastructure
Google Colab	Development and testing
☁️ Google Cloud Components

LeadPilot uses Google Cloud as the application infrastructure.

Google Cloud
│
├── Gemini
│     └── AI reasoning
│
├── Google ADK
│     └── Agent orchestration
│
├── Cloud Firestore
│     └── Persistent memory
│
├── Cloud Run
│     └── Hosted application
│
├── Cloud Build
│     └── Application build
│
└── Artifact Registry
      └── Container image storage
📊 Example Demonstration
Customer
Rahul Sharma
Requirement
Location:
Pune

Preferred Location:
Baner / Wakad

Configuration:
2 BHK

Budget:
₹80 Lakh

Possession:
Within 6 Months
AI Decision
Lead Score:
88 / 100

Classification:
HOT
Matching Property
Baner Heights

Location:
Baner, Pune

Configuration:
2 BHK

Price:
₹78 Lakh

Possession:
5 Months
Actions
✓ Lead analyzed
✓ Lead qualified
✓ Inventory searched
✓ Property matched
✓ Lead saved to Firestore
✓ Follow-up scheduled
✓ Personalized outreach prepared
🧠 Persistent Memory Example

The Firestore record can contain information similar to:

Customer:
Rahul Sharma

Requirements:
2 BHK, Pune, ₹80 Lakh, possession within 6 months

Lead Score:
88

Classification:
HOT

Property Match:
Baner Heights

Property Price:
₹78 Lakh

Follow-Up:
Scheduled

Purpose:
Coordinate site visit

This demonstrates that the agent is maintaining persistent business state, rather than relying only on conversational context.

🖥️ Dashboard

The hosted Streamlit dashboard provides a visual representation of the agent workflow.

The dashboard displays:

✓ Lead Received
✓ Lead Analyzed
✓ Lead Scored
✓ Inventory Searched
✓ Lead Saved
✓ Follow-Up Scheduled
✓ Outreach Prepared

It also displays:

AI Lead Score
Lead Classification
Property Match
Follow-Up Status
Firestore Connection
Persistent Memory
Personalized Outreach
🌐 Live Application
LeadPilot AI

Cloud Run Deployment:

https://leadpilot-460215870720.asia-south1.run.app/

The application is publicly accessible for demonstration.

📸 Screenshots

Screenshots can be added to the repository under:

screenshots/
├── live-dashboard.png
├── agent-execution.png
└── firestore-memory.png
Live Dashboard

The dashboard demonstrates the complete workflow and persistent memory.

Agent Execution

The development execution demonstrates the agent's tool calls and decision-making.

Firestore

The Firestore view demonstrates persistent lead and workflow state.

🚀 Getting Started
Prerequisites

You will need:

Python 3.x
A Google Cloud project
Google Cloud SDK
A Gemini API key or appropriate Google Cloud authentication
Cloud Firestore enabled
Google Cloud Run enabled for deployment
📦 Installation

Clone the repository:

git clone https://github.com/snehalladdha-PhD/leadpilot-ai.git

Enter the project directory:

cd leadpilot-ai

Install dependencies:

pip install -r requirements.txt
▶️ Run the Dashboard Locally

Run:

streamlit run app.py

The dashboard will be available locally through the Streamlit URL.

☁️ Deploy to Google Cloud Run

The application can be deployed from source using:

gcloud run deploy leadpilot \
    --source . \
    --region asia-south1 \
    --allow-unauthenticated

Cloud Run provides the hosted HTTPS endpoint for the application.

🔐 Security

Sensitive credentials should never be committed to this repository.

Do not upload:

API keys
Service-account JSON files
Passwords
.env files
Private credentials
Access tokens

Google Cloud IAM and environment variables should be used for secure configuration.

⚠️ Demo Limitations

This project is a hackathon prototype demonstrating an autonomous sales workflow.

Current limitations
Property inventory is represented through the demonstration inventory/tool.
Outreach is simulated and is not sent to real customers.
Follow-up scheduling demonstrates workflow state rather than a production CRM calendar integration.
The current dashboard focuses on demonstrating the agent workflow rather than providing a complete enterprise CRM.
Authentication and role-based access control are not part of the prototype.

These components can be extended for production deployments.

🔮 Future Scope

LeadPilot can be extended into a complete autonomous sales platform.

CRM Integration

Integrate with:

Salesforce
HubSpot
Zoho CRM
Custom enterprise CRMs
Communication

Integrate with:

WhatsApp Business API
Email
SMS
Voice calling
Live Inventory

Connect the property-search tool to:

Real-time property databases
Builder APIs
CRM inventory
Enterprise databases
Advanced Intelligence

Future versions can include:

Customer-response prediction
Lead conversion probability
Dynamic lead scoring
Sales forecasting
Recommendation ranking
Conversation intelligence
Voice agents
Multi-agent sales workflows
Enterprise Deployment

Future versions can add:

Authentication
Role-based access
Audit logging
Analytics
Multi-tenant architecture
Human approval workflows
Enterprise CRM integration
🏆 Hackathon Track
Taskmaster — Complete Workflow, Not Just a Chatbot

LeadPilot is designed around a complete multi-step business workflow.

Instead of simply answering:

"What property should Rahul buy?"

the agent is designed to determine:

Who is the lead?
        ↓
How valuable is the lead?
        ↓
What inventory matches?
        ↓
What should be remembered?
        ↓
What should happen next?
        ↓
What communication should be prepared?

This makes LeadPilot an action-oriented agentic workflow.

💼 Business Impact

LeadPilot targets a common operational problem:

The gap between receiving a lead and taking the next sales action.

By automating qualification, matching, persistence and follow-up preparation, LeadPilot can help sales teams:

Reduce manual lead-processing time
Prioritize high-intent customers
Respond more consistently
Reduce missed follow-ups
Maintain customer context
Improve sales-team productivity
Create a repeatable lead-management workflow

The system is designed around the principle:

The value of an AI sales agent is not only in what it says, but in what it does next.

🧪 Demonstrated Workflow

The prototype has demonstrated the following workflow:

Lead Received
      ↓
AI Analysis
      ↓
Lead Score
      ↓
HOT Classification
      ↓
Property Search
      ↓
Property Match
      ↓
Firestore Persistence
      ↓
Follow-Up Scheduling
      ↓
Outreach Preparation

Example result:

Lead Score: 88 / 100
Classification: HOT

Property:
Baner Heights

Price:
₹78 Lakh

Possession:
5 Months

Follow-Up:
Scheduled in 24 Hours

Memory:
Stored in Firestore
📁 Repository Structure
leadpilot-ai/
│
├── app.py
├── requirements.txt
├── .gcloudignore
├── README.md
│
└── screenshots/
    ├── live-dashboard.png
    ├── agent-execution.png
    └── firestore-memory.png
🎥 Demo

The hackathon demonstration covers:

1. Customer requirement
2. AI lead analysis
3. Lead scoring
4. HOT/WARM/COLD classification
5. Property inventory search
6. Property matching
7. Firestore persistent memory
8. Follow-up scheduling
9. Personalized outreach preparation
10. Cloud Run hosted dashboard
🧩 Agent Tools

The LeadPilot agent uses tools to complete the workflow.

search_properties()

Searches available property inventory based on customer requirements.

save_lead()

Persists the lead profile and qualification information.

schedule_followup()

Creates the next follow-up workflow state.

execute_outreach()

Prepares and records a personalized outreach action.

The tools allow the agent to move from reasoning to execution.

🔄 Agentic Design Principle

LeadPilot follows a simple operating principle:

                   ┌─────────────┐
                   │ UNDERSTAND  │
                   └──────┬──────┘
                          ↓
                   ┌─────────────┐
                   │   REASON    │
                   └──────┬──────┘
                          ↓
                   ┌─────────────┐
                   │    ACT      │
                   └──────┬──────┘
                          ↓
                   ┌─────────────┐
                   │   REMEMBER  │
                   └──────┬──────┘
                          ↓
                   ┌─────────────┐
                   │  FOLLOW UP  │
                   └──────┬──────┘
                          ↓
                   ┌─────────────┐
                   │ NEXT ACTION │
                   └─────────────┘
👩‍💻 Author
Snehal Laddha

LeadPilot AI — Autonomous AI Sales Employee

⭐ Final Concept

LeadPilot doesn't just answer a sales request.

It understands the lead, evaluates intent, searches for a match, takes action, remembers the customer, schedules the next step, and prepares personalized outreach.

📜 License

This project was developed as a hackathon prototype.

For demonstration and evaluation purposes.


### One important thing

I intentionally **did not put any fake claims** such as “real WhatsApp automation,” “live property API,” or “production CRM integration.” That makes the README more credible to technical judges.

After you paste and commit this, the next step is:

**GitHub → add `architecture.png` + 3 screenshots → verify repository → record the 3–4 minute demo → final Devpos
