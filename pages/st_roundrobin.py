import streamlit as st 
from roundrobin import make_pairs

st.write("# Round Robin Scheduler")

entry = st.text_input('Type some names, separated by commas')
people = []

for p in entry.split(','):
    people.append(p)

if len(set(people)) == len(people) and len(people) > 1:
    schedule = make_pairs(people=people)
    st.markdown("## Here's your schedule")
    rounds = len(schedule)
    for round in range(rounds):
        st.markdown(f"### Round {round + 1}")
        output = ""
        for pair in schedule[round]:
            st.markdown(pair)
    