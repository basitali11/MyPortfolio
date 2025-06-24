import streamlit as st

def show(): 
    st.markdown('<h2 class="section-title">Featured Projects</h2>', unsafe_allow_html=True)

    projects = [
        {
            "title": "🎯 Xana AI Protocol",
            "subtitle": "Personality-Driven Conversational AI",
            "description": "Advanced conversational AI using state-of-the-art LLMs (Gemma, Mixtral, Llama) with dynamic personality adaptation, RAG integration, and real-time processing optimization.",
            "tech": ["LLMs", "LangChain", "RAG", "Groq", "FastAPI", "SQLite"]
        },
        {
            "title": "🎙️ Voice AI Assistant",
            "subtitle": "Voice-Enabled Chatbot",
            "description": "Seamless voice interactions using OpenAI GPT-4, LangChain framework, ElevenLabs TTS, and Whisper STT for natural conversation flow.",
            "tech": ["OpenAI GPT-4", "LangChain", "ElevenLabs", "Whisper", "Voice Processing"]
        },
        {
            "title": "👁️ UGC Facial Analysis",
            "subtitle": "AI-Powered Feature Detection",
            "description": "Advanced facial feature detection using OpenAI Vision model with hairstyle similarity scoring, landmark detection, and reference-based matching.",
            "tech": ["OpenAI Vision", "Computer Vision", "Haar Cascade", "Async Processing"]
        },
        {
            "title": "🎬 AI Content Generation",
            "subtitle": "Images & Videos with Stable Diffusion",
            "description": "Professional content creation pipeline using Stable Diffusion and ComfyUI for marketing materials with flicker-free video generation.",
            "tech": ["Stable Diffusion", "ComfyUI", "ControlNet", "Video Processing"]
        },
        {
            "title": "🤖 ComfyUI Automation",
            "subtitle": "Video Style Transfer Pipeline",
            "description": "Automated workflow for transforming videos into stylized animations using Python, OpenCV, FFmpeg, and AI-driven scene selection.",
            "tech": ["ComfyUI", "OpenCV", "FFmpeg", "Python", "AI Animation"]
        },
        {
            "title": "👤 Face Recognition System",
            "subtitle": "Automated Attendance Tracking",
            "description": "Real-time facial recognition attendance system using LBPH algorithm with Tkinter GUI and MySQL database integration.",
            "tech": ["OpenCV", "LBPH", "Tkinter", "MySQL", "Real-time Processing"]
        },
        {
            "title": "📊 Twitter Sentiment Analysis",
            "subtitle": "Hybrid AI Architecture",
            "description": "Advanced sentiment analysis using hybrid RNN and Transformer architectures (BERT) for real-time emotion detection and trend analysis.",
            "tech": ["BERT", "RNNs", "TensorFlow", "Hugging Face", "NLP"]
        }
    ]

    for project in projects:
        st.markdown(f"""
        <div class="project-card">
            <h3 style="color: #6366f1; margin-bottom: 0.5rem;">{project['title']}</h3>
            <h4 style="opacity: 0.8; margin-bottom: 1rem; font-weight: 500;">{project['subtitle']}</h4>
            <p style="margin-bottom: 1rem; line-height: 1.6;">{project['description']}</p>
            <div>
                {''.join([f'<span class="skill-pill">{tech}</span>' for tech in project['tech']])}
            </div>
        </div>
        """, unsafe_allow_html=True)