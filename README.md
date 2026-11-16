# Legal Rights Helper - India (Streamlit)

A chatbot that answers citizens' legal-rights questions strictly from a built-in guide, powered by Gemini.

## Run locally
1. `pip install -r requirements.txt`
2. Open `.streamlit/secrets.toml` and replace the placeholder with your Gemini API key.
3. `streamlit run app.py`

## Deploy on Streamlit Community Cloud
1. Push this folder to GitHub (`.gitignore` already excludes `secrets.toml`).
2. Create the app on share.streamlit.io, main file `app.py`.
3. In Advanced settings > Secrets, paste:
   ```
   GEMINI_API_KEY = "your-key"
   ```

## Files
- `app.py` - Streamlit UI and Gemini call
- `manual.py` - legal guide, system prompt, helplines, sample questions
- `.streamlit/secrets.toml` - API key (private)
