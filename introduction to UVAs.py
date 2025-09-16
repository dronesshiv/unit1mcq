import streamlit as st

# Title
st.title("MCQs – Introduction to UAVs with Explanations")

# Questions data structure
questions = [
    {
        "question": "What is a UAV?",
        "options": ["A manned aircraft with advanced autopilot",
                    "An aircraft that operates without an onboard pilot",
                    "A spacecraft used for deep space missions",
                    "A satellite communication device"],
        "correct": "An aircraft that operates without an onboard pilot",
        "explanation": "UAVs (Unmanned Aerial Vehicles) operate without a pilot on board and are controlled remotely or autonomously."
    },
    {
        "question": "What is included in a UAS besides the UAV?",
        "options": ["Just the camera",
                    "The ground control station and communication links",
                    "Satellite networks only",
                    "Engine components only"],
        "correct": "The ground control station and communication links",
        "explanation": "A UAS includes the UAV, ground control station, and communication links that allow it to be operated."
    },
    {
        "question": "Which system helps UAVs navigate autonomously?",
        "options": ["Manual steering system",
                    "Wind sensors",
                    "GPS and flight control software",
                    "Radar altimeter only"],
        "correct": "GPS and flight control software",
        "explanation": "GPS and flight control software allow UAVs to navigate without human intervention."
    },
    {
        "question": "When was the first recorded use of UAVs in warfare?",
        "options": ["1918", "1945", "1849", "2000"],
        "correct": "1849",
        "explanation": "In 1849, Austria used pilotless balloons to attack Venice, marking the first recorded UAV use in warfare."
    },
    {
        "question": "The Kettering Bug was used during which war?",
        "options": ["World War II", "World War I", "Vietnam War", "Gulf War"],
        "correct": "World War I",
        "explanation": "The Kettering Bug was an early unmanned flying bomb used in World War I by the United States."
    },
    {
        "question": "What was the primary use of UAVs during World War II?",
        "options": ["Delivery of cargo", "Aerial photography", "Target drones for training anti-aircraft gunners", "Long-range surveillance"],
        "correct": "Target drones for training anti-aircraft gunners",
        "explanation": "During WWII, UAVs were mainly used as target drones to train anti-aircraft gunners."
    },
    {
        "question": "Which UAV was widely used for reconnaissance during the Cold War?",
        "options": ["DJI Phantom", "Ryan Model 147 \"Lightning Bug\"", "MQ-9 Reaper", "Quantum Systems Trinity"],
        "correct": "Ryan Model 147 \"Lightning Bug\"",
        "explanation": "The Ryan Model 147 \"Lightning Bug\" was a reconnaissance UAV used extensively in the Vietnam War."
    },
    {
        "question": "What is a key feature of modern military UAVs like the MQ-9 Reaper?",
        "options": ["Low-endurance tasks only", "Real-time data and armed capability", "Manual control without sensors", "Used only for entertainment"],
        "correct": "Real-time data and armed capability",
        "explanation": "Modern UAVs like the MQ-9 Reaper are equipped with sensors, GPS, and weapons, enabling real-time surveillance and combat missions."
    },
    {
        "question": "Which UAV popularized drone usage among hobbyists?",
        "options": ["RQ-1 Predator", "Reginald Denny UAV", "DJI Phantom", "Ryan Lightning Bug"],
        "correct": "DJI Phantom",
        "explanation": "The DJI Phantom made drones accessible and popular for recreational and commercial use."
    },
    {
        "question": "What technology helps UAVs avoid obstacles autonomously?",
        "options": ["Manual override", "Object detection sensors", "Wind compensation algorithm", "Hydraulic control system"],
        "correct": "Object detection sensors",
        "explanation": "Obstacle detection sensors such as LiDAR or cameras help UAVs avoid collisions automatically."
    }
    # Add more questions following the same structure if needed
]

# Sidebar to navigate between questions
st.sidebar.title("Navigation")
q_index = st.sidebar.selectbox("Select Question Number", range(1, len(questions)+1)) - 1

# Display the question
q = questions[q_index]
st.subheader(f"Q{q_index+1}: {q['question']}")

# Show options and capture user input
user_answer = st.radio("Choose an answer:", q["options"])

# Check answer
if st.button("Submit Answer"):
    if user_answer == q["correct"]:
        st.success("✔ Correct!")
    else:
        st.error("✘ Incorrect.")
    st.info(f"**Correct Answer:** {q['correct']}")
    st.write(f"**Explanation:** {q['explanation']}")
