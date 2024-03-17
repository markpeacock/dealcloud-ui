import streamlit as st
import streamlit_antd_components as sac
import streamlit.components.v1 as components

# Setting the page configuration
st.set_page_config(layout="wide")
col1, col2, col3 = st.columns(3)

# Sidebar

# Hierarchy of links for demonstration
# A dictionary where keys are categories and values are dictionaries of links
personas = {
        "Senior Management": "sm",
        "Investment Professsional": "ip",
        "Investor Relations": "ir",
        "Operations": "ops",
        "Staffing Manager": "sm",
        "Fund Operations": "fundops",
        "Assistant": "ass",
        "Legal & Compliance": "ass",
}

# Add personas as radio buttons
persona = st.sidebar.radio("Choose a persona:", list(personas.keys()))

# Menu groups

ip_root_nav = [
    sac.MenuItem('Investment Dashboard', href='https://nordiccapital.dealcloud.eu/portal/pages/11672/reports/37308'),
    sac.MenuItem('Sector Pipeline', href='https://nordiccapital.dealcloud.eu/portal/pages/11672/reports/37631'),
    sac.MenuItem('Interactions', href='https://nordiccapital.dealcloud.eu/portal/pages/11672/reports/15316'),
]

sector_ops_nav = [
    sac.MenuItem('Sector Operations', children=[
                sac.MenuItem('Pipeline Analytics', href="https://nordiccapital.dealcloud.eu/portal/pages/11672/reports/37840"),
                sac.MenuItem('Team Activity Analytics', tag=sac.Tag('New', color='red')),
            ]),
]

ip_contacts_nav = [
    sac.MenuItem('Contacts', children=[
                sac.MenuItem('Personal Contacts', tag=sac.Tag('New', color='red')),
                sac.MenuItem('Realtionships', href="https://nordiccapital.dealcloud.eu/portal/pages/11672/reports/40341"),
                sac.MenuItem('Network Exploration', href="https://nordiccapital.dealcloud.eu/portal/pages/11672/reports/40348"),
                sac.MenuItem('Nexus Search', href="https://nordiccapital.dealcloud.eu/portal/pages/11672/reports/40348"),
            ]),
]

deal_nav = [
    sac.MenuItem('Deal Pipeline', children=[
                sac.MenuItem('Active Deals', href="https://nordiccapital.dealcloud.eu/portal/pages/11672/reports/11679"),
                sac.MenuItem('Pipeline Analytics', href="https://nordiccapital.dealcloud.eu/portal/pages/11672/reports/13936"),
                sac.MenuItem('Pipeline Snapshots', href='https://nordiccapital.dealcloud.eu/portal/pages/11672/reports/37810'),
                sac.MenuItem('Bids and Completions', href='https://nordiccapital.dealcloud.eu/portal/pages/11672/reports/13930'),
                sac.MenuItem('By Sector', href='https://nordiccapital.dealcloud.eu/portal/pages/11672/reports/11683'),
                sac.MenuItem('By Country', href='https://nordiccapital.dealcloud.eu/portal/pages/11672/reports/11685'),
                sac.MenuItem('By Fund', href='https://nordiccapital.dealcloud.eu/portal/pages/11672/reports/37914'),
            ]),
]

companies_nav = [
    sac.MenuItem('Companies', children=[
                sac.MenuItem('Portfolio Companies', href="https://www.google.com"),
            ]),
]

staffing_nav = [
    sac.MenuItem('Staffing', children=[
                sac.MenuItem('Reporting | Members | Flagship Funds', href="https://nordiccapital.dealcloud.eu/portal/pages/11672/reports/31895"),
                sac.MenuItem('Reporting | Members | Evo', href="https://nordiccapital.dealcloud.eu/portal/pages/11672/reports/37248"),
                sac.MenuItem('Reporting | Leaders | Flagship Funds', href="https://nordiccapital.dealcloud.eu/portal/pages/11672/reports/37254"),
                sac.MenuItem('Reporting | Leaders | Evo', href="https://nordiccapital.dealcloud.eu/portal/pages/11672/reports/31978"),
                sac.MenuItem('Project List | Flagship Funds', href="https://nordiccapital.dealcloud.eu/portal/pages/11672/reports/31903"),
                sac.MenuItem('Project List | Evo', href="https://nordiccapital.dealcloud.eu/portal/pages/11672/reports/37238"),
                sac.MenuItem('Intensity | Projects', href="https://nordiccapital.dealcloud.eu/portal/pages/11672/reports/31905"),
                sac.MenuItem('Intensity | Person', href="https://nordiccapital.dealcloud.eu/portal/pages/11672/reports/31926"),
                sac.MenuItem('Intensity | Person (LW)', href="https://nordiccapital.dealcloud.eu/portal/pages/11672/reports/35262"),
                sac.MenuItem('Details | Members', href="https://nordiccapital.dealcloud.eu/portal/pages/11672/reports/31990"),
                sac.MenuItem('Details | Leaders', href="https://nordiccapital.dealcloud.eu/portal/pages/11672/reports/31993"),
                sac.MenuItem('Analytics | Time spent', href="https://nordiccapital.dealcloud.eu/portal/pages/11672/reports/32014"),
                sac.MenuItem('Analytics | Reporting | Flagship Funds', href="https://nordiccapital.dealcloud.eu/portal/pages/11672/reports/32022"),
                sac.MenuItem('Analytics | Reporting | Evo', href="https://nordiccapital.dealcloud.eu/portal/pages/11672/reports/37262"),
                sac.MenuItem('Staffing Analytics | Flagship Funds', href="https://nordiccapital.dealcloud.eu/portal/pages/11672/reports/12796"),
                sac.MenuItem('Staffing Analytics | Evo', href="https://nordiccapital.dealcloud.eu/portal/pages/11672/reports/37264"),
                sac.MenuItem('Value Portfolio Staffing', href="https://nordiccapital.dealcloud.eu/portal/pages/11672/reports/34048"),
            ]),
]

# Define the menu groups based on role

nav = []

if persona == 'Investment Professsional':
    nav = ip_root_nav + sector_ops_nav + deal_nav + companies_nav + ip_contacts_nav

elif persona == 'Staffing Manager':
    nav = staffing_nav

# Finally add to the page
    
with col1:
    sac.menu(variant='subtle', items=nav, open_all=True)