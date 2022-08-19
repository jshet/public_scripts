import streamlit as st 
from roundrobin import make_pairs

st.write("# Round Robin Scheduler")

entry = st.text_input('Type some names here, separated by commas.', value="Bob, Sue, Jim, Kelly, Dave, Betty, Pria")
people = []

for p in entry.split(','):
    people.append(p)

if len(set(people)) == len(people) and len(people) > 1:
    schedule = make_pairs(people=people)
    st.markdown("## Meeting schedule")
    rounds = len(schedule)
    for round in range(rounds):
        st.markdown(f"### Round {round + 1}")
        output = ""
        for pair in schedule[round]:
            output+=pair[0]
            output+=" and "
            output+=pair[1]
            output+=" | "    
        st.write(output)    
    for p in people:
        st.write(f"### Schedule for {p}")
        for round in range(rounds):
            for pair in schedule[round]:
                if p in pair:
                    for person in pair:
                        if p == person:
                            pass
                        else:
                            st.write(f"Round {round+1}: {person}")