import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Page title
st.title("🏥 Hospital Chatbot")

# Hospital image
st.image(
    "images/hospital.jpeg",
    caption="Multispeciality Hospital",
    width=400
)

# Load dataset
df = pd.read_csv("hospital_dataset.csv")

# TF-IDF model
vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(df["question"])

# Chatbot function
def chatbot(query):

    query = query.lower()

    # Greeting

    if any(
        word in query
        for word in [
            "hi",
            "hello",
            "hey"
        ]
    ):

        return ("Hello! Welcome to our hospital. How can I assist you today?")

    # Thank you

    if "thank" in query:

        return ("You're welcome 😊")

    # Bye

    if "bye" in query:

        return ("Goodbye! Take care.")

    # ICU response

    if "icu" in query:

        st.image(
            "images/icu.jpeg",
            width=400
        )

        return (
            "ICU facility available."
        )

    # Ambulance response

    if "ambulance" in query:

        st.image(
            "images/ambulance.jpeg",
            width=400
        )

        return (
            "Ambulance service available."
        )

    # TF-IDF logic

    query_vec = vectorizer.transform(
        [query]
    )

    similarity = cosine_similarity(
        query_vec,
        X
    )

    score = similarity.max()

    index = similarity.argmax()

    # Fallback

    if score < 0.2:

        return """
Sorry, I could not understand.

Try asking:

• Hospital timing

• Doctor list

• Emergency

• Ambulance

• Insurance

• Appointment

• Services
"""

    return df["answer"][index]


# Chat history

if "messages" not in st.session_state:

    st.session_state.messages = []


# Chat input

user_input = st.chat_input(
    "Ask hospital question"
)


# Process input

if user_input:

    response = chatbot(
        user_input
    )

    st.session_state.messages.append(
        (
            "You",
            user_input
        )
    )

    st.session_state.messages.append(
        (
            "Bot",
            response
        )
    )


# Display history

for sender, msg in st.session_state.messages:

    if sender == "You":

        st.chat_message(
            "user"
        ).write(
            msg
        )

    else:

        st.chat_message(
            "assistant"
        ).write(
            msg
        )