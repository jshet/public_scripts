import streamlit as st 
from roundrobin import make_pairs
import pandas as pd

st.write("# Round Robin Pair Maker")
st.write("Names go in, pairings come out, nobody gets hurt.")

st.markdown("## Names")
st.markdown("Type the names of the people you would like to pair into the text input box below. Separate names with commas. Like this: 'Bob, Sally, Dave, Jill'. When all the names are added, press [Enter] or touch outside the box and the script will do things.")
entry = st.text_input('Names:')
st.markdown('*Example: "Pedro, Wolverine, Seinfeld, Famous Person, Third Wheel, Wingman"*')
people = []


for p in entry.split(','):
    people.append(p.lstrip())

st.markdown("## Pairings")
st.markdown("Copy/paste the below into an email, write it on a whiteboard, send a screenshot in a text.  Or click the button below to download a CSV file and email that to people.")

if len(set(people)) == len(people) and len(people) > 1:
    schedule = make_pairs(people=people)
    schedule_by_person = []
    rounds = len(schedule)
    table_header = ["Name"]

    for round in range(rounds):
        table_header.append(f"Round {round+1}")  

    for p in people:
        p_list = [p]
        for round in range(rounds):
            for pair in schedule[round]:
                if p in pair:
                    for person in pair:
                        if p == person:
                            pass
                        else:
                            p_list.append(person)
        schedule_by_person.append(p_list)
    df = pd.DataFrame(schedule_by_person, columns=table_header)
    style = df.style.hide(axis='index')
    st.write(style.to_html(), unsafe_allow_html=True) 

    df_csv = df.to_csv(index=False).encode('utf-8')
    st.markdown("#")
    st.download_button("Download pairings as CSV", df_csv, "schedule.csv", "text/csv", key='download-csv')

else:
    st.markdown("(Pairings appear down here when names get added up there.)")