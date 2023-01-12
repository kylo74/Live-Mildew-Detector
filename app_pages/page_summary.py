import streamlit as st

def page_summary_body():
    st.write("## Project Summary")

    st.info(
        f"*The cherry plantation crop from Farmy & Foods is facing a challenge where their "
        f" cherry plantations have been presenting powdery mildew "
        f" Currently, the process is to manually verify if a given "
        f" cherry tree contains powdery mildew. An employee spends around 30 minutes ")

    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/GyanShashwat1611/WalkthroughProject01/blob/main/README.md).")
    

    st.success(
        f"The project has 2 business requirements:\n"
        f"* 1 - The client is interested in having a study to differentiate "
        f"a parasitized and uninfected cell visually.\n"
        f"* 2 - The client is interested to tell whether a given cell contains malaria parasite or not. "
        )