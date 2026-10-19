
import streamlit as st

st.title("Stack and Queue Visualizer")

# Initialize
if "created" not in st.session_state:
    st.session_state["created"] = False
    st.session_state["elements"] = []

# Choose Stack or Queue
if not st.session_state["created"]:

    choice = st.radio("Choose Data Structure", ["Stack", "Queue"])

    size = st.text_input("Enter Maximum Size", "5")

    if st.button("Create"):
        try:
            maximum = int(size)

            if maximum < 1 or maximum > 20:
                st.error("Enter a size between 1 and 20.")
            else:
                st.session_state["choice"] = choice
                st.session_state["size"] = maximum
                st.session_state["elements"] = []
                st.session_state["created"] = True
                st.rerun()

        except ValueError:
            st.error("Enter a valid integer size.")

# Stack or Queue operations
else:

    choice = st.session_state["choice"]
    size = st.session_state["size"]
    elements = st.session_state["elements"]

    st.subheader(choice)
    st.write("Maximum Size:", size)

    value = st.text_input("Enter Value", "0")

    col1, col2 = st.columns(2)

    with col1:
        if choice == "Stack":
            insert = st.button("Push")
        else:
            insert = st.button("Enqueue")

    with col2:
        if choice == "Stack":
            remove = st.button("Pop")
        else:
            remove = st.button("Dequeue")

    # Push or Enqueue
    if insert:
        try:
            number = int(value)

            if len(elements) >= size:
                st.error("Overflow! Structure is full.")
            else:
                elements.append(number)
                st.success("Value inserted successfully.")

        except ValueError:
            st.error("Enter a valid integer.")

    # Pop or Dequeue
    if remove:
        if len(elements) == 0:
            st.error("Underflow! Structure is empty.")
        else:
            if choice == "Stack":
                removed = elements.pop()
            else:
                removed = elements.pop(0)

            st.success(f"Removed value: {removed}")

    # Visualization
    st.write("Visualization:")

    if len(elements) == 0:
        st.info("Empty")

    elif choice == "Stack":
        st.write("TOP")

        for x in elements[::-1]:
            st.info(x)

        st.write("BOTTOM")

    else:
        st.write("FRONT → REAR")

        cols = st.columns(len(elements))

        for i in range(len(elements)):
            with cols[i]:
                st.info(elements[i])

    # Start Again
    if st.button("Start Again"):
        st.session_state["created"] = False
        st.session_state["elements"] = []
        st.rerun()
