import streamlit as st
import base64

def get_img_as_base64(file_path):
    """Convert image to base64 string"""
    try:
        with open(file_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except FileNotFoundError:
        return None

def create_download_link(file_path, link_text):
    """Create a download link for the CV file"""
    try:
        with open(file_path, 'rb') as f:
            data = f.read()
        b64 = base64.b64encode(data).decode()
        href = f'<a href="data:application/pdf;base64,{b64}" download="{file_path}" class="download-btn">📄 {link_text}</a>'
        return href
    except FileNotFoundError:
        return f'<button class="download-btn" onclick="alert(\'CV file not found. Please add AI-Resume.pdf to the directory.\')">📄 {link_text}</button>'

def show():
    # Profile Header with Image
    profile_img_b64 = get_img_as_base64("images/profile.jpg")
    # Social Icons
    social_icons_data = {
        # Platform: [URL, Icon]
        "Email": ["mailto:basitali171480@gmail.com", "https://cdn-icons-png.flaticon.com/512/732/732200.png"],
        "LinkedIn": ["https://www.linkedin.com/in/basit-ali11", "https://cdn-icons-png.flaticon.com/512/174/174857.png"],
        "GitHub": ["https://github.com/basitali11", "https://icon-library.com/images/github-icon-white/github-icon-white-6.jpg"],
    }

    social_icons_html = [f"<a href='{social_icons_data[platform][0]}' target='_blank' style='margin-right: 10px;'><img class='social-icon' src='{social_icons_data[platform][1]}' alt='{platform}'></a>" for platform in social_icons_data]


    if profile_img_b64:
        st.markdown(f"""
        <div class="profile-header">
        <div class="profile-image">
            <img src="data:image/jpeg;base64,{profile_img_b64}" alt="Basit Ali"/>
        </div>
        <div class="profile-info">
            <h1>Basit Ali</h1>
            <div class="subtitle">AI Developer & Machine Learning Engineer</div>
            <div class="social-icons">
                {''.join(social_icons_html)}
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Section Divider
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

    # ABOUT SECTION
    st.markdown('<h2 class="section-title">About Me</h2>', unsafe_allow_html=True)

    # Personal Info
    st.markdown("""
    <div class="modern-card">
        <h3>👨‍💻 Professional Profile</h3>
        <p>Passionate AI Developer with 2+ years of hands-on experience in designing and deploying intelligent systems that bridge cutting-edge artificial intelligence capabilities with real-world business applications. Proven track record in developing scalable AI solutions, optimizing model performance, and integrating advanced technologies like natural language processing (NLP), computer vision, and generative AI to solve complex challenges across industries.</p>
    </div>
    """, unsafe_allow_html=True)

    # Education & Certifications in columns
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="modern-card">
            <h3>🎓 Education</h3>
            <div style="margin-top: 1rem;">
                <strong>Bachelor of Science in Information Technology</strong><br>
                <span style="color: #6366f1;">University of the Punjab, Lahore</span><br>
                <span style="opacity: 0.7;">Foundation in software development, algorithms, and system design</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="modern-card">
            <h3>🏆 Certifications</h3>
            <div style="margin-top: 1rem;">
                <div style="margin: 0.5rem 0;">
                    <span class="skill-pill">Certified AI Developer - NAVTTC</span>
                </div>
                <div style="margin: 0.5rem 0;">
                    <span class="skill-pill">Microsoft Azure AI Fundamentals</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Section Divider
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

    # Quick Stats
    st.markdown("""
    <div class="stats-grid">
        <div class="stat-card">
            <div class="stat-number">2+</div>
            <div class="stat-label">Years Experience</div>
        </div>
        <div class="stat-card">
            <div class="stat-number">10+</div>
            <div class="stat-label">Major Projects</div>
        </div>
        <div class="stat-card">
            <div class="stat-number">2</div>
            <div class="stat-label">Certifications</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Section Divider
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

    # SKILLS SECTION
    st.markdown('<h2 class="section-title">Technical Expertise</h2>', unsafe_allow_html=True)

    skills_categories = [
        {
            "title": "🤖 Natural Language Processing",
            "skills": ["Large Language Models (LLMs)", "LangChain", "Embeddings", "Vector Search", "NLTK", "Transformers"]
        },
        {
            "title": "🧠 Machine Learning & Deep Learning",
            "skills": ["Scikit-Learn", "TensorFlow", "Keras", "PyTorch", "OpenCV", "Computer Vision"]
        },
        {
            "title": "☁️ Cloud & Deployment",
            "skills": ["Amazon EC2", "PM2", "Heroku", "Streamlit Cloud", "Google Colab", "FastAPI", "Flask", "Streamlit"]
        },
        {
            "title": "🎤 Voice & Speech Processing",
            "skills": ["Text-to-Speech", "Speech-to-Text", "ElevenLabs", "OpenAI Whisper", "Audio Processing"]
        },
        {
            "title": "💻 Programming Languages",
            "skills": ["Python", "C++", "HTML", "CSS", "SQL"]
        },
        {
            "title": "🗄️ Databases & Tools",
            "skills": ["MySQL", "SQLite", "Git", "Linux", "API Development"]
        },
        {
            "title": "🎨 Generative AI",
            "skills": ["Stable Diffusion", "ComfyUI", "Image Generation", "Video Generation", "SeaArt"]
        },
        {
            "title": "🔧 Frameworks & Libraries",
            "skills": ["OpenAI API", "Hugging Face", "BERT", "ControlNet", "RAG Systems"]
        }
    ]

    # Display skills in a 2-column layout
    for i in range(0, len(skills_categories), 2):
        col1, col2 = st.columns(2)
        
        with col1:
            category = skills_categories[i]
            st.markdown(f"""
            <div class="modern-card">
                <h3>{category['title']}</h3>
                <div style="margin-top: 1rem;">
                    {''.join([f'<span class="skill-pill">{skill}</span>' for skill in category['skills']])}
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            if i + 1 < len(skills_categories):
                category = skills_categories[i + 1]
                st.markdown(f"""
                <div class="modern-card">
                    <h3>{category['title']}</h3>
                    <div style="margin-top: 1rem;">
                        {''.join([f'<span class="skill-pill">{skill}</span>' for skill in category['skills']])}
                    </div>
                </div>
                """, unsafe_allow_html=True)

    # Download CV Section
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        # Create download link for CV
        download_link = create_download_link("AI-Resume.pdf", "Download CV")
        st.markdown(download_link, unsafe_allow_html=True)