import streamlit as st
import random

# Define quiz questions
quiz_data = {
    "Sport": [
        ("Who captained the All Blacks during their 2011 Rugby World Cup victory?", "Richie McCaw"),
        ("Which Kiwi fighter won the UFC Middleweight Championship in 2019?", "Israel Adesanya"),
        ("What is the nickname of New Zealand’s professional basketball team in the NBL?", "Breakers"),
        ("Who became the first New Zealander to win a major golf tournament in the modern era?", "Lydia Ko"),
        ("Which city hosted the final of the 2022 Women's Cricket World Cup?", "Christchurch"),
        ("Who is New Zealand’s highest try-scorer in Rugby World Cup history?", "Jonah Lomu"),
        ("Which Kiwi athlete won a gold medal in the 2020 Tokyo Olympic triathlon?", "Hayden Wilde"),
        ("What year did the Warriors reach their first NRL Grand Final?", "2002"),
        ("Which New Zealand driver has won multiple IndyCar championships?", "Scott Dixon"),
        ("Which Kiwi boxer held a world heavyweight title in 2017?", "Joseph Parker"),
        # Add more to reach 50+
    ],
    "History": [
        ("Who was New Zealand’s Prime Minister during the peak of the COVID-19 pandemic?", "Jacinda Ardern"),
        ("In what year did the Christchurch earthquakes cause significant damage?", "2011"),
        ("What was the first satellite launched by a New Zealand company?", "Rocket Lab’s ‘Atea-1’"),
        ("Which New Zealand Prime Minister signed the Paris Agreement on climate change?", "John Key"),
        ("When did New Zealand legalize same-sex marriage?", "2013"),
        ("Which treaty signed in 1840 shaped New Zealand’s history?", "Treaty of Waitangi"),
        ("Who was the first female Prime Minister of New Zealand?", "Jenny Shipley"),
        ("When did New Zealand officially implement its nuclear-free policy?", "1987"),
        ("Which major battle occurred in the Waikato region in 1863?", "Battle of Rangiriri"),
        ("Who led the Labour Party to a landslide victory in the 2020 election?", "Jacinda Ardern"),
        # Add more to reach 50+
    ],
    "Pop Culture": [
        ("Which Kiwi actor stars as Homelander in 'The Boys'?", "Antony Starr"),
        ("Who won an Academy Award for directing 'The Power of the Dog'?", "Jane Campion"),
        ("Which New Zealand band released the hit song 'Young Blood'?", "The Naked and Famous"),
        ("Which Wellington-based visual effects company worked on 'Avatar'?", "Weta Digital"),
        ("Which New Zealand singer-songwriter released the album 'Melodrama'?", "Lorde"),
        ("Who is one of New Zealand’s most internationally recognized fashion designers?", "Karen Walker"),
        ("What fantasy series, partly filmed in New Zealand, features dragons?", "Game of Thrones"),
        ("Which Kiwi musician won the Silver Scroll for 'Giant of the Sea'?", "Dudley Benson"),
        ("Which New Zealand comedian stars in 'Our Flag Means Death'?", "Rhys Darby"),
        # Add more to reach 50+
    ],
    "Geography": [
        ("Which New Zealand town is famous for its geothermal activity and mud pools?", "Rotorua"),
        ("What is the name of the longest walking trail in New Zealand?", "Te Araroa Trail"),
        ("Which glacier on the South Island has been retreating due to climate change?", "Franz Josef Glacier"),
        ("Where is New Zealand’s only castle located?", "Dunedin (Larnach Castle)"),
        ("What is the easternmost point of New Zealand’s main islands?", "East Cape"),
        ("What is the mountain range that runs down the South Island?", "Southern Alps"),
        ("Which New Zealand city is the first to see the sunrise?", "Gisborne"),
        ("What is the deepest lake in New Zealand?", "Lake Hauroko"),
        ("Which city is nicknamed the 'Garden City'?", "Christchurch"),
        ("What is New Zealand’s longest river?", "Waikato River"),
        # Add more to reach 50+
    ],
    "Around The Country": [
        ("Where is New Zealand’s tallest building located?", "Auckland (Sky Tower)"),
        ("Which town is known as the ‘Shearing Capital’ of New Zealand?", "Te Kuiti"),
        ("What is the name of the ferry service between Wellington and Picton?", "Interislander"),
        ("Which town hosts the famous ‘Golden Shears’ shearing competition?", "Masterton"),
        ("Where can you visit glowworm caves in New Zealand?", "Waitomo"),
        ("Which town is famous for its annual oyster festival?", "Bluff"),
        ("Which city is home to Te Papa, the national museum?", "Wellington"),
        ("Where can you find the Pancake Rocks rock formations?", "Punakaiki"),
        ("What is the Māori name for New Zealand?", "Aotearoa"),
        ("Which town is well known for its Art Deco architecture?", "Napier"),
        # Add more to reach 50+
    ],
    "Flora/Fauna": [
        ("What is New Zealand’s national bird?", "Kiwi"),
        ("Which native tree is famous for its bright red flowers at Christmas?", "Pōhutukawa"),
        ("What is the largest species of weta?", "Giant weta"),
        ("Which flightless parrot is one of the world’s rarest?", "Kākāpō"),
        ("What is the Māori name for the silver fern?", "Ponga"),
        ("Which native dolphin species is one of the smallest in the world?", "Hector’s dolphin"),
        # Add more to reach 50+
    ]
}

# Streamlit app
st.title("NZ General Knowledge Quiz")
category = st.selectbox("Select a Category:", list(quiz_data.keys()))

if "attempts" not in st.session_state:
    st.session_state.attempts = 3

if st.button("Get Question"):
    st.session_state.question, st.session_state.answer = random.choice(quiz_data[category])
    st.session_state.attempts = 3

st.write(f"### {st.session_state.question}")
user_answer = st.text_input("Your Answer:")

if st.button("Submit Answer"):
    if user_answer.lower() == st.session_state.answer.lower():
        st.success("Correct!")
    else:
        st.session_state.attempts -= 1
        if st.session_state.attempts > 0:
            st.warning(f"Incorrect. You have {st.session_state.attempts} attempts left.")
        else:
            st.error(f"Out of attempts! The correct answer was: {st.session_state.answer}")


