import streamlit as st
import random

# Define quiz questions
quiz_data = {
    "Sport": [
        ("Who is New Zealand’s highest test run scorer in cricket?", "Kane Williamson"),
        ("Which rugby team is known as the All Blacks?", "New Zealand National Rugby Team"),
        ("Who won New Zealand's first Olympic gold medal?", "Jack Lovelock"),
        ("What is the national sport of New Zealand?", "Rugby Union"),
        ("Which New Zealand city hosts the annual ASB Classic tennis tournament?", "Auckland"),
        ("Who was the first New Zealander to win a Formula 1 World Championship?", "Denny Hulme"),
        ("Which New Zealand golfer won the 2005 U.S. Open?", "Michael Campbell"),
        ("Which famous New Zealand horse won the Melbourne Cup three times?", "Makybe Diva"),
        ("Who was the first New Zealander to win the Tour de France?", "No New Zealander has won"),
        ("Which team did the All Blacks defeat in the 2015 Rugby World Cup final?", "Australia"),
        # Add remaining questions up to 30
    ],
    "History": [
        ("In what year did New Zealand become the first country to grant women the right to vote?", "1893"),
        ("Who was the first European to discover New Zealand?", "Abel Tasman"),
        ("What treaty was signed between the British Crown and Māori chiefs in 1840?", "Treaty of Waitangi"),
        ("Who was New Zealand's first Prime Minister?", "Henry Sewell"),
        ("Which famous New Zealander climbed Mount Everest in 1953?", "Sir Edmund Hillary"),
        ("What year did New Zealand officially become a dominion?", "1907"),
        ("Which city was New Zealand's capital before Wellington?", "Auckland"),
        ("Who led the Māori resistance during the New Zealand Wars?", "Te Kooti"),
        ("What year did New Zealand abolish the death penalty?", "1989"),
        ("Who was New Zealand’s longest-serving Prime Minister?", "Richard Seddon"),
        # Add remaining questions up to 30
    ],
    "Pop Culture": [
        ("Which New Zealand director made the Lord of the Rings movies?", "Peter Jackson"),
        ("What is the name of the popular New Zealand comedy duo?", "Flight of the Conchords"),
        ("Which New Zealand singer is known for the hit song 'Royals'?", "Lorde"),
        ("Which TV series was filmed in New Zealand and featured Hercules and Xena?", "Hercules: The Legendary Journeys & Xena: Warrior Princess"),
        ("Who is New Zealand's most famous fashion designer?", "Karen Walker"),
        ("Which New Zealand actor played Dr. Alan Grant in Jurassic Park?", "Sam Neill"),
        ("What is the name of the famous New Zealand film about a Māori girl breaking traditions?", "Whale Rider"),
        ("Who is the lead singer of Crowded House?", "Neil Finn"),
        ("Which New Zealand-made animated film won an Academy Award in 2005?", "The Lion, the Witch and the Wardrobe (VFX)"),
        ("What New Zealand radio host is known for his breakfast show on The Edge?", "Jay-Jay Feeney"),
        # Add remaining questions up to 30
    ],
    "Geography": [
        ("What is the name of New Zealand’s tallest mountain?", "Aoraki / Mount Cook"),
        ("Which city is known as the ‘City of Sails’?", "Auckland"),
        ("What is the longest river in New Zealand?", "Waikato River"),
        ("Which is New Zealand's largest lake?", "Lake Taupō"),
        ("Which island is larger, the North Island or South Island?", "South Island"),
        ("What is the name of the active volcano on White Island?", "Whakaari / White Island"),
        ("Which New Zealand region is famous for its wine production?", "Marlborough"),
        ("What is the easternmost city in New Zealand?", "Gisborne"),
        ("Where is Milford Sound located?", "Fiordland National Park"),
        ("What is the capital of New Zealand?", "Wellington"),
        # Add remaining questions up to 30
    ],
    "Around The Country": [
        ("What is the name of New Zealand’s capital city?", "Wellington"),
        ("Where can you find the Hobbiton movie set?", "Matamata"),
        ("Which New Zealand town is famous for its hot pools and geysers?", "Rotorua"),
        ("Which beach is known for its black sand near Auckland?", "Piha Beach"),
        ("Which city is home to the famous Dunedin Railway Station?", "Dunedin"),
        ("What is the name of New Zealand’s largest national park?", "Fiordland National Park"),
        ("Which town is known as the Art Deco capital of New Zealand?", "Napier"),
        ("What is the Māori name for New Zealand?", "Aotearoa"),
        ("Which New Zealand city is known for its historic tramway system?", "Christchurch"),
        ("Where is the Sky Tower located?", "Auckland"),
        # Add remaining questions up to 30
    ]
}

# Streamlit app
st.title("NZ General Knowledge Quiz")
category = st.selectbox("Select a Category:", list(quiz_data.keys()))
if st.button("Get Question"):
    question, answer = random.choice(quiz_data[category])
    st.write(f"### {question}")
    if st.button("Show Answer"):
        st.write(f"**Answer:** {answer}")

