import streamlit as st

# Initialize the board
if "board" not in st.session_state:
    st.session_state.board = [""] * 9
    st.session_state.current_player = "X"
    st.session_state.winner = None

# Function to check for winner
def check_winner():
    b = st.session_state.board
    wins = [(0,1,2), (3,4,5), (6,7,8),  # rows
            (0,3,6), (1,4,7), (2,5,8),  # cols
            (0,4,8), (2,4,6)]           # diagonals
    for i,j,k in wins:
        if b[i] == b[j] == b[k] and b[i] != "":
            return b[i]
    if "" not in b:
        return "Tie"
    return None

# Game title
st.title("🎮 Tic Tac Toe")
st.subheader("Player Turn: " + st.session_state.current_player)

# Create 3×3 buttons grid
cols = st.columns(3)
for i in range(3):
    for j in range(3):
        idx = i*3 + j
        with cols[j]:
            if st.button(st.session_state.board[idx] or " ", key=idx, use_container_width=True):
                if st.session_state.board[idx] == "" and st.session_state.winner is None:
                    st.session_state.board[idx] = st.session_state.current_player
