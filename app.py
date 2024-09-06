import streamlit as st
import pandas as pd

# App Title
st.title("SLO and SLI Helper for Engineers")

# Introduction
st.write("""
Welcome to the SLO and SLI Helper App. This tool will help you define Service Level Objectives (SLOs) based on critical user journeys and identify the relevant Service Level Indicators (SLIs) for monitoring these objectives.
""")

# Step 1: Input Service Name
st.header("Step 1: Define Your Service Name")
service_name = st.text_input("Enter the name of your service (e.g., 'User Authentication', 'Payment Processing'):")

# Step 2: Input Critical User Journeys
st.header("Step 2: Define Critical User Journeys")
user_journey = st.text_input("Describe the critical user journey for your service (e.g., 'User login', 'Product purchase', 'Data upload'):")

# Step 3: Input Steps Involved in the User Journey
st.header("Step 3: Define Steps Involved in the User Journey")
journey_steps = st.text_area("List the steps involved in the user journey (e.g., 'User enters login credentials', 'System verifies credentials', 'User is redirected to dashboard'):")

# Helper Section
st.header("Helper: Understanding SLIs for Your Critical User Journey")
st.write("""
**What indicators best represent the user experience for this critical user journey?**

Examples:
- **Availability**: How often is the service accessible?
- **Latency**: What is the response time for requests?
- **Error Rate**: How frequently do errors occur?
- **Throughput**: What is the number of successful transactions?

**For Availability, how will you measure whether the service is accessible?**

Example question: What endpoints or services are critical to this user journey? What status codes indicate success?

**For Latency, what is the maximum acceptable response time for a successful interaction?**

Example: Is 500ms an acceptable threshold for the checkout service response time?

**For Error Rate, what types of errors are considered failures, and how will you track them?**

Example: Will you exclude certain HTTP status codes like 3XX (redirects) and 4XX (client errors) from your total failure count?

**How are Error Rates Calculated?**

The error rate is calculated as the ratio of the number of failed requests to the total number of requests over a specific period. A common formula is:

    Error Rate = (Number of Failed Requests / Total Number of Requests) * 100%

Example: If there were 1000 requests and 10 of them failed, the error rate would be (10/1000) * 100% = 1%.
""")

# Step 4: Identify Relevant SLIs
st.header("Step 4: Identify Relevant SLIs")
sli_questions = {
    "Availability": "Is it critical that the service is available 99.9% of the time or more?",
    "Latency": "Should the response time be within 200ms for 95% of requests?",
    "Error Rate": "Is it important that the error rate is below 1%?",
    "Throughput": "Does the service need to handle a high volume of requests (e.g., 1000 requests per second)?"
}

selected_slis = []

if user_journey:
    st.write(f"**Evaluating SLIs for the journey: {user_journey}**")
    for sli, question in sli_questions.items():
        if st.checkbox(question):
            selected_slis.append(sli)

# Step 5: Input Dependent Services
st.header("Step 5: Define Dependent Services")
dependent_services = st.text_input("List any dependent services relevant to the critical user journey (e.g., 'Authentication Service', 'Payment Gateway', 'Data Storage'):")

# Step 6: Define Realistic SLOs
st.header("Step 6: Define Realistic SLOs")
slo_definitions = []

if selected_slis:
    for sli in selected_slis:
        slo_input = st.text_input(f"Define a realistic SLO for {sli} ")
        if slo_input:
            slo_definitions.append((sli, slo_input))

# Step 7: Display Results in a Table
if slo_definitions and service_name and user_journey and journey_steps:
    st.header("Summary of SLOs, SLIs, Journey Steps, and Dependencies")
    data_rows = []

    for sli, slo in slo_definitions:
        data_rows.append({
            "Service": service_name,
            "User Journey": user_journey,
            "Journey Steps": journey_steps,
            "SLI": sli,
            "SLO": slo,
            "Dependent Services": dependent_services
        })

    # Create a DataFrame from the list of rows
    summary_df = pd.DataFrame(data_rows)

    # Display the summary table
    st.table(summary_df)

# Additional Guidance
st.header("Additional Guidance")
st.write("""
- SLOs should be measurable and aligned with business goals.
- Choose SLIs that accurately reflect the performance of the user journey.
- Regularly review and adjust SLOs and SLIs as your service evolves.
""")
