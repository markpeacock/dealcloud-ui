import streamlit as st

# Setting the page configuration
st.set_page_config(layout="wide")

# Sidebar
st.sidebar.title("Navigation")
# List of links for demonstration
links = {
    "OpenAI": "https://www.openai.com",
    "Google": "https://www.google.com",
    "Wikipedia": "https://www.wikipedia.org",
}

# Display links in the sidebar and return the selected one
selected_link = st.sidebar.radio("Choose a site:", list(links.keys()))

# Main page
# Use columns to allocate space, with 20% for the sidebar implicitly and 80% for the content
col1, col2 = st.columns([1, 4])

# Display the iframe in the second column based on selected link
with col2:
    st.write(f"### Displaying: {selected_link}")
    st.markdown(f'<iframe src="{links[selected_link]}" width="100%" height="600"></iframe>', unsafe_allow_html=True)

