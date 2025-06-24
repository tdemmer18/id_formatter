import streamlit as st


def format_ids(input_text):
    ids = [
        id_.strip()
        for id_ in input_text.replace(";", "\n").replace(",", "\n").splitlines()
        if id_.strip()
    ]
    return ", ".join(f"'{id_}'" for id_ in ids)


# App configuration
st.set_page_config(page_title="Document ID Formatter", layout="centered")
st.title("📄 Document ID Formatter")

st.markdown("Paste IDs (one per line, or comma/semicolon-separated):")
input_text = st.text_area("", height=200)

if st.button("Format IDs"):
    if input_text.strip():
        output_text = format_ids(input_text)
        st.text_area("Formatted Output", value=output_text, height=150)
        st.download_button(
            "Download Output as .txt", output_text, file_name="formatted_ids.txt"
        )
        st.code(output_text, language="sql")
    else:
        st.warning("Please enter at least one ID.")
