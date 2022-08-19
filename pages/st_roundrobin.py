import streamlit as st 
from roundrobin import make_pairs

st.write("# Round Robin Pair Maker")
st.write("Names go in, pairings come out, nobody gets hurt.")

st.markdown("## Names")
st.markdown("Type the names of the people you would like to pair into the text input box below. Separate names with commas. Like this: 'Bob, Sally, Dave, Jill'. When all the names are added, press [Enter] or touch outside the box and the script will do things.")
entry = st.text_input('Names:')
st.markdown('*Example: "Pedro, Wolverine, Seinfeld, Famous Person, Third Wheel, Wingman"*')
people = []


for p in entry.split(','):
    people.append(p)

st.markdown("## Pairings")
if len(set(people)) == len(people) and len(people) > 1:
    schedule = make_pairs(people=people)
    rounds = len(schedule)
    for round in range(rounds):
        st.markdown(f"#### Round {round + 1}")
        output = ""
        for pair in schedule[round]:
            output+=pair[0]
            output+=" and "
            output+=pair[1]
            output+=" | "    
        st.write(output[:-2])  # remove the last | character    
    st.markdown("## Pairings by people")
    for p in people:
        st.markdown(f"#### {p}'s pairings")
        for round in range(rounds):
            for pair in schedule[round]:
                if p in pair:
                    for person in pair:
                        if p == person:
                            pass
                        else:
                            st.markdown(f"**Round {round+1}:** {person}")
else:
    st.markdown("(Pairings appear down here when names get added up there.)")