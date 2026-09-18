import streamlit as st

st.set_page_config(
    page_title="My Profile",
    page_icon="👤",
    layout="centered"
)

# Custom styling
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #eef2ff, #fdf2f8);
    }

    .profile-card {
        background: white;
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
        margin-top: 20px;
    }

    .profile-title {
        color: #6366f1;
        text-align: center;
    }

    .profile-text {
        font-size: 18px;
        line-height: 1.8;
    }
</style>
""", unsafe_allow_html=True)

st.title("👤 My Profile")
st.write("Tell me a little about yourself!")

st.divider()

# Input form
name = st.text_input("👋 Name")
age = st.number_input("🎂 Age", min_value=1, max_value=120, step=1)
school = st.text_input("🏫 School")
subject = st.text_input("📚 Favorite subject")
hobby = st.text_input("🎨 Favorite hobby")

if st.button("✨ Create My Profile", use_container_width=True):
    if name and school and subject and hobby:
        st.markdown(f"""
        <div class="profile-card">
            <h2 class="profile-title">🌟 Hello, {name}!</h2>
            <div class="profile-text">
                👋 My name is <b>{name}</b>.<br>
                🎂 I am <b>{age}</b> years old.<br>
                🏫 I go to <b>{school}</b>.<br>
                📚 My favorite subject is <b>{subject}</b>.<br>
                🎨 I enjoy <b>{hobby}</b>.
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("Please fill in all the fields first! 😊")
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Neon Calculator",
    page_icon="🧮",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ---------------------------------------------------------
# PAGE BACKGROUND
# ---------------------------------------------------------

st.markdown("""
<style>

    /* Remove Streamlit default spacing */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 900px;
    }

    header {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    /* Background */
    .stApp {
        background:
            radial-gradient(circle at 20% 20%, #14213d 0%, transparent 35%),
            radial-gradient(circle at 80% 80%, #24103d 0%, transparent 35%),
            linear-gradient(135deg, #050509, #0a0a12 50%, #050509);
    }

</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# TITLE
# ---------------------------------------------------------

st.markdown("""
<div style="
    text-align:center;
    margin-bottom:18px;
">
    <div style="
        font-size:42px;
        font-weight:900;
        letter-spacing:3px;
        color:#ffffff;
        text-shadow:
            0 0 5px #00eaff,
            0 0 15px #00eaff,
            0 0 30px #0077ff;
    ">
        🧮 NEON CALCULATOR
    </div>

    <div style="
        color:#7eeeff;
        font-size:13px;
        letter-spacing:4px;
        margin-top:5px;
    ">
        FUTURISTIC • FAST • DIGITAL
    </div>
</div>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# CALCULATOR
# ---------------------------------------------------------

calculator_html = r"""
<!DOCTYPE html>
<html>

<head>

<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>

* {
    box-sizing: border-box;
    font-family: Arial, Helvetica, sans-serif;
    user-select: none;
}

body {
    margin: 0;
    padding: 10px;
    background: transparent;
}

.calculator {

    width: 100%;
    max-width: 620px;

    margin: auto;

    padding: 22px;

    border-radius: 30px;

    background:
        linear-gradient(
            145deg,
            rgba(25,25,40,0.98),
            rgba(5,5,12,0.98)
        );

    border: 1px solid rgba(0, 234, 255, 0.25);

    box-shadow:
        0 0 20px rgba(0,234,255,0.12),
        0 0 60px rgba(90,0,255,0.12),
        inset 0 0 30px rgba(255,255,255,0.02);

    position: relative;

    overflow: hidden;
}


/* Neon line around calculator */

.calculator::before {

    content: "";

    position: absolute;

    top: -2px;
    left: -2px;
    right: -2px;
    height: 3px;

    background:
        linear-gradient(
            90deg,
            #00eaff,
            #0077ff,
            #a000ff,
            #ff00aa,
            #00eaff
        );

    background-size: 300% 100%;

    animation: neonLine 4s linear infinite;

}

@keyframes neonLine {

    0% {
        background-position: 0%;
    }

    100% {
        background-position: 300%;
    }

}


/* Brand */

.brand {

    display: flex;

    align-items: center;

    gap: 12px;

    margin-bottom: 15px;

}

.logo {

    width: 48px;
    height: 48px;

    display: flex;

    align-items: center;
    justify-content: center;

    border-radius: 14px;

    background:
        linear-gradient(
            135deg,
            #00eaff,
            #0066ff
        );

    box-shadow:
        0 0 15px rgba(0,234,255,0.6);

    font-size: 26px;

}

.brand-title {

    color: white;

    font-size: 23px;

    font-weight: bold;

    letter-spacing: 2px;

}

.brand-subtitle {

    color: #5eeeff;

    font-size: 10px;

    letter-spacing: 3px;

    margin-top: 3px;

}


/* Display */

.display {

    background:
        linear-gradient(
            145deg,
            #05070a,
            #10151c
        );

    border-radius: 20px;

    border: 1px solid rgba(0,234,255,0.2);

    padding: 18px;

    margin-bottom: 18px;

    min-height: 120px;

    display: flex;

    flex-direction: column;

    justify-content: center;

    align-items: flex-end;

    box-shadow:
        inset 0 0 25px rgba(0,0,0,0.9),
        0 0 15px rgba(0,234,255,0.05);

    overflow: hidden;

}

.expression {

    width: 100%;

    text-align: right;

    color: #64717e;

    font-size: 17px;

    min-height: 25px;

    overflow-x: auto;

    white-space: nowrap;

}

.result {

    width: 100%;

    text-align: right;

    color: #ffffff;

    font-size: clamp(30px, 7vw, 50px);

    font-weight: 700;

    letter-spacing: 1px;

    overflow-x: auto;

    white-space: nowrap;

    text-shadow:
        0 0 7px #00eaff,
        0 0 18px rgba(0,234,255,0.5);

}


/* Buttons */

.buttons {

    display: grid;

    grid-template-columns: repeat(4, 1fr);

    gap: 11px;

}


button {

    height: 67px;

    border: none;

    border-radius: 16px;

    background:
        linear-gradient(
            145deg,
            #1c2029,
            #0d1016
        );

    color: #dcecff;

    font-size: 20px;

    font-weight: 600;

    cursor: pointer;

    border: 1px solid rgba(255,255,255,0.06);

    box-shadow:
        0 6px 12px rgba(0,0,0,0.45),
        inset 0 1px 0 rgba(255,255,255,0.04);

    transition:
        transform 0.08s,
        box-shadow 0.15s,
        background 0.15s;

    position: relative;

    overflow: hidden;

}


/* Ripple */

button::after {

    content: "";

    position: absolute;

    width: 10px;

    height: 10px;

    border-radius: 50%;

    background: rgba(255,255,255,0.5);

    transform: scale(0);

    opacity: 0;

    pointer-events: none;

}

button.clicked::after {

    animation: ripple 0.35s ease-out;

}

@keyframes ripple {

    0% {
        transform: scale(0);
        opacity: 0.7;
    }

    100% {
        transform: scale(15);
        opacity: 0;
    }

}


button:hover {

    background:
        linear-gradient(
            145deg,
            #26313d,
            #111822
        );

    box-shadow:
        0 0 12px rgba(0,234,255,0.25),
        0 6px 15px rgba(0,0,0,0.5);

    transform: translateY(-2px);

}

button:active {

    transform:
        translateY(2px)
        scale(0.96);

}


/* Number buttons */

.number {

    color: #ffffff;

}


/* Operators */

.operator {

    color: #00eaff;

    background:
        linear-gradient(
            145deg,
            #102b35,
            #08151b
        );

    border-color:
        rgba(0,234,255,0.25);

}

.operator:hover {

    box-shadow:
        0 0 18px rgba(0,234,255,0.4);

}


/* Equals */

.equals {

    color: white;

    background:
        linear-gradient(
            135deg,
            #0077ff,
            #7a00ff
        );

    box-shadow:
        0 0 15px rgba(0,119,255,0.4),
        0 0 30px rgba(122,0,255,0.25);

}

.equals:hover {

    background:
        linear-gradient(
            135deg,
            #00bfff,
            #9b00ff
        );

    box-shadow:
        0 0 25px rgba(0,234,255,0.6),
        0 0 40px rgba(150,0,255,0.3);

}


/* Clear */

.clear {

    color: #ff5277;

    background:
        linear-gradient(
            145deg,
            #32141e,
            #180b10
        );

    border-color:
        rgba(255,82,119,0.25);

}


/* Backspace */

.back {

    color: #ffb84d;

}


/* Percentage */

.percent {

    color: #bb8cff;

}


/* Zero */

.zero {

    grid-column: span 2;

}


/* History */

.history {

    margin-top: 18px;

    padding-top: 15px;

    border-top:
        1px solid rgba(255,255,255,0.07);

}

.history-title {

    color: #5eeeff;

    font-size: 11px;

    letter-spacing: 3px;

    margin-bottom: 8px;

}

.history-list {

    color: #687581;

    font-size: 13px;

    max-height: 75px;

    overflow-y: auto;

}

.history-item {

    padding: 4px 0;

}


/* Mobile */

@media (max-width: 500px) {

    .calculator {
        padding: 14px;
        border-radius: 22px;
    }

    button {
        height: 58px;
        font-size: 18px;
        border-radius: 13px;
    }

    .display {
        min-height: 105px;
    }

}

</style>

</head>


<body>

<div class="calculator">

    <div class="brand">

        <div class="logo">
            🧮
        </div>

        <div>

            <div class="brand-title">
                NEON CALCULATOR
            </div>

            <div class="brand-subtitle">
                DIGITAL COMPUTATION SYSTEM
            </div>

        </div>

    </div>


    <div class="display">

        <div class="expression" id="expression">
            Ready...
        </div>

        <div class="result" id="result">
            0
        </div>

    </div>


    <div class="buttons">

        <button class="clear" data-value="C">
            C
        </button>

        <button class="back" data-value="BACK">
            ⌫
        </button>

        <button class="percent" data-value="%">
            %
        </button>

        <button class="operator" data-value="/">
            ÷
        </button>


        <button class="number" data-value="7">
            7
        </button>

        <button class="number" data-value="8">
            8
        </button>

        <button class="number" data-value="9">
            9
        </button>

        <button class="operator" data-value="*">
            ×
        </button>


        <button class="number" data-value="4">
            4
        </button>

        <button class="number" data-value="5">
            5
        </button>

        <button class="number" data-value="6">
            6
        </button>

        <button class="operator" data-value="-">
            −
        </button>


        <button class="number" data-value="1">
            1
        </button>

        <button class="number" data-value="2">
            2
        </button>

        <button class="number" data-value="3">
            3
        </button>

        <button class="operator" data-value="+">
            +
        </button>


        <button class="number zero" data-value="0">
            0
        </button>

        <button class="number" data-value=".">
            .
        </button>

        <button class="equals" data-value="=">
            =
        </button>

    </div>


    <div class="history">

        <div class="history-title">
            CALCULATION HISTORY
        </div>

        <div class="history-list" id="history">
            No calculations yet
        </div>

    </div>

</div>


<script>

let current = "";
let expression = "";

const resultDisplay =
    document.getElementById("result");

const expressionDisplay =
    document.getElementById("expression");

const historyDisplay =
    document.getElementById("history");


/* --------------------------------------------------
   SOUND ENGINE
-------------------------------------------------- */

let audioContext = null;


function getAudioContext() {

    if (!audioContext) {

        audioContext =
            new (
                window.AudioContext ||
                window.webkitAudioContext
            )();

    }

    return audioContext;
}


function playClickSound(type = "normal") {

    try {

        const ctx = getAudioContext();

        const oscillator =
            ctx.createOscillator();

        const gain =
            ctx.createGain();

        oscillator.connect(gain);

        gain.connect(ctx.destination);


        if (type === "equals") {

            oscillator.type = "sine";

            oscillator.frequency.setValueAtTime(
                420,
                ctx.currentTime
            );

            oscillator.frequency.exponentialRampToValueAtTime(
                900,
                ctx.currentTime + 0.12
            );

        }

        else if (type === "operator") {

            oscillator.type = "triangle";

            oscillator.frequency.setValueAtTime(
                300,
                ctx.currentTime
            );

            oscillator.frequency.exponentialRampToValueAtTime(
                500,
                ctx.currentTime + 0.07
            );

        }

        else {

            oscillator.type = "sine";

            oscillator.frequency.setValueAtTime(
                650,
                ctx.currentTime
            );

            oscillator.frequency.exponentialRampToValueAtTime(
                350,
                ctx.currentTime + 0.045
            );

        }


        gain.gain.setValueAtTime(
            0.0001,
            ctx.currentTime
        );

        gain.gain.exponentialRampToValueAtTime(
            0.08,
            ctx.currentTime + 0.005
        );

        gain.gain.exponentialRampToValueAtTime(
            0.0001,
            ctx.currentTime + 0.09
        );


        oscillator.start();

        oscillator.stop(
            ctx.currentTime + 0.1
        );

    }

    catch(error) {

        console.log("Audio unavailable");

    }

}


/* --------------------------------------------------
   DISPLAY
-------------------------------------------------- */

function updateDisplay() {

    if (current === "") {

        resultDisplay.innerText = "0";

    }

    else {

        resultDisplay.innerText = current;

    }

    expressionDisplay.innerText =
        expression || "Ready...";

}


/* --------------------------------------------------
   HISTORY
-------------------------------------------------- */

let history = [];


function addHistory(text) {

    history.unshift(text);

    if (history.length > 5) {

        history.pop();

    }

    historyDisplay.innerHTML =
        history
        .map(item =>
            `<div class="history-item">${item}</div>`
        )
        .join("");

}


/* --------------------------------------------------
   CALCULATE
-------------------------------------------------- */

function calculate() {

    if (!current) return;

    try {

        let calculation = current;

        calculation =
            calculation.replace(/%/g, "/100");

        /*
           Only allow calculator characters.
           This prevents arbitrary JavaScript
           from being entered.
        */

        if (!/^[0-9+\-*/().\s]+$/.test(calculation)) {

            throw new Error("Invalid");

        }

        let answer =
            Function(
                '"use strict"; return (' +
                calculation +
                ')'
            )();


        if (!Number.isFinite(answer)) {

            throw new Error("Math error");

        }


        let oldExpression = current;

        let formatted =
            Number.isInteger(answer)
                ? answer.toString()
                : Number(answer.toFixed(10)).toString();


        expression =
            oldExpression + " =";

        current =
            formatted;


        addHistory(
            oldExpression
            .replace(/\*/g, "×")
            .replace(/\//g, "÷")
            + " = "
            + formatted
        );


        playClickSound("equals");

        updateDisplay();

    }

    catch(error) {

        resultDisplay.innerText =
            "ERROR";

        expressionDisplay.innerText =
            "Invalid calculation";

        playClickSound("operator");

        setTimeout(() => {

            current = "";

            expression = "";

            updateDisplay();

        }, 900);

    }

}


/* --------------------------------------------------
   BUTTON PRESS
-------------------------------------------------- */

function press(value, button) {

    button.classList.remove("clicked");

    void button.offsetWidth;

    button.classList.add("clicked");


    /* Clear */

    if (value === "C") {

        current = "";

        expression = "";

        playClickSound();

        updateDisplay();

        return;

    }


    /* Backspace */

    if (value === "BACK") {

        current =
            current.slice(0, -1);

        playClickSound();

        updateDisplay();

        return;

    }


    /* Equals */

    if (value === "=") {

        calculate();

        return;

    }


    /* Percentage */

    if (value === "%") {

        if (current !== "") {

            current += "%";

        }

        playClickSound("operator");

        updateDisplay();

        return;

    }


    /* Operators */

    if (
        value === "+" ||
        value === "-" ||
        value === "*" ||
        value === "/"
    ) {

        if (current === "") {

            return;

        }


        /* Prevent double operators */

        if (/[+\-*/]$/.test(current)) {

            current =
                current.slice(0, -1);

        }


        current += value;

        playClickSound("operator");

        updateDisplay();

        return;

    }


    /* Decimal */

    if (value === ".") {

        let parts =
            current.split(/[+\-*/]/);

        let lastNumber =
            parts[parts.length - 1];


        if (lastNumber.includes(".")) {

            return;

        }

    }


    /* Number */

    current += value;

    playClickSound();

    updateDisplay();

}


/* --------------------------------------------------
   BUTTON EVENTS
-------------------------------------------------- */

document
    .querySelectorAll("button")
    .forEach(button => {

        button.addEventListener(
            "click",
            () => {

                press(
                    button.dataset.value,
                    button
                );

            }
        );

    });


/* --------------------------------------------------
   KEYBOARD SUPPORT
-------------------------------------------------- */

document.addEventListener(
    "keydown",
    function(event) {

        let key =
            event.key;

        let button =
            document.querySelector(
                `button[data-value="${CSS.escape(key)}"]`
            );


        if (
            /^[0-9]$/.test(key) ||
            key === "." ||
            key === "+" ||
            key === "-" ||
            key === "*" ||
            key === "/" ||
            key === "%"
        ) {

            if (button) {

                press(key, button);

            }

            return;

        }


        if (
            key === "Enter" ||
            key === "="
        ) {

            let equals =
                document.querySelector(
                    'button[data-value="="]'
                );

            press("=", equals);

            return;

        }


        if (key === "Backspace") {

            let back =
                document.querySelector(
                    'button[data-value="BACK"]'
                );

            press("BACK", back);

            return;

        }


        if (key === "Escape") {

            let clear =
                document.querySelector(
                    'button[data-value="C"]'
                );

            press("C", clear);

        }

    }
);


/* Initial display */

updateDisplay();

</script>

</body>
</html>
"""


components.html(
    calculator_html,
    height=720,
    scrolling=False
)


# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------

st.markdown("""
<div style="
    text-align:center;
    margin-top:15px;
    color:#4d5965;
    font-size:11px;
    letter-spacing:2px;
">
    PRESS THE BUTTONS • USE YOUR KEYBOARD • ENJOY THE SOUND
</div>
""", unsafe_allow_html=True)

import streamlit as st

    # =========================================================
    # PAGE CONFIG
    # =========================================================

st.set_page_config(
        page_title="Grade Calculator",
        page_icon="📚",
        layout="centered"
    )


    # =========================================================
    # CUSTOM CSS
    # =========================================================

st.markdown("""
    <style>
    /* -------------------------------------------------------
    PAGE
    ------------------------------------------------------- */

    .stApp {
        background: #ffffff;
    }

    .block-container {
        max-width: 760px;
        padding-top: 45px;
        padding-bottom: 50px;
    }

    header {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }


    /* -------------------------------------------------------
    TOP DESCRIPTION
    ------------------------------------------------------- */

    .top-description {
        text-align: center;
        color: #64748b;
        font-size: 15px;
        margin-bottom: 45px;
    }


    /* -------------------------------------------------------
    SECTION HEADINGS
    ------------------------------------------------------- */

    .section-title {
        color: #172554;
        font-size: 27px;
        font-weight: 700;
        margin-top: 15px;
        margin-bottom: 20px;
    }


    /* -------------------------------------------------------
    INPUT LABELS
    ------------------------------------------------------- */

    .input-label {
        color: #334155;
        font-size: 14px;
        font-weight: 500;
        margin-bottom: 5px;
    }


    /* -------------------------------------------------------
    BUTTONS
    ------------------------------------------------------- */

    div.stButton > button {
        border-radius: 8px;
        min-height: 40px;
        font-weight: 500;
    }


    /* -------------------------------------------------------
    CALCULATE BUTTON
    ------------------------------------------------------- */

    div.stButton > button[kind="primary"] {
        background-color: #ff4b4b;
        border-color: #ff4b4b;
        color: white;
    }

    div.stButton > button[kind="primary"]:hover {
        background-color: #e63e3e;
        border-color: #e63e3e;
    }


    /* -------------------------------------------------------
    RESULTS
    ------------------------------------------------------- */

    .result-label {
        color: #475569;
        font-size: 14px;
        margin-bottom: 3px;
    }

    .result-number {
        color: #172554;
        font-size: 30px;
        font-weight: 500;
    }


    /* -------------------------------------------------------
    OVERALL GRADE
    ------------------------------------------------------- */

    .grade-card {
        border: 1px solid #d9dee7;
        border-radius: 18px;
        padding: 28px;
        text-align: center;
        margin-top: 20px;
        margin-bottom: 20px;
        background: #ffffff;
    }

    .grade-title {
        color: #172554;
        font-size: 16px;
        margin-bottom: 15px;
    }

    .grade-value {
        color: #1e293b;
        font-size: 50px;
        font-weight: 800;
    }

    .average-value {
        color: #2563eb;
        font-size: 15px;
        margin-top: 8px;
    }


    /* -------------------------------------------------------
    SUBJECT RESULT
    ------------------------------------------------------- */

    .subject-result-name {
        color: #172554;
        font-weight: 600;
        font-size: 15px;
    }

    .subject-result-mark {
        color: #475569;
        font-size: 15px;
    }

    .subject-result-grade {
        font-weight: 700;
        font-size: 15px;
    }


    /* -------------------------------------------------------
    FOOTER
    ------------------------------------------------------- */

    .footer {
        text-align: center;
        color: #94a3b8;
        font-size: 12px;
        margin-top: 40px;
    }
    </style>
    """, unsafe_allow_html=True)


    # =========================================================
    # SESSION STATE
    # =========================================================

if "subjects" not in st.session_state:
        st.session_state.subjects = [
            {
                "name": "Mathematics",
                "marks": 0.0
            },
            {
                "name": "Science",
                "marks": 0.0
            },
            {
                "name": "English",
                "marks": 0.0
            }
        ]

if "show_results" not in st.session_state:
       st.session_state.show_results = False


    # =========================================================
    # GRADE CALCULATION FUNCTION
    # =========================================================

def get_grade(mark):

        if mark >= 90:
            return "A+", 4.0

        elif mark >= 85:
            return "A", 4.0

        elif mark >= 80:
            return "A-", 3.7

        elif mark >= 75:
            return "B+", 3.3

        elif mark >= 70:
            return "B", 3.0

        elif mark >= 65:
            return "B-", 2.7

        elif mark >= 60:
            return "C+", 2.3

        elif mark >= 55:
            return "C", 2.0

        elif mark >= 50:
            return "C-", 1.7

        elif mark >= 45:
            return "D", 1.0

        else:
            return "F", 0.0


    # =========================================================
    # PAGE TITLE
    # =========================================================

st.markdown(
        '<div class="top-description">'
        'Calculate your marks, percentage, grade and GPA'
        '</div>',
        unsafe_allow_html=True
    )


    # =========================================================
    # SUBJECTS TITLE
    # =========================================================

st.markdown(
        '<div class="section-title">📚 Your Subjects 🔗</div>',
        unsafe_allow_html=True
    )


    # =========================================================
    # SUBJECT INPUTS
    # =========================================================

for i in range(len(st.session_state.subjects)):

        subject = st.session_state.subjects[i]

        # Three columns:
        # Subject | Marks | Delete
        col1, col2, col3 = st.columns(
            [5, 2, 0.7]
        )

        # -----------------------------------------------------
        # SUBJECT NAME
        # -----------------------------------------------------

        with col1:

            st.markdown(
                '<div class="input-label">Subject</div>',
                unsafe_allow_html=True
            )

            name = st.text_input(
                "Subject",
                value=subject["name"],
                key=f"name_{i}",
                label_visibility="collapsed"
            )

            st.session_state.subjects[i]["name"] = name


        # -----------------------------------------------------
        # MARKS
        # -----------------------------------------------------

        with col2:

            st.markdown(
                '<div class="input-label">Marks</div>',
                unsafe_allow_html=True
            )

            marks = st.number_input(
                "Marks",
                min_value=0.0,
                max_value=100.0,
                value=float(subject["marks"]),
                step=1.0,
                key=f"marks_{i}",
                label_visibility="collapsed"
            )

            st.session_state.subjects[i]["marks"] = marks


        # -----------------------------------------------------
        # DELETE BUTTON
        # -----------------------------------------------------

        with col3:

            # Keep at least one subject
            if len(st.session_state.subjects) > 1:

                st.markdown("<br>", unsafe_allow_html=True)

                if st.button(
                    "🗑️",
                    key=f"delete_{i}",
                    help="Delete this subject"
                ):

                    st.session_state.subjects.pop(i)

                    st.session_state.show_results = False

                    st.rerun()


    # =========================================================
    # ADD / RESET
    # =========================================================

st.markdown("<br>", unsafe_allow_html=True)

button_col1, button_col2 = st.columns(2)


    # ---------------------------------------------------------
    # ADD SUBJECT
    # ---------------------------------------------------------

with button_col1:

        if st.button(
            "➕ Add Subject",
            use_container_width=True
        ):

            new_number = len(st.session_state.subjects) + 1

            st.session_state.subjects.append(
                {
                    "name": f"Subject {new_number}",
                    "marks": 0.0
                }
            )

            st.session_state.show_results = False

            st.rerun()


    # ---------------------------------------------------------
    # RESET
    # ---------------------------------------------------------

with button_col2:

        if st.button(
            "🗑️ Reset",
            use_container_width=True
        ):

            st.session_state.subjects = [
                {
                    "name": "Mathematics",
                    "marks": 0.0
                },
                {
                    "name": "Science",
                    "marks": 0.0
                },
                {
                    "name": "English",
                    "marks": 0.0
                }
            ]

            st.session_state.show_results = False

            st.rerun()


    # =========================================================
    # CALCULATE BUTTON
    # =========================================================

st.markdown("<br>", unsafe_allow_html=True)

calculate = st.button(
        "🎯 Calculate My Grade",
        use_container_width=True,
        type="primary"
    )

if calculate:
        st.session_state.show_results = True


    # =========================================================
    # RESULTS
    # =========================================================

if st.session_state.show_results:

        # -----------------------------------------------------
        # CHECK SUBJECT NAMES
        # -----------------------------------------------------

        empty_subject = False

        for subject in st.session_state.subjects:

            if not subject["name"].strip():
                empty_subject = True

        if empty_subject:

            st.warning(
                "Please enter a name for every subject."
            )

        else:

            # -------------------------------------------------
            # TOTAL MARKS
            # -------------------------------------------------

            total_marks = sum(
                subject["marks"]
                for subject in st.session_state.subjects
            )

            number_of_subjects = len(
                st.session_state.subjects
            )

            maximum_marks = (
                number_of_subjects * 100
            )


            # -------------------------------------------------
            # PERCENTAGE
            # -------------------------------------------------

            if maximum_marks > 0:

                percentage = (
                    total_marks /
                    maximum_marks
                ) * 100

            else:

                percentage = 0


            # -------------------------------------------------
            # OVERALL GRADE
            # -------------------------------------------------

            overall_grade, overall_gpa = get_grade(
                percentage
            )


            # =================================================
            # RESULTS TITLE
            # =================================================

            st.markdown(
                '<div class="section-title">'
                '📊 Your Results'
                '</div>',
                unsafe_allow_html=True
            )


            # =================================================
            # SUMMARY
            # =================================================

            col1, col2, col3 = st.columns(3)


            # -------------------------------------------------
            # TOTAL MARKS
            # -------------------------------------------------

            with col1:

                st.markdown(
                    '<div class="result-label">'
                    'Total Marks'
                    '</div>',
                    unsafe_allow_html=True
                )

                st.markdown(
                    f'<div class="result-number">'
                    f'{total_marks:g}/{maximum_marks}'
                    f'</div>',
                    unsafe_allow_html=True
                )


            # -------------------------------------------------
            # PERCENTAGE
            # -------------------------------------------------

            with col2:

                st.markdown(
                    '<div class="result-label">'
                    'Percentage'
                    '</div>',
                    unsafe_allow_html=True
                )

                st.markdown(
                    f'<div class="result-number">'
                    f'{percentage:.1f}%'
                    f'</div>',
                    unsafe_allow_html=True
                )


            # -------------------------------------------------
            # GPA
            # -------------------------------------------------

            with col3:

                st.markdown(
                    '<div class="result-label">'
                    'GPA'
                    '</div>',
                    unsafe_allow_html=True
                )

                st.markdown(
                    f'<div class="result-number">'
                    f'{overall_gpa:.2f}/4.0'
                    f'</div>',
                    unsafe_allow_html=True
                )


            # =================================================
            # OVERALL GRADE
            # =================================================

            st.markdown(
                f"""
    <div class="grade-card">
        <div class="grade-title">
            Overall Grade
        </div>
        <div class="grade-value">
            {overall_grade}
        </div>
        <div class="average-value">
            Average: {percentage:.1f}%
        </div>
    </div>
    """,
                unsafe_allow_html=True
            )


            # =================================================
            # PERFORMANCE
            # =================================================

            st.markdown(
                "### 📈 Overall Performance"
            )

            st.progress(
                int(percentage)
            )


            # =================================================
            # SUBJECT RESULTS
            # =================================================

            st.markdown(
                '<div class="section-title">'
                '📚 Subject Results'
                '</div>',
                unsafe_allow_html=True
            )


            # -------------------------------------------------
            # EACH SUBJECT
            # -------------------------------------------------

            for subject in st.session_state.subjects:

                name = subject["name"]
                marks = subject["marks"]

                grade, gpa = get_grade(marks)


                # Use Streamlit columns.
                # This prevents the raw HTML problem.
                result_col1, result_col2, result_col3 = st.columns(
                    [4, 2, 1]
                )


                # ------------------------------------------------
                # SUBJECT NAME
                # ------------------------------------------------

                with result_col1:

                    st.markdown(
                        f'<div class="subject-result-name">'
                        f'{name}'
                        f'</div>',
                        unsafe_allow_html=True
                    )


                # ------------------------------------------------
                # SUBJECT MARK
                # ------------------------------------------------

                with result_col2:

                    st.markdown(
                        f'<div class="subject-result-mark">'
                        f'{marks:g}/100'
                        f'</div>',
                        unsafe_allow_html=True
                    )


                # ------------------------------------------------
                # SUBJECT GRADE
                # ------------------------------------------------

                with result_col3:

                    # Grade colors
                    if grade in ["A+", "A", "A-"]:
                        grade_color = "#16a34a"

                    elif grade in ["B+", "B", "B-"]:
                        grade_color = "#2563eb"

                    elif grade in ["C+", "C", "C-"]:
                        grade_color = "#ca8a04"

                    elif grade == "D":
                        grade_color = "#ea580c"

                    else:
                        grade_color = "#dc2626"


                    st.markdown(
                        f'<div class="subject-result-grade" '
                        f'style="color:{grade_color};">'
                        f'{grade}'
                        f'</div>',
                        unsafe_allow_html=True
                    )


                # ------------------------------------------------
                # LINE
                # ------------------------------------------------

                st.markdown(
                    """
    <hr style="
        border:0;
        border-top:1px solid #e5e7eb;
        margin:12px 0;
    ">
    """,
                    unsafe_allow_html=True
                )


            # =================================================
            # GPA DETAILS
            # =================================================

            st.markdown(
                "### 🎓 GPA Details"
            )

            st.info(
                f"Your GPA is {overall_gpa:.2f}/4.0 "
                f"with an overall grade of {overall_grade}."
            )


    # =========================================================
    # FOOTER
    # =========================================================

st.markdown(
        """
        <div class="footer">
            📚 Grade Calculator • Calculate your academic performance
        </div>
        """,
        unsafe_allow_html=True
    )
import streamlit as st


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Quiz",
    page_icon="📝",
    layout="centered"
)


# ============================================================
# CSS
# ============================================================

st.markdown("""
<style>

.stApp {
    background: #0d1016;
}

header {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

.block-container {
    max-width: 535px;
    padding-top: 24px;
    padding-bottom: 40px;
}

/* Main title */

.quiz-title {
    color: #f5f5f5;
    font-size: 18px;
    font-weight: 700;
    margin-bottom: 16px;
}

/* Labels */

.field-label {
    color: #f5f5f5;
    font-size: 10px;
    font-weight: 600;
    margin-bottom: 5px;
}

.choice-label {
    color: #f5f5f5;
    font-size: 10px;
    font-weight: 600;
    margin-bottom: 5px;
}

.blue {
    color: #168de2;
}

.yellow {
    color: #fff000;
}

.green {
    color: #13c926;
}

.red {
    color: #ff1833;
}


/* Text inputs */

div[data-baseweb="input"] {
    background-color: #272933 !important;
    border: none !important;
    border-radius: 6px !important;
}

div[data-baseweb="input"] input {
    background-color: #272933 !important;
    color: #b7b9c3 !important;
    font-size: 10px !important;
}


/* Text areas */

div[data-baseweb="textarea"] {
    background-color: #272933 !important;
    border-radius: 6px !important;
}

div[data-baseweb="textarea"] textarea {
    background-color: #272933 !important;
    color: #b7b9c3 !important;
    font-size: 10px !important;
}


/* Buttons */

.stButton > button {
    width: 100%;
    height: 38px;
    background-color: #ff4d52 !important;
    color: white !important;
    border: none !important;
    border-radius: 6px !important;
    font-size: 10px !important;
    font-weight: 500;
}

.stButton > button:hover {
    background-color: #e83f44 !important;
    color: white !important;
}


/* Secondary buttons */

.secondary-button .stButton > button {
    background-color: #272933 !important;
}


/* Divider */

hr {
    border-color: #3a3d46 !important;
}


/* Radio */

div[role="radiogroup"] label {
    color: #f5f5f5 !important;
    font-size: 10px !important;
}


/* Selectbox */

div[data-baseweb="select"] {
    background-color: #272933 !important;
}

div[data-baseweb="select"] * {
    color: #f5f5f5 !important;
}


/* Info */

div[data-testid="stAlert"] {
    background-color: #272933;
}


/* Score */

.score {
    text-align: center;
    color: #ff4d52;
    font-size: 28px;
    font-weight: 700;
}

.result-text {
    text-align: center;
    color: #b7b9c3;
    font-size: 11px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# DEFAULT QUESTIONS
# ============================================================

DEFAULT_QUESTIONS = [
    {
        "question": "What is the capital of France?",
        "choices": [
            "Paris",
            "London",
            "Berlin",
            "Madrid"
        ],
        "correct": 0
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "choices": [
            "Earth",
            "Mars",
            "Jupiter",
            "Venus"
        ],
        "correct": 1
    },
    {
        "question": "What is 5 + 7?",
        "choices": [
            "10",
            "11",
            "12",
            "13"
        ],
        "correct": 2
    }
]


# ============================================================
# SESSION STATE
# ============================================================

if "questions" not in st.session_state:
    st.session_state.questions = [
        q.copy() for q in DEFAULT_QUESTIONS
    ]

if "page" not in st.session_state:
    st.session_state.page = "editor"

if "edit_index" not in st.session_state:
    st.session_state.edit_index = 0

if "quiz_index" not in st.session_state:
    st.session_state.quiz_index = 0

if "score" not in st.session_state:
    st.session_state.score = 0


# ============================================================
# HELPER
# ============================================================

def reset_editor_keys():
    """
    Forces Streamlit to load the selected question's values
    into the editor widgets.
    """
    st.session_state.edit_version = (
        st.session_state.get("edit_version", 0) + 1
    )


# ============================================================
# EDITOR PAGE
# ============================================================

def editor_page():

    questions = st.session_state.questions

    # Make sure index is valid
    if len(questions) == 0:
        st.session_state.edit_index = 0
    else:
        if st.session_state.edit_index >= len(questions):
            st.session_state.edit_index = len(questions) - 1

    # --------------------------------------------------------
    # HEADER
    # --------------------------------------------------------

    current_number = st.session_state.edit_index + 1

    st.markdown(
        f"""
        <div class="quiz-title">
            📝 Question {current_number}
        </div>
        """,
        unsafe_allow_html=True
    )

    # --------------------------------------------------------
    # QUESTION SELECTOR
    # --------------------------------------------------------

    if len(questions) > 1:

        selected = st.selectbox(
            "Edit question",
            range(len(questions)),
            index=st.session_state.edit_index,
            format_func=lambda x: f"Question {x + 1}",
            key="question_selector"
        )

        if selected != st.session_state.edit_index:

            st.session_state.edit_index = selected

            # Remove old widget values
            for key in [
                "question_input",
                "choice_a_input",
                "choice_b_input",
                "choice_c_input",
                "choice_d_input",
                "correct_input"
            ]:
                if key in st.session_state:
                    del st.session_state[key]

            st.rerun()

    # Current question
    index = st.session_state.edit_index
    q = questions[index]

    # --------------------------------------------------------
    # QUESTION
    # --------------------------------------------------------

    st.markdown(
        '<div class="field-label">Question</div>',
        unsafe_allow_html=True
    )

    question_text = st.text_input(
        "question",
        value=q["question"],
        key=f"question_input_{index}",
        label_visibility="collapsed"
    )

    st.write("")

    # --------------------------------------------------------
    # CHOICES
    # --------------------------------------------------------

    col1, col2 = st.columns(2, gap="small")

    # Choice A
    with col1:

        st.markdown(
            """
            <div class="choice-label">
                <span class="blue">●</span> Choice A
            </div>
            """,
            unsafe_allow_html=True
        )

        choice_a = st.text_input(
            "choice_a",
            value=q["choices"][0],
            key=f"choice_a_input_{index}",
            label_visibility="collapsed"
        )

    # Choice B
    with col2:

        st.markdown(
            """
            <div class="choice-label">
                <span class="yellow">●</span> Choice B
            </div>
            """,
            unsafe_allow_html=True
        )

        choice_b = st.text_input(
            "choice_b",
            value=q["choices"][1],
            key=f"choice_b_input_{index}",
            label_visibility="collapsed"
        )

    st.write("")

    # Choice C
    with col1:

        st.markdown(
            """
            <div class="choice-label">
                <span class="green">●</span> Choice C
            </div>
            """,
            unsafe_allow_html=True
        )

        choice_c = st.text_input(
            "choice_c",
            value=q["choices"][2],
            key=f"choice_c_input_{index}",
            label_visibility="collapsed"
        )

    # Choice D
    with col2:

        st.markdown(
            """
            <div class="choice-label">
                <span class="red">●</span> Choice D
            </div>
            """,
            unsafe_allow_html=True
        )

        choice_d = st.text_input(
            "choice_d",
            value=q["choices"][3],
            key=f"choice_d_input_{index}",
            label_visibility="collapsed"
        )

    st.write("")

    # --------------------------------------------------------
    # CORRECT ANSWER
    # --------------------------------------------------------

    st.markdown(
        '<div class="field-label">Correct answer</div>',
        unsafe_allow_html=True
    )

    correct = st.radio(
        "correct",
        ["A", "B", "C", "D"],
        index=q["correct"],
        horizontal=True,
        key=f"correct_input_{index}",
        label_visibility="collapsed"
    )

    # --------------------------------------------------------
    # SAVE VALUES
    # --------------------------------------------------------

    q["question"] = question_text

    q["choices"] = [
        choice_a,
        choice_b,
        choice_c,
        choice_d
    ]

    q["correct"] = ["A", "B", "C", "D"].index(correct)

    # --------------------------------------------------------
    # DIVIDER
    # --------------------------------------------------------

    st.write("")
    st.divider()
    st.write("")

    # --------------------------------------------------------
    # NAVIGATION BUTTONS
    # --------------------------------------------------------

    nav1, nav2 = st.columns(2, gap="small")

    with nav1:

        if st.button("← Previous"):

            if index > 0:

                st.session_state.edit_index -= 1

                for key in list(st.session_state.keys()):
                    if key.startswith(
                        (
                            "question_input_",
                            "choice_a_input_",
                            "choice_b_input_",
                            "choice_c_input_",
                            "choice_d_input_",
                            "correct_input_"
                        )
                    ):
                        del st.session_state[key]

                st.rerun()

    with nav2:

        if st.button("Next →"):

            if index < len(questions) - 1:

                st.session_state.edit_index += 1

                for key in list(st.session_state.keys()):
                    if key.startswith(
                        (
                            "question_input_",
                            "choice_a_input_",
                            "choice_b_input_",
                            "choice_c_input_",
                            "choice_d_input_",
                            "correct_input_"
                        )
                    ):
                        del st.session_state[key]

                st.rerun()

    st.write("")

    # --------------------------------------------------------
    # ADD / DELETE
    # --------------------------------------------------------

    col1, col2 = st.columns(2, gap="small")

    with col1:

        if st.button("➕ Add Question"):

            new_question = {
                "question": "Enter your question here",
                "choices": [
                    "Enter choice A",
                    "Enter choice B",
                    "Enter choice C",
                    "Enter choice D"
                ],
                "correct": 0
            }

            questions.append(new_question)

            st.session_state.edit_index = len(questions) - 1

            # Clear editor widgets
            for key in list(st.session_state.keys()):
                if key.startswith(
                    (
                        "question_input_",
                        "choice_a_input_",
                        "choice_b_input_",
                        "choice_c_input_",
                        "choice_d_input_",
                        "correct_input_"
                    )
                ):
                    del st.session_state[key]

            st.rerun()

    with col2:

        if st.button("🗑️ Delete Question"):

            if len(questions) > 1:

                questions.pop(index)

                if st.session_state.edit_index >= len(questions):
                    st.session_state.edit_index = len(questions) - 1

                for key in list(st.session_state.keys()):
                    if key.startswith(
                        (
                            "question_input_",
                            "choice_a_input_",
                            "choice_b_input_",
                            "choice_c_input_",
                            "choice_d_input_",
                            "correct_input_"
                        )
                    ):
                        del st.session_state[key]

                st.rerun()

            else:

                st.warning(
                    "You need at least one question."
                )

    st.write("")

    # --------------------------------------------------------
    # QUESTION COUNT
    # --------------------------------------------------------

    st.markdown(
        f"""
        <div style="
            color:#777b86;
            text-align:center;
            font-size:9px;
            margin-bottom:10px;
        ">
            {len(questions)} question(s) created
        </div>
        """,
        unsafe_allow_html=True
    )

    # --------------------------------------------------------
    # START QUIZ
    # --------------------------------------------------------

    if st.button("🚀 Start Quiz"):

        valid = True

        for q in questions:

            if not q["question"].strip():
                valid = False

            for choice in q["choices"]:

                if not choice.strip():
                    valid = False

        if not valid:

            st.error(
                "Please fill in every question and choice."
            )

        else:

            st.session_state.quiz_index = 0
            st.session_state.score = 0
            st.session_state.page = "quiz"

            st.rerun()


# ============================================================
# QUIZ PAGE
# ============================================================

def quiz_page():

    questions = st.session_state.questions

    index = st.session_state.quiz_index

    q = questions[index]

    # --------------------------------------------------------
    # HEADER
    # --------------------------------------------------------

    st.markdown(
        f"""
        <div class="quiz-title">
            📝 Question {index + 1} of {len(questions)}
        </div>
        """,
        unsafe_allow_html=True
    )

    # --------------------------------------------------------
    # QUESTION BOX
    # --------------------------------------------------------

    st.markdown(
        f"""
        <div style="
            background:#272933;
            border-radius:6px;
            padding:14px;
            color:#b7b9c3;
            font-size:11px;
            margin-bottom:20px;
        ">
            {q["question"]}
        </div>
        """,
        unsafe_allow_html=True
    )

    # --------------------------------------------------------
    # ANSWERS
    # --------------------------------------------------------

    answer = st.radio(
        "Choose your answer",
        q["choices"],
        key=f"quiz_answer_{index}"
    )

    st.write("")
    st.divider()
    st.write("")

    # --------------------------------------------------------
    # NEXT / FINISH
    # --------------------------------------------------------

    if index == len(questions) - 1:
        button_text = "Finish Quiz"
    else:
        button_text = "Next Question"

    if st.button(button_text):

        selected = q["choices"].index(answer)

        if selected == q["correct"]:
            st.session_state.score += 1

        if index < len(questions) - 1:

            st.session_state.quiz_index += 1

            st.rerun()

        else:

            st.session_state.page = "result"

            st.rerun()


# ============================================================
# RESULT PAGE
# ============================================================

def result_page():

    score = st.session_state.score
    total = len(st.session_state.questions)

    percentage = round(
        (score / total) * 100
    )

    st.markdown(
        """
        <div class="quiz-title">
            🎉 Quiz Complete!
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    st.markdown(
        f"""
        <div class="score">
            Your Score: {score} / {total}
        </div>

        <div class="result-text">
            You scored {percentage}%
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")
    st.write("")
    st.divider()
    st.write("")

    # --------------------------------------------------------
    # TRY AGAIN
    # --------------------------------------------------------

    if st.button("🔄 Try Again"):

        st.session_state.quiz_index = 0
        st.session_state.score = 0
        st.session_state.page = "quiz"

        st.rerun()

    st.write("")

    # --------------------------------------------------------
    # EDIT QUESTIONS
    # --------------------------------------------------------

    if st.button("✏️ Edit Questions"):

        st.session_state.edit_index = 0
        st.session_state.page = "editor"

        st.rerun()


# ============================================================
# RUN PAGE
# ============================================================

if st.session_state.page == "editor":

    editor_page()

elif st.session_state.page == "quiz":

    quiz_page()

elif st.session_state.page == "result":

    result_page()
