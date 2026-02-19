import streamlit as st
from db import *
from llm_engine import classify_query
from rag_engine import query_kb
from identity_matcher import resolve_identity

st.set_page_config(page_title="BookLeaf Support Bot")
st.title("📚 BookLeaf Author Support")

# Initialize DB
init_db()
seed_data()

if "messages" not in st.session_state:
    st.session_state.messages = []

user_email = st.text_input("Enter your registered email")
query = st.chat_input("Ask your query...")

if query and user_email:

    escalated = False
    error_message = None

    try:
        intent_data = classify_query(query)
        intent = intent_data["intent"]
        confidence = intent_data["confidence"]

    except Exception:
        intent = "unknown"
        confidence = 0
        escalated = True
        response = "🚨 AI system error. Human agent notified."

    if not escalated and confidence < 80:
        response = "⚠️ Low confidence detected. Human agent will assist."
        escalated = True

    elif not escalated:
        try:
            author, id_conf = resolve_identity(user_email)

            if not author:
                response = "❌ No author found."
                escalated = True

            elif id_conf < 70:
                response = "⚠️ Multiple profiles found. Manual verification required."
                escalated = True

            elif intent_data["requires_db"]:
                books = get_book_by_author(author[0])

                if not books:
                    response = "No book found."
                    escalated = True

                elif len(books) > 1:
                    response = "Multiple books found. Please specify."
                    escalated = True

                else:
                    book = books[0]

                    if intent == "book_live_status":
                        response = f"🎉 Book Live Date: {book[4]}"

                    elif intent == "royalty_status":
                        response = f"💰 Royalty Status: {book[5]}"

                    elif intent == "add_on_status":
                        response = f"📦 Add-ons: {book[7]}"

                    else:
                        response = "Query requires support review."
                        escalated = True
            else:
                response = f"📘 {query_kb(query)}"

        except Exception as e:
            response = "🚨 System error. Human agent notified."
            escalated = True
            error_message = str(e)

    log_query(
        user_email,
        query,
        intent,
        confidence,
        response,
        int(escalated),
        error_message
    )

    st.chat_message("user").write(query)
    st.chat_message("assistant").write(response)
