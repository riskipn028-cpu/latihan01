import streamlit as st

pages = [
    st.page(page="pages/page1.py", title="Home", icon="🏠"),
    st.page(page="pages/page2.py", title="visualisasi Data", icon="📈"),
    st.page(page="pages/page3.py", title="Settings", icon="⚙️")
]

pg = st.navigation(
    pages,
    position="sidebar",
    expanded=True
)

pg.run()
