import streamlit as st

# Initialize session state
if 'q_index' not in st.session_state:
    st.session_state.q_index = 0
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'answers' not in st.session_state:
    st.session_state.answers = []

st.title("Drone Technology – MCQs with Explanations")

# Questions list
questions = [
    {
        "question": "What does UAV stand for?",
        "options": ["Unmanned Aerial Vehicle", "Universal Aerial Vision", "Underwater Autonomous Vehicle", "Unidentified Airborne Vector"],
        "correct": "Unmanned Aerial Vehicle",
        "explanation": "UAV stands for Unmanned Aerial Vehicle, which operates without a pilot on board."
    },
    {
        "question": "What is a common use of drones?",
        "options": ["Space exploration", "Agriculture monitoring", "Deep-sea diving", "Nuclear power generation"],
        "correct": "Agriculture monitoring",
        "explanation": "Drones are widely used in agriculture to monitor crops, assess field health, and optimize yields."
    },
    {
        "question": "Which sensor helps drones maintain altitude?",
        "options": ["GPS", "Accelerometer", "Barometer", "Camera"],
        "correct": "Barometer",
        "explanation": "A barometer measures air pressure, helping drones maintain consistent altitude during flight."
    },
    {
        "question": "Which of the following is a benefit of drone technology?",
        "options": ["Increased human labor", "Reduced efficiency", "Access to hard-to-reach areas", "Requires large runways"],
        "correct": "Access to hard-to-reach areas",
        "explanation": "Drones can reach remote or dangerous areas safely and efficiently."
    },
    {
        "question": "What enables drones to navigate precisely?",
        "options": ["Wind speed", "GPS systems", "Radar altimeter only", "Manual steering"],
        "correct": "GPS systems",
        "explanation": "GPS technology allows drones to navigate and follow precise flight paths."
    },
    {
        "question": "Which drone type can hover in place?",
        "options": ["Fixed-wing", "Multirotor", "Glider", "Jet-powered"],
        "correct": "Multirotor",
        "explanation": "Multirotor drones can hover, making them ideal for tasks like photography and inspection."
    },
    {
        "question": "What is the primary energy source for most small drones?",
        "options": ["Lead-acid batteries", "Lithium Polymer (LiPo) batteries", "Solar panels", "Fuel cells"],
        "correct": "Lithium Polymer (LiPo) batteries",
        "explanation": "LiPo batteries are lightweight and provide the necessary power for drone motors."
    },
    {
        "question": "Why are drones useful in disaster management?",
        "options": ["They increase chaos", "They provide quick aerial assessment", "They block communication signals", "They are too slow"],
        "correct": "They provide quick aerial assessment",
        "explanation": "Drones help survey disaster areas quickly, providing critical data for rescue and recovery."
    },
    {
        "question": "What is a drone’s payload?",
        "options": ["Battery", "Camera or sensors", "Propellers", "Landing gear"],
        "correct": "Camera or sensors",
        "explanation": "The payload includes equipment like cameras or sensors used for specific tasks."
    },
    {
        "question": "Which technology helps drones avoid obstacles?",
        "options": ["Barometer", "GPS", "Object detection sensors", "Manual control"],
        "correct": "Object detection sensors",
        "explanation": "Sensors such as LiDAR or cameras help drones detect and avoid obstacles in their path."
    },
    {
        "question": "What is a drawback of multirotor drones?",
        "options": ["They can't hover", "Limited flight time due to battery", "They require large airports", "They are too aerodynamic"],
        "correct": "Limited flight time due to battery",
        "explanation": "Multirotor drones often have shorter flight durations due to battery capacity."
    },
    {
        "question": "Which industry uses drones for surveying land?",
        "options": ["Healthcare", "Construction", "Retail", "Hospitality"],
        "correct": "Construction",
        "explanation": "Drones are used in construction for mapping sites, monitoring progress, and surveying terrain."
    },
    {
        "question": "What is the role of a flight controller?",
        "options": ["Store energy", "Control motors and stabilize flight", "Capture images", "Transmit signals"],
        "correct": "Control motors and stabilize flight",
        "explanation": "The flight controller processes sensor data to maintain stable and controlled flight."
    },
    {
        "question": "How does RTK GPS improve drone operation?",
        "options": ["Provides voice commands", "Gives centimeter-level accuracy", "Reduces payload capacity", "Increases drag"],
        "correct": "Gives centimeter-level accuracy",
        "explanation": "RTK GPS improves navigation precision, essential for mapping and surveying."
    },
    {
        "question": "Which feature is common in drones used for filmmaking?",
        "options": ["Heavy payloads", "Stabilized camera gimbals", "Manual propellers", "No navigation system"],
        "correct": "Stabilized camera gimbals",
        "explanation": "Camera gimbals help stabilize footage, providing smooth video shots during filming."
    },
    {
        "question": "Why is balancing the center of gravity important?",
        "options": ["It increases speed only", "It ensures stable flight", "It reduces weight only", "It makes drones waterproof"],
        "correct": "It ensures stable flight",
        "explanation": "A balanced center of gravity helps prevent vibration and instability during flight."
    },
    {
        "question": "Which part of a drone helps regulate voltage and current to motors?",
        "options": ["GPS", "ESC (Electronic Speed Controller)", "Camera", "Landing gear"],
        "correct": "ESC (Electronic Speed Controller)",
        "explanation": "ESCs regulate power delivery to motors for smooth and efficient flight."
    },
    {
        "question": "What is a challenge when flying drones in windy conditions?",
        "options": ["Easier navigation", "Stable flight", "More control", "Reduced stability"],
        "correct": "Reduced stability",
        "explanation": "Strong winds can destabilize drones, making navigation and control harder."
    },
    {
        "question": "Why are lightweight materials like carbon fiber used in drones?",
        "options": ["They are cheaper", "They are heavier", "They provide strength and reduce weight", "They are decorative"],
        "correct": "They provide strength and reduce weight",
        "explanation": "Carbon fiber offers strength without adding weight, improving drone performance."
    },
    {
        "question": "What helps drones transmit video signals?",
        "options": ["Solar panels", "Frequency bands like 5.8 GHz", "Fuel cells", "Mechanical gears"],
        "correct": "Frequency bands like 5.8 GHz",
        "explanation": "The 5.8 GHz frequency band is commonly used for transmitting live video from drones."
    }
]

# Quiz logic
if st.session_state.q_index < len(questions):
    q = questions[st.session_state.q_index]
    st.subheader(f"Question {st.session_state.q_index + 1}")
    st.write(q["question"])

    user_answer = st.radio("Choose an answer:", q["options"], key=f"radio_{st.session_state.q_index}")

    if st.button("Submit"):
        is_correct = user_answer == q["correct"]
        if is_correct:
            st.session_state.score += 1
            st.success("✔ Correct!")
        else:
            st.error("✘ Incorrect.")
        st.info(f"**Correct Answer:** {q['correct']}")
        st.write(f"**Explanation:** {q['explanation']}")

        st.session_state.answers.append({
            "question": q["question"],
            "selected": user_answer,
            "correct": q["correct"],
            "explanation": q["explanation"],
            "is_correct": is_correct
        })

        st.session_state.q_index += 1
        st.experimental_rerun()
else:
    st.header("Quiz Completed!")
    st.write(f"Your score: {st.session_state.score} out of {len(questions)}")

    for idx, ans in enumerate(st.session_state.answers):
        st.subheader(f"Question {idx + 1}")
        st.write(ans["question"])
        if ans["is_correct"]:
            st.success(f"Your Answer: {ans['selected']} (Correct)")
        else:
            st.error(f"Your Answer: {ans['selected']} (Incorrect)")
            st.info(f"Correct Answer: {ans['correct']}")
        st.write(f"Explanation: {ans['explanation']}")

    if st.button("Restart Quiz"):
        for key in ["q_index", "score", "answers"]:
            del st.session_state[key]
        st.experimental_rerun()
