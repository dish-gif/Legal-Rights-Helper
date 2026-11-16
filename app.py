"""Legal Rights Helper - India (Streamlit + Gemini)."""

import streamlit as st
from google import genai
from google.genai import types

from manual import HELPLINES, MANUAL, SAMPLE_QUESTIONS, SYSTEM_PROMPT

DEFAULT_MODEL = "gemini-3.5-flash-lite"

st.set_page_config(page_title="Legal Rights Helper - India", page_icon="⚖️", layout="centered")


# ---------- Gemini client (API key comes from .streamlit/secrets.toml) ----------
@st.cache_resource
def get_client() -> genai.Client:
    return genai.Client(api_key=st.secrets["GEMINI_API_KEY"])


def get_model_name() -> str:
    return st.secrets.get("GEMINI_MODEL", DEFAULT_MODEL)


def ask_gemini(history: list[dict]) -> str:
    """Send the whole chat history so follow-up questions work."""
    contents = [
        types.Content(
            role="user" if m["role"] == "user" else "model",
            parts=[types.Part(text=m["content"])],
        )
        for m in history
    ]
    response = get_client().models.generate_content(
        model=get_model_name(),
        contents=contents,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT + "\n\nGUIDE:\n" + MANUAL,
        ),
    )
    return response.text or "Sorry, I could not generate an answer. Please try again."


# ---------- Guard: missing API key ----------
try:
    _ = st.secrets["GEMINI_API_KEY"]
except Exception:
    st.error(
        "GEMINI_API_KEY not found. Add it to `.streamlit/secrets.toml` "
        "(locally) or to the app's Secrets settings (Streamlit Community Cloud)."
    )
    st.stop()

# ---------- Session state ----------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------- Sidebar ----------
with st.sidebar:
    st.header("📞 Important Helplines")
    for name, number in HELPLINES:
        st.markdown(f"**{name}:** {number}")
    st.divider()
    if st.button("🗑️ Clear chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
    st.caption("General information only, not legal advice. Laws change and state rules differ.")

# ---------- Header ----------
st.title("⚖️ Legal Rights Helper")
st.caption("Ask about FIRs, arrest rights, consumer complaints, RTI, tenant rights, free legal aid, "
           "cyber fraud and workplace rights. You can write in English, Hindi or Punjabi.")

# ---------- Chat history ----------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---------- Sample questions (only on an empty chat) ----------
clicked = None
if not st.session_state.messages:
    st.write("**Try asking:**")
    for i, q in enumerate(SAMPLE_QUESTIONS):
        if st.button(q, key=f"sample_{i}", use_container_width=True):
            clicked = q

# ---------- Input ----------
question = st.chat_input("Ask your question...") or clicked

if question:
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        with st.spinner("Looking through the guide..."):
            try:
                answer = ask_gemini(st.session_state.messages)
            except Exception as e:
                answer = f"⚠️ Something went wrong while contacting Gemini: `{e}`"
        st.markdown(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})
