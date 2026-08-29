
import streamlit as st
from google.cloud import firestore
from datetime import datetime

# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------

st.set_page_config(
    page_title="LeadPilot AI",
    page_icon="🚀",
    layout="wide"
)

# ---------------------------------------------------------
# DATABASE
# ---------------------------------------------------------

PROJECT_ID = "leadpilot-hackathon-30081986"

try:
    db = firestore.Client(
        project=PROJECT_ID,
        database="leadpilot"
    )
    firestore_connected = True
except Exception:
    db = None
    firestore_connected = False


# ---------------------------------------------------------
# DEMO DATA
# ---------------------------------------------------------

lead = {
    "customer_name": "Rahul Sharma",
    "location": "Pune",
    "property_type": "2 BHK",
    "budget_lakh": 80,
    "timeline_months": 6,
    "lead_score": 88,
    "classification": "HOT",
    "status": "QUALIFIED"
}

property_match = {
    "project": "Baner Heights",
    "location": "Baner, Pune",
    "type": "2 BHK",
    "price_lakh": 78,
    "possession_months": 5,
    "match": 96
}

actions = [
    ("Lead analyzed", True),
    ("Lead qualified", True),
    ("Property inventory searched", True),
    ("Baner Heights matched", True),
    ("Lead saved to Firestore", firestore_connected),
    ("Follow-up scheduled", True),
    ("Personalized outreach prepared", True)
]


# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------

st.title("🚀 LeadPilot AI")

st.subheader("Autonomous AI Sales Employee")

st.caption(
    "Understand → Reason → Act → Remember → Follow Up"
)

st.divider()


# ---------------------------------------------------------
# TOP METRICS
# ---------------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "AI Lead Score",
        f"{lead['lead_score']}/100"
    )

with col2:
    st.metric(
        "Classification",
        lead["classification"]
    )

with col3:
    st.metric(
        "Autonomy",
        "87%"
    )

with col4:
    st.metric(
        "Actions",
        "7"
    )


st.divider()


# ---------------------------------------------------------
# LEAD INFORMATION
# ---------------------------------------------------------

left, right = st.columns([1, 1])

with left:

    st.subheader("👤 Lead Intelligence")

    st.markdown(
        f"""
**Customer:** {lead['customer_name']}

**Location:** {lead['location']}

**Requirement:** {lead['property_type']}

**Budget:** ₹{lead['budget_lakh']} Lakh

**Timeline:** {lead['timeline_months']} months

**Purchase Intent:** 🔥 **High**
"""
    )

    st.success(
        "HOT LEAD — Immediate action recommended"
    )


with right:

    st.subheader("🏠 Best Property Match")

    st.markdown(
        f"""
### {property_match['project']}

📍 **{property_match['location']}**

🏠 **{property_match['type']}**

💰 **₹{property_match['price_lakh']} Lakh**

📅 **Possession: {property_match['possession_months']} months**

🎯 **AI Match Score: {property_match['match']}%**
"""
    )

    st.info(
        "Strong match: within budget and timeline"
    )


st.divider()


# ---------------------------------------------------------
# AUTONOMOUS ACTIONS
# ---------------------------------------------------------

st.subheader("🤖 Autonomous Actions")

for action, completed in actions:

    if completed:
        st.markdown(
            f"✅ **{action}**"
        )
    else:
        st.markdown(
            f"⏳ **{action}**"
        )


st.divider()


# ---------------------------------------------------------
# WORKFLOW STATUS
# ---------------------------------------------------------

st.subheader("🔄 Agent Workflow")

workflow = [
    "Lead Received",
    "Lead Analyzed",
    "Lead Scored",
    "Inventory Searched",
    "Lead Saved",
    "Follow-Up Scheduled",
    "Outreach Prepared"
]

cols = st.columns(len(workflow))

for i, step in enumerate(workflow):

    with cols[i]:
        st.success(
            f"✓\n\n{step}"
        )


st.divider()


# ---------------------------------------------------------
# FOLLOW-UP
# ---------------------------------------------------------

follow_left, follow_right = st.columns([1, 1])

with follow_left:

    st.subheader("📅 Follow-Up")

    st.markdown(
        """
**Status:** 🟢 SCHEDULED

**When:** 24 hours

**Purpose:** Coordinate site visit

**Lead:** Rahul Sharma
"""
    )


with follow_right:

    st.subheader("🧠 Persistent Memory")

    if firestore_connected:

        st.success(
            "Firestore Connected ✓"
        )

        st.markdown(
            """
**Lead profile:** Stored ✓

**Qualification:** Stored ✓

**Property match:** Available ✓

**Follow-up state:** Stored ✓
"""
        )

    else:

        st.warning(
            "Firestore connection unavailable"
        )


st.divider()


# ---------------------------------------------------------
# OUTREACH
# ---------------------------------------------------------

st.subheader("💬 Personalized Outreach")

st.code(
f"""Hi {lead['customer_name']},

Based on your requirement for a {lead['property_type']}
in Pune around ₹{lead['budget_lakh']} lakh, we found a
strong match:

🏠 {property_match['project']}
💰 ₹{property_match['price_lakh']} Lakh
📍 {property_match['location']}
📅 Possession: {property_match['possession_months']} months

Would you like to schedule a site visit?

— LeadPilot AI""",
language="text"
)

st.caption(
    "Demo communication is simulated and is not sent to a real customer."
)


# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------

st.divider()

st.caption(
    "LeadPilot AI • Google ADK • Gemini • Firestore • Cloud Run"
)
