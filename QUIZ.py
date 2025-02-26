import streamlit as st
import random

# Define quiz questions
quiz_data = {
    "Sport": [
        ("Who captained the All Blacks during their 2011 Rugby World Cup victory?", "Richie McCaw"),
        ("Which New Zealander won the UFC Middleweight Championship in 2019?", "Israel Adesanya"),
        ("What is the name of New Zealand’s professional basketball team in the NBL?", "New Zealand Breakers"),
        ("Who became the first Kiwi to win a PGA Tour major in 2013?", "Lydia Ko"),
        ("Which New Zealand city hosted the 2022 Women's Cricket World Cup final?", "Christchurch"),
        ("Who holds the record for the most points scored in a single Rugby World Cup?", "Jonah Lomu"),
        ("Which New Zealander won gold in the 2020 Tokyo Olympic triathlon?", "Hayden Wilde"),
        ("What year did the Warriors make their first NRL Grand Final?", "2002"),
        ("Who is the most successful New Zealand IndyCar driver?", "Scott Dixon"),
        ("Which Kiwi boxer held multiple heavyweight world titles in 2017?", "Joseph Parker"),
        # Add more to reach 50+
    ],
    "History": [
        ("Who was the Prime Minister of New Zealand during the COVID-19 pandemic?", "Jacinda Ardern"),
        ("Which year did the Christchurch earthquakes cause major devastation?", "2011"),
        ("What was the name of New Zealand's first satellite launched into space?", "Rocket Lab’s ‘Atea-1’"),
        ("Which New Zealand PM signed the Paris Agreement on climate change in 2016?", "John Key"),
        ("In what year did New Zealand legalize same-sex marriage?", "2013"),
        ("Which treaty was signed between the British Crown and Māori chiefs in 1840?", "Treaty of Waitangi"),
        ("Who was New Zealand's first female Prime Minister?", "Jenny Shipley"),
        ("When did New Zealand officially become nuclear-free?", "1987"),
        ("Which famous battle took place in Waikato in 1863?", "Battle of Rangiriri"),
        ("Who led the New Zealand Labour Party to victory in 2020?", "Jacinda Ardern"),
        # Add more to reach 50+
    ],
    "Pop Culture": [
        ("Which New Zealand actor played Homelander in 'The Boys'?", "Antony Starr"),
        ("Who directed the 2021 film 'The Power of the Dog' and won an Academy Award?", "Jane Campion"),
        ("Which New Zealand band released the song 'Young Blood' in 2010?", "The Naked and Famous"),
        ("What is the name of the New Zealand-based visual effects company that worked on Avatar?", "Weta Digital"),
        ("Who played the role of Peeta Mellark in The Hunger Games, but was born in New Zealand?", "No one - trick question!"),
        ("Which New Zealand pop star released the album 'Melodrama'?", "Lorde"),
        ("Who is known as New Zealand’s most famous fashion designer?", "Karen Walker"),
        ("Which popular TV series was filmed in New Zealand and featured dragons?", "Game of Thrones (some scenes)"),
        ("Which Kiwi musician won the Silver Scroll for 'Giant of the Sea'?", "Dudley Benson"),
        ("Which New Zealand comedian stars in 'Our Flag Means Death'?", "Rhys Darby"),
        # Add more to reach 50+
    ],
    "Geography": [
        ("Which New Zealand region is known for its geothermal activity and mud pools?", "Rotorua"),
        ("What is the name of the longest walking trail in New Zealand?", "Te Araroa Trail"),
        ("Which New Zealand glacier has been retreating due to climate change?", "Franz Josef Glacier"),
        ("Where can you find New Zealand’s only castle?", "Dunedin (Larnach Castle)"),
        ("What is the name of the easternmost point of New Zealand’s main islands?", "East Cape"),
        ("What is the name of the mountain range running down the South Island?", "Southern Alps"),
        ("Which New Zealand town is closest to the international date line?", "Gisborne"),
        ("What is the name of the deepest lake in New Zealand?", "Lake Hauroko"),
        ("Which city is known as the 'Garden City'?", "Christchurch"),
        ("What is the longest river in New Zealand?", "Waikato River"),
        # Add more to reach 50+
    ],
    "Around The Country": [
        ("Where can you find New Zealand's tallest building?", "Auckland (Sky Tower)"),
        ("Which New Zealand town is famous for its annual 'Running of the Sheep'?", "Te Kuiti"),
        ("What is the name of the inter-island ferry service between Wellington and Picton?", "Interislander"),
        ("Which small town hosts the annual ‘Golden Shears’ shearing competition?", "Masterton"),
        ("Where is the famous glowworm cave attraction?", "Waitomo Caves"),
        ("Which town is known for its annual 'Bluff Oyster Festival'?", "Bluff"),
        ("Which city is home to Te Papa, New Zealand’s national museum?", "Wellington"),
        ("Where is the iconic 'Pancake Rocks' formation?", "Punakaiki"),
        ("What is the Māori name for New Zealand?", "Aotearoa"),
        ("Which town is famous for its Art Deco architecture?", "Napier"),
        # Add more to reach 50+
    ]
}

# Streamlit app
st.title("NZ General Knowledge Quiz")
category = st.selectbox("Select a Category:", list(quiz_data.keys()))

if "asked_questions" not in st.session_state:
    st.session_state.asked_questions = {key: set() for key in quiz_data}

if "question" not in st.session_state:
    st.session_state.question = ""
    st.session_state.answer = ""

if st.button("Get Question"):
    available_questions = [q for q in quiz_data[category] if q[0] not in st.session_state.asked_questions[category]]
    if available_questions:
        st.session_state.question, st.session_state.answer = random.choice(available_questions)
        st.session_state.asked_questions[category].add(st.session_state.question)
    else:
        st.session_state.question = "No more unique questions left in this category!"
        st.session_state.answer = ""

st.write(f"### {st.session_state.question}")

if st.button("Show Answer") and st.session_state.answer:
    st.write(f"**Answer:** {st.session_state.answer}")

