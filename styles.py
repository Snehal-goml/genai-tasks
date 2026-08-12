def get_css():
    return """
    <style>

    /* Force dark background everywhere */
    html, body {
        background: #05070f !important;
        margin: 0 !important;
        padding: 0 !important;
    }

    /* Make ALL text bright white and readable */
    * {
        color: #ffffff !important;
    }

    /* Remove Streamlit default header and footer white bars */
    header[data-testid="stHeader"] {
        background: #05070f !important;
        border-bottom: none !important;
    }
    
    footer[data-testid="stFooter"],
    [data-testid="stFooter"] {
        background: #05070f !important;
        border-top: none !important;
    }
    
    /* Force full viewport dark */
    #root,
    [data-testid="stAppViewContainer"],
    [data-testid="appViewContainer"] {
        background: transparent !important;
        min-height: 100vh !important;
    }
    
    /* Starry night background - REAL-TIME ANIMATED MOVING + TWINKLING STARS */
    .stApp {
        background-color: #05070f !important;
        background-image:
            radial-gradient(2px 2px at 20px 30px, #fff, rgba(255,255,255,0)),
            radial-gradient(2px 2px at 40px 70px, #fff, rgba(255,255,255,0)),
            radial-gradient(1px 1px at 90px 40px, #fff, rgba(255,255,255,0)),
            radial-gradient(1px 1px at 160px 120px, #fff, rgba(255,255,255,0)),
            radial-gradient(2px 2px at 200px 10px, #fff, rgba(255,255,255,0)),
            radial-gradient(1px 1px at 130px 90px, #fff, rgba(255,255,255,0)),
            radial-gradient(2px 2px at 60px 140px, #fff, rgba(255,255,255,0)),
            radial-gradient(1px 1px at 180px 70px, #fff, rgba(255,255,255,0)),
            radial-gradient(1px 1px at 10px 100px, #fff, rgba(255,255,255,0)),
            radial-gradient(2px 2px at 120px 150px, #fff, rgba(255,255,255,0)),
            radial-gradient(1px 1px at 220px 130px, #fff, rgba(255,255,255,0)),
            radial-gradient(1px 1px at 90px 180px, #fff, rgba(255,255,255,0));
        background-repeat: repeat;
        background-size: 240px 200px;
        color: #ffffff;
        min-height: 100vh;
        animation: starDrift 90s linear infinite;
    }

    /* Twinkling star layer on top */
    .stApp::before {
        content: "";
        position: fixed;
        inset: 0;
        z-index: 0;
        pointer-events: none;
        background-image:
            radial-gradient(1.5px 1.5px at 50px 60px, #ffffff, rgba(255,255,255,0)),
            radial-gradient(1px 1px at 150px 20px, #ffffff, rgba(255,255,255,0)),
            radial-gradient(2px 2px at 90px 110px, #ffffff, rgba(255,255,255,0)),
            radial-gradient(1px 1px at 210px 90px, #ffffff, rgba(255,255,255,0)),
            radial-gradient(1px 1px at 30px 160px, #ffffff, rgba(255,255,255,0)),
            radial-gradient(2px 2px at 190px 160px, #ffffff, rgba(255,255,255,0));
        background-repeat: repeat;
        background-size: 240px 200px;
        animation: twinkle 4s ease-in-out infinite alternate;
    }

    @keyframes starDrift {
        0%   { background-position: 0 0; }
        100% { background-position: 240px 200px; }
    }

    @keyframes twinkle {
        0%   { opacity: 0.2; }
        50%  { opacity: 1; }
        100% { opacity: 0.3; }
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background: rgba(14, 17, 28, 0.95);
        border-right: 1px solid rgba(255,255,255,0.08);
    }

    /* Chat message cards */
    [data-testid="stChatMessage"] {
        background: rgba(255, 255, 255, 0.04);
        border: 1px solid rgba(255,255,255,0.06);
        border-radius: 18px;
        padding: 10px;
        backdrop-filter: blur(8px);
    }

    /* Buttons */
    .stButton button {
        border-radius: 12px;
        border: 1px solid rgba(255,255,255,0.12);
        background: rgba(255,255,255,0.06);
        transition: all 0.3s ease;
        color: white !important;
    }

    .stButton button:hover {
        border: 1px solid rgba(255,255,255,0.25);
        transform: scale(1.02);
        background: rgba(255,255,255,0.12);
        box-shadow: 0 0 20px rgba(100, 150, 255, 0.3);
    }

    /* Text input styling - Top text box (chat title) */
    input[type="text"] {
        background: linear-gradient(135deg, rgba(100, 50, 255, 0.1), rgba(0, 200, 255, 0.08)) !important;
        border: 1.5px solid rgba(100, 150, 255, 0.3) !important;
        border-radius: 12px !important;
        color: white !important;
        padding: 12px 16px !important;
        font-size: 1rem !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 0 20px rgba(100, 100, 255, 0.1) inset !important;
    }

    input[type="text"]:focus {
        background: linear-gradient(135deg, rgba(100, 50, 255, 0.2), rgba(0, 200, 255, 0.15)) !important;
        border: 1.5px solid rgba(100, 200, 255, 0.6) !important;
        box-shadow: 0 0 30px rgba(100, 150, 255, 0.3), inset 0 0 20px rgba(100, 100, 255, 0.15) !important;
    }

    /* Chat input - Bottom text box */
    [data-testid="stChatInput"] {
        background: rgba(14, 17, 28, 0.95) !important;
        border-top: 1px solid rgba(255,255,255,0.1) !important;
    }
    
    [data-testid="stChatInput"] input {
        background: linear-gradient(135deg, rgba(0, 200, 255, 0.08), rgba(255, 50, 150, 0.06)) !important;
        border: 1.5px solid rgba(0, 200, 255, 0.4) !important;
        border-radius: 15px !important;
        color: white !important;
        padding: 14px 18px !important;
        font-size: 1rem !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 0 25px rgba(0, 150, 255, 0.15) inset !important;
    }

    [data-testid="stChatInput"] input:focus {
        background: linear-gradient(135deg, rgba(0, 200, 255, 0.15), rgba(255, 50, 150, 0.1)) !important;
        border: 1.5px solid rgba(0, 200, 255, 0.8) !important;
        box-shadow: 0 0 40px rgba(0, 150, 255, 0.4), inset 0 0 25px rgba(0, 150, 255, 0.2) !important;
    }

    /* Text area styling for edit prompts */
    textarea {
        background: linear-gradient(135deg, rgba(100, 50, 255, 0.08), rgba(255, 50, 150, 0.06)) !important;
        border: 1.5px solid rgba(150, 100, 255, 0.3) !important;
        border-radius: 12px !important;
        color: white !important;
        padding: 12px 16px !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 0 20px rgba(150, 100, 255, 0.1) inset !important;
    }

    textarea:focus {
        background: linear-gradient(135deg, rgba(100, 50, 255, 0.15), rgba(255, 50, 150, 0.1)) !important;
        border: 1.5px solid rgba(150, 150, 255, 0.6) !important;
        box-shadow: 0 0 30px rgba(150, 100, 255, 0.3), inset 0 0 20px rgba(150, 100, 255, 0.15) !important;
    }

    /* Input placeholder styling */
    input::placeholder,
    textarea::placeholder {
        color: rgba(255, 255, 255, 0.4) !important;
    }
    
    /* Remove white gaps - fix top and bottom padding */
    .main .block-container {
        padding-top: 0.5rem !important;
        padding-bottom: 0 !important;
        padding-left: 2rem !important;
        padding-right: 2rem !important;
        background: transparent !important;
        max-width: 100% !important;
    }
    
    /* Ensure all sections have dark backgrounds */
    [data-testid="stVerticalBlock"] {
        background: transparent !important;
    }

    /* --- Comprehensive base-background coverage --- */
    .main,
    section.main,
    [data-testid="stMain"],
    [data-testid="main"] {
        background: #0a0e1a !important;
    }

    /* Bottom chat-input container (pin to bottom, no white) */
    [data-testid="stBottom"],
    [data-testid="stBottomBlockContainer"] {
        background: #0a0e1a !important;
        border-top: 1px solid rgba(255,255,255,0.08) !important;
    }

    /* Any remaining inner wrapper containers */
    [data-testid="stVerticalBlockBorderWrapper"],
    [data-testid="stHorizontalBlock"] {
        background: transparent !important;
    }

    /* Chat message avatars - keep on theme */
    [data-testid="stChatMessageAvatarAssistant"],
    [data-testid="stChatMessageAvatarUser"] {
        background: rgba(100, 150, 255, 0.15) !important;
    }

    /* Expand buttons / other widgets */
    [data-testid="stExpander"] {
        background: rgba(255,255,255,0.04) !important;
    }

    </style>
    """