
# import streamlit as st
# import base64
# from pathlib import Path

# # Page configuration
# st.set_page_config(
#     page_title="Basit Ali - AI Developer Portfolio",
#     page_icon="./images/profile_icon.png",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # Custom CSS for modern, theme-adaptive styling
# st.markdown("""
# <style>
#     @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
#     * {
#         font-family: 'Inter', sans-serif;
#     }
    
#     /* Main container styling */
#     .main-container {
#         max-width: 1200px;
#         margin: 0 auto;
#         padding: 1rem;
#     }
    
#     /* Modern Navigation Styling */
#     .nav-container {
#         background: rgba(255, 255, 255, 0.05);
#         backdrop-filter: blur(15px);
#         border: 1px solid rgba(255, 255, 255, 0.1);
#         border-radius: 20px;
#         padding: 1rem;
#         margin-bottom: 2rem;
#         box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
#     }
    
#     .nav-grid {
#         display: grid;
#         grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
#         gap: 1rem;
#     }
    
#     .nav-item {
#         background: rgba(255, 255, 255, 0.02);
#         border: 2px solid rgba(255, 255, 255, 0.1);
#         border-radius: 16px;
#         padding: 1.2rem 1.5rem;
#         text-align: center;
#         cursor: pointer;
#         transition: all 0.3s ease;
#         position: relative;
#         overflow: hidden;
#     }
    
#     .nav-item::before {
#         content: '';
#         position: absolute;
#         top: 0;
#         left: -100%;
#         width: 100%;
#         height: 100%;
#         background: linear-gradient(90deg, transparent, rgba(99, 102, 241, 0.1), transparent);
#         transition: left 0.5s ease;
#     }
    
#     .nav-item:hover::before {
#         left: 100%;
#     }
    
#     .nav-item:hover {
#         transform: translateY(-3px);
#         border-color: rgba(99, 102, 241, 0.5);
#         box-shadow: 0 10px 30px rgba(99, 102, 241, 0.2);
#         background: rgba(99, 102, 241, 0.05);
#     }
    
#     .nav-item.active {
#         border-color: #6366f1;
#         background: rgba(99, 102, 241, 0.1);
#         box-shadow: 0 8px 25px rgba(99, 102, 241, 0.3);
#     }
    
#     .nav-icon {
#         font-size: 2rem;
#         margin-bottom: 0.5rem;
#         display: block;
#     }
    
#     .nav-title {
#         font-weight: 600;
#         font-size: 1.1rem;
#         margin: 0;
#     }
    
#     /* Remove underlines and fix link colors */
#     a, .nav-item a, .download-btn {
#         text-decoration: none !important;
#         color: inherit !important;
#     }
    
#     .nav-subtitle {
#         font-size: 0.8rem;
#         opacity: 0.7;
#         margin: 0.3rem 0 0 0;
#     }
    
#     /* Profile section with image */
#     .profile-header {
#         display: flex;
#         align-items: center;
#         gap: 2rem;
#         padding: 2rem;
#         background: rgba(255, 255, 255, 0.02);
#         backdrop-filter: blur(10px);
#         border: 1px solid rgba(255, 255, 255, 0.1);
#         border-radius: 20px;
#         margin-bottom: 2rem;
#         box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
#     }
    
#     .profile-image {
#         width: 120px;
#         height: 120px;
#         border-radius: 50%;
#         background: linear-gradient(135deg, #6366f1, #8b5cf6, #ec4899);
#         display: flex;
#         align-items: center;
#         justify-content: center;
#         font-size: 3rem;
#         color: white;
#         box-shadow: 0 8px 25px rgba(99, 102, 241, 0.3);
#         flex-shrink: 0;
#         overflow: hidden;
#     }
    
#     .profile-image img {
#         width: 100%;
#         height: 100%;
#         object-fit: cover;
#         border-radius: 50%;
#     }
    
#     .profile-info h1 {
#         font-size: 2.5rem;
#         font-weight: 800;
#         margin: 0 0 0.5rem 0;
#         background: linear-gradient(135deg, #6366f1, #8b5cf6);
#         -webkit-background-clip: text;
#         -webkit-text-fill-color: transparent;
#         background-clip: text;
#     }
    
#     .profile-info .subtitle {
#         font-size: 1.2rem;
#         opacity: 0.8;
#         margin: 0 0 1rem 0;
#         font-weight: 500;
#     }
    
#     .profile-info .location {
#         font-size: 1rem;
#         opacity: 0.7;
#         margin: 0;
#     }
    
#     /* Modern card styling */
#     .modern-card {
#         background: rgba(255, 255, 255, 0.03);
#         backdrop-filter: blur(10px);
#         border: 1px solid rgba(255, 255, 255, 0.1);
#         border-radius: 16px;
#         padding: 1.5rem;
#         margin: 1rem 0;
#         transition: all 0.3s ease;
#         box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
#     }
    
#     .modern-card:hover {
#         transform: translateY(-2px);
#         box-shadow: 0 8px 30px rgba(0, 0, 0, 0.1);
#         border-color: rgba(99, 102, 241, 0.3);
#     }
    
#     /* Skill pills */
#     .skill-pill {
#         display: inline-block;
#         background: rgba(99, 102, 241, 0.1);
#         border: 1px solid rgba(99, 102, 241, 0.3);
#         color: #6366f1;
#         padding: 0.4rem 0.8rem;
#         border-radius: 20px;
#         font-size: 0.85rem;
#         font-weight: 500;
#         margin: 0.2rem;
#         transition: all 0.3s ease;
#     }
    
#     .skill-pill:hover {
#         background: rgba(99, 102, 241, 0.2);
#         transform: translateY(-1px);
#     }
    
#     /* Project cards */
#     .project-card {
#         background: rgba(255, 255, 255, 0.02);
#         border: 1px solid rgba(255, 255, 255, 0.1);
#         border-radius: 16px;
#         padding: 1.5rem;
#         margin: 1rem 0;
#         transition: all 0.3s ease;
#         position: relative;
#         overflow: hidden;
#     }
    
#     .project-card::before {
#         content: '';
#         position: absolute;
#         top: 0;
#         left: 0;
#         right: 0;
#         height: 3px;
#         background: linear-gradient(90deg, #6366f1, #8b5cf6, #ec4899);
#         opacity: 0;
#         transition: opacity 0.3s ease;
#     }
    
#     .project-card:hover::before {
#         opacity: 1;
#     }
    
#     .project-card:hover {
#         transform: translateY(-3px);
#         border-color: rgba(99, 102, 241, 0.3);
#         box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1);
#     }
    
#     /* Section headers */
#     .section-title {
#         font-size: 2rem;
#         font-weight: 700;
#         text-align: center;
#         margin: 2rem 0;
#         background: linear-gradient(135deg, #6366f1, #8b5cf6);
#         -webkit-background-clip: text;
#         -webkit-text-fill-color: transparent;
#         background-clip: text;
#     }
    
#     /* Fixed section divider */
#     .section-divider {
#         width: 100%;
#         height: 3px !important;
#         background: linear-gradient(90deg, transparent, #6366f1, #8b5cf6, #ec4899, transparent) !important;
#         border: none !important;
#         margin: 3rem 0 !important;
#         border-radius: 2px !important;
#         display: block !important;
#     }
    
#     /* Stats grid */
#     .stats-grid {
#         display: grid;
#         grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
#         gap: 1rem;
#         margin: 2rem 0;
#     }
    
#     .stat-card {
#         background: rgba(255, 255, 255, 0.03);
#         border: 1px solid rgba(255, 255, 255, 0.1);
#         border-radius: 12px;
#         padding: 1.5rem;
#         text-align: center;
#         transition: all 0.3s ease;
#     }
    
#     .stat-card:hover {
#         border-color: rgba(99, 102, 241, 0.4);
#         transform: translateY(-2px);
#     }
    
#     .stat-number {
#         font-size: 2rem;
#         font-weight: 800;
#         color: #6366f1;
#         margin: 0;
#     }
    
#     .stat-label {
#         font-size: 0.9rem;
#         opacity: 0.7;
#         margin: 0.5rem 0 0 0;
#         font-weight: 500;
#     }
    
#     /* Download button */
#     .download-section {
#         text-align: center;
#         padding: 2rem;
#         background: rgba(99, 102, 241, 0.05);
#         border: 1px solid rgba(99, 102, 241, 0.2);
#         border-radius: 16px;
#         margin: 2rem 0;
#     }
    
#     .download-btn {
#         background: linear-gradient(135deg, #6366f1, #8b5cf6);
#         color: white;
#         border: none;
#         padding: 1rem 2rem;
#         border-radius: 12px;
#         font-weight: 600;
#         font-size: 1rem;
#         cursor: pointer;
#         transition: all 0.3s ease;
#         box-shadow: 0 4px 15px rgba(99, 102, 241, 0.3);
#         text-decoration: none;
#         display: inline-block;
#     }
    
#     .download-btn:hover {
#         transform: translateY(-2px);
#         box-shadow: 0 8px 25px rgba(99, 102, 241, 0.4);
#     }
    
#     /* Timeline for experience */
#     .timeline-item {
#         position: relative;
#         padding-left: 2rem;
#         margin: 2rem 0;
#     }
    
#     .timeline-item::before {
#         content: '';
#         position: absolute;
#         left: 0;
#         top: 0.5rem;
#         width: 12px;
#         height: 12px;
#         background: #6366f1;
#         border-radius: 50%;
#         box-shadow: 0 0 0 4px rgba(99, 102, 241, 0.2);
#     }
    
#     .timeline-item::after {
#         content: '';
#         position: absolute;
#         left: 5px;
#         top: 1.5rem;
#         width: 2px;
#         height: calc(100% - 1rem);
#         background: rgba(99, 102, 241, 0.2);
#     }
    
#     .timeline-item:last-child::after {
#         display: none;
#     }
    
#     /* Contact form styling */
#     .contact-grid {
#         display: grid;
#         grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
#         gap: 1rem;
#         margin: 2rem 0;
#     }
    
#     .contact-item {
#         background: rgba(255, 255, 255, 0.02);
#         border: 1px solid rgba(255, 255, 255, 0.1);
#         border-radius: 12px;
#         padding: 1.5rem;
#         text-align: center;
#         transition: all 0.3s ease;
#     }
    
#     .contact-item:hover {
#         border-color: rgba(99, 102, 241, 0.3);
#         transform: translateY(-2px);
#     }
    
#     .contact-item a {
#         color: inherit;
#         text-decoration: none;
#     }
    
#     .contact-item:hover a {
#         color: #6366f1;
#     }
    
#     .contact-icon {
#         font-size: 2rem;
#         margin-bottom: 1rem;
#         color: #6366f1;
#     }
    
#     /* Responsive design */
#     @media (max-width: 768px) {
#         .profile-header {
#             flex-direction: column;
#             text-align: center;
#         }
        
#         .profile-info h1 {
#             font-size: 2rem;
#         }
        
#         .nav-grid {
#             grid-template-columns: repeat(2, 1fr);
#         }
#     }
    
#     /* Streamlit specific overrides */
#     .stButton > button {
#         background: linear-gradient(135deg, #6366f1, #8b5cf6) !important;
#         color: white !important;
#         border: none !important;
#         padding: 0.75rem 1.5rem !important;
#         border-radius: 12px !important;
#         font-weight: 600 !important;
#         transition: all 0.3s ease !important;
#         box-shadow: 0 4px 15px rgba(99, 102, 241, 0.3) !important;
#     }
    
#     .stButton > button:hover {
#         transform: translateY(-2px) !important;
#         box-shadow: 0 8px 25px rgba(99, 102, 241, 0.4) !important;
#     }
    
#     /* Sidebar styling */
#     .css-1d391kg {
#         background: rgba(255, 255, 255, 0.02) !important;
#     }
    
#     /* Hide streamlit menu and footer */
#     #MainMenu {visibility: hidden;}
#     footer {visibility: hidden;}
#     header {visibility: hidden;}
# </style>
# """, unsafe_allow_html=True)

# # Function to create download link for CV
# def create_download_link(file_path, link_text):
#     """Create a download link for the CV file"""
#     try:
#         with open(file_path, 'rb') as f:
#             data = f.read()
#         b64 = base64.b64encode(data).decode()
#         href = f'<a href="data:application/pdf;base64,{b64}" download="{file_path}" class="download-btn">📄 {link_text}</a>'
#         return href
#     except FileNotFoundError:
#         return f'<button class="download-btn" onclick="alert(\'CV file not found. Please add AI-Resume.pdf to the directory.\')">📄 {link_text}</button>'

# # Function to get base64 of image for profile
# def get_img_as_base64(file_path):
#     """Convert image to base64 string"""
#     try:
#         with open(file_path, "rb") as img_file:
#             return base64.b64encode(img_file.read()).decode()
#     except FileNotFoundError:
#         return None

# # Session state setup
# if 'selected_section' not in st.session_state:
#     st.session_state.selected_section = "Home"

# # Handle navigation via query params (Streamlit >=1.30)
# query_params = st.query_params
# if "section" in query_params:
#     st.session_state.selected_section = query_params["section"]

# # Navigation buttons styled as HTML divs using form
# st.markdown("""
# <div class="nav-container">
#     <div class="nav-grid">
#         <a href="?section=Home"><div class="nav-item">
#             <div class="nav-icon">🏠</div>
#             <div class="nav-title">Home</div>
#             <div class="nav-subtitle">Overview & Skills</div>
#         </div></a>
#         <a href="?section=Experience"><div class="nav-item">
#             <div class="nav-icon">💼</div>
#             <div class="nav-title">Experience</div>
#             <div class="nav-subtitle">Professional Journey</div>
#         </div></a>
#         <a href="?section=Projects"><div class="nav-item">
#             <div class="nav-icon">🚀</div>
#             <div class="nav-title">Projects</div>
#             <div class="nav-subtitle">Featured Work</div>
#         </div></a>
#         <a href="?section=Contact"><div class="nav-item">
#             <div class="nav-icon">📞</div>
#             <div class="nav-title">Contact</div>
#             <div class="nav-subtitle">Get In Touch</div>
#         </div></a>
#     </div>
# </div>
# """, unsafe_allow_html=True)


# # Use session state for current selection
# current_section = st.session_state.selected_section

# # Main Content
# if current_section == "Home":
#     # Profile Header with Image
#     profile_img_b64 = get_img_as_base64("images/profile.jpg")  # Add your profile image as profile.jpg
    
#     if profile_img_b64:
#         st.markdown(f"""
#         <div class="profile-header">
#             <div class="profile-image">
#                 <img src="data:image/jpeg;base64,{profile_img_b64}" alt="Basit Ali"/>
#             </div>
#             <div class="profile-info">
#                 <h1>Basit Ali</h1>
#                 <div class="subtitle">AI Developer & Machine Learning Engineer</div>
#                 <div class="location">📍 Lahore, Pakistan</div>
#             </div>
#         </div>
#         """, unsafe_allow_html=True)
#     else:
#         st.markdown("""
#         <div class="profile-header">
#             <div class="profile-image">
#                 👨‍💻
#             </div>
#             <div class="profile-info">
#                 <h1>Basit Ali</h1>
#                 <div class="subtitle">AI Developer & Machine Learning Engineer</div>
#                 <div class="location">📍 Lahore, Pakistan</div>
#             </div>
#         </div>
#         """, unsafe_allow_html=True)
#         st.info("💡 Add your profile image as 'profile.jpg' in the app directory to display your photo")
    
#     # Section Divider
#     st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

#     # ABOUT SECTION
#     st.markdown('<h2 class="section-title">About Me</h2>', unsafe_allow_html=True)
    
#     # Personal Info
#     st.markdown("""
#     <div class="modern-card">
#         <h3>👨‍💻 Professional Profile</h3>
#         <p>Passionate AI Developer with over a year of experience in cutting-edge technologies. 
#         I specialize in creating intelligent solutions that bridge the gap between complex AI capabilities 
#         and practical business applications.</p>
#     </div>
#     """, unsafe_allow_html=True)

#     # Education & Certifications in columns
#     col1, col2 = st.columns(2)
    
#     with col1:
#         st.markdown("""
#         <div class="modern-card">
#             <h3>🎓 Education</h3>
#             <div style="margin-top: 1rem;">
#                 <strong>Bachelor of Science in Information Technology</strong><br>
#                 <span style="color: #6366f1;">University of the Punjab, Lahore</span><br>
#                 <span style="opacity: 0.7;">Foundation in software development, algorithms, and system design</span>
#             </div>
#         </div>
#         """, unsafe_allow_html=True)
    
#     with col2:
#         st.markdown("""
#         <div class="modern-card">
#             <h3>🏆 Certifications</h3>
#             <div style="margin-top: 1rem;">
#                 <div style="margin: 0.5rem 0;">
#                     <span class="skill-pill">Certified AI Developer - NAVTTC</span>
#                 </div>
#                 <div style="margin: 0.5rem 0;">
#                     <span class="skill-pill">Microsoft Azure AI Fundamentals</span>
#                 </div>
#             </div>
#         </div>
#         """, unsafe_allow_html=True)
    
#     # Section Divider
#     st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

#     # Quick Stats
#     st.markdown("""
#     <div class="stats-grid">
#         <div class="stat-card">
#             <div class="stat-number">2+</div>
#             <div class="stat-label">Years Experience</div>
#         </div>
#         <div class="stat-card">
#             <div class="stat-number">7+</div>
#             <div class="stat-label">Major Projects</div>
#         </div>
#         <div class="stat-card">
#             <div class="stat-number">2</div>
#             <div class="stat-label">Certifications</div>
#         </div>
#     </div>
#     """, unsafe_allow_html=True)
    
#     # Section Divider
#     st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    
#     # SKILLS SECTION MERGED
#     st.markdown('<h2 class="section-title">Technical Expertise</h2>', unsafe_allow_html=True)
    
#     skills_categories = [
#         {
#             "title": "🤖 Natural Language Processing",
#             "skills": ["Large Language Models (LLMs)", "LangChain", "Embeddings", "Vector Search", "NLTK", "Transformers"]
#         },
#         {
#             "title": "🧠 Machine Learning & Deep Learning",
#             "skills": ["Scikit-Learn", "TensorFlow", "Keras", "PyTorch", "OpenCV", "Computer Vision"]
#         },
#         {
#             "title": "☁️ Cloud & Deployment",
#             "skills": ["Amazon EC2", "PM2", "Heroku", "Streamlit Cloud", "Google Colab", "FastAPI", "Flask", "Streamlit"]
#         },
#         {
#             "title": "🎤 Voice & Speech Processing",
#             "skills": ["Text-to-Speech", "Speech-to-Text", "ElevenLabs", "OpenAI Whisper", "Audio Processing"]
#         },
#         {
#             "title": "💻 Programming Languages",
#             "skills": ["Python", "C++", "HTML", "CSS", "SQL"]
#         },
#         {
#             "title": "🗄️ Databases & Tools",
#             "skills": ["MySQL", "SQLite", "Git", "Linux", "API Development"]
#         },
#         {
#             "title": "🎨 Generative AI",
#             "skills": ["Stable Diffusion", "ComfyUI", "Image Generation", "Video Generation", "SeaArt"]
#         },
#         {
#             "title": "🔧 Frameworks & Libraries",
#             "skills": ["OpenAI API", "Hugging Face", "BERT", "ControlNet", "RAG Systems"]
#         }
#     ]
    
#     # Display skills in a 2-column layout
#     for i in range(0, len(skills_categories), 2):
#         col1, col2 = st.columns(2)
        
#         with col1:
#             category = skills_categories[i]
#             st.markdown(f"""
#             <div class="modern-card">
#                 <h3>{category['title']}</h3>
#                 <div style="margin-top: 1rem;">
#                     {''.join([f'<span class="skill-pill">{skill}</span>' for skill in category['skills']])}
#                 </div>
#             </div>
#             """, unsafe_allow_html=True)
        
#         with col2:
#             if i + 1 < len(skills_categories):
#                 category = skills_categories[i + 1]
#                 st.markdown(f"""
#                 <div class="modern-card">
#                     <h3>{category['title']}</h3>
#                     <div style="margin-top: 1rem;">
#                         {''.join([f'<span class="skill-pill">{skill}</span>' for skill in category['skills']])}
#                     </div>
#                 </div>
#                 """, unsafe_allow_html=True)
    
#     # Download CV Section
#     st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    
#     col1, col2, col3 = st.columns([1, 1, 1])
#     with col1:
#         # Create download link for CV
#         download_link = create_download_link("AI-Resume.pdf", "Download CV")
#         st.markdown(download_link, unsafe_allow_html=True)

# elif current_section == "Experience":
#     st.markdown('<h2 class="section-title">Professional Experience</h2>', unsafe_allow_html=True)
    
#     st.markdown("""
#     <div class="timeline-item">
#         <div class="modern-card">
#             <h3 style="color: #6366f1;">🏢 AI Developer</h3>
#             <h4 style="opacity: 0.8; margin: 0.5rem 0;">NOBORDER.z INNOVATIONS, Lahore</h4>
#             <p style="color: #6366f1; font-weight: 600; margin-bottom: 1rem;">October 2023 - Present</p>
            
#             <p style="margin-bottom: 1.5rem; line-height: 1.6;">
#                 Leading AI development initiatives with focus on conversational AI, computer vision, and generative AI solutions. 
#                 Responsible for developing sophisticated AI-driven systems and implementing cutting-edge NLP technologies.
#             </p>
            
#             <h4 style="margin-bottom: 1rem;">🎯 Key Achievements:</h4>
#             <ul style="line-height: 1.8; margin-left: 1rem;">
#                 <li>Developed personality-driven conversational AI using state-of-the-art LLMs</li>
#                 <li>Implemented advanced facial feature detection with OpenAI Vision</li>
#                 <li>Created AI-powered image and video generation systems for marketing</li>
#                 <li>Built automated ComfyUI workflows for video transformation</li>
#                 <li>Designed real-time face recognition attendance systems</li>
#                 <li>Engineered sentiment analysis pipelines with hybrid architectures</li>
#                 <li>Optimized model performance using Groq for real-time processing</li>
#             </ul>
#         </div>
#     </div>
#     """, unsafe_allow_html=True)
    
#     # Professional Competencies
#     st.markdown("""
#     <div class="modern-card">
#         <h3>🎯 Professional Competencies</h3>
#         <div style="margin-top: 1.5rem;">
#             <div style="margin-bottom: 1.5rem;">
#                 <h4 style="color: #6366f1; margin-bottom: 0.5rem;">Advanced AI System Development</h4>
#                 <p>Proficient in designing and deploying sophisticated AI-driven systems with proven track record in AI chatbot development using OpenAI frameworks.</p>
#             </div>
#             <div style="margin-bottom: 1.5rem;">
#                 <h4 style="color: #6366f1; margin-bottom: 0.5rem;">Natural Language Processing Excellence</h4>
#                 <p>Strong proficiency in NLP, sentiment analysis, language understanding, and automated content generation with emotion classification expertise.</p>
#             </div>
#             <div>
#                 <h4 style="color: #6366f1; margin-bottom: 0.5rem;">Innovative Technical Integration</h4>
#                 <p>Renowned for seamlessly integrating AI technologies to deliver superior functionality, including expertise in image and video generation.</p>
#             </div>
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

# elif current_section == "Projects":
#     st.markdown('<h2 class="section-title">Featured Projects</h2>', unsafe_allow_html=True)
    
#     projects = [
#         {
#             "title": "🎯 Xana AI Protocol",
#             "subtitle": "Personality-Driven Conversational AI",
#             "description": "Advanced conversational AI using state-of-the-art LLMs (Gemma, Mixtral, Llama) with dynamic personality adaptation, RAG integration, and real-time processing optimization.",
#             "tech": ["LLMs", "LangChain", "RAG", "Groq", "FastAPI", "SQLite"]
#         },
#         {
#             "title": "🎙️ Voice AI Assistant",
#             "subtitle": "Voice-Enabled Chatbot",
#             "description": "Seamless voice interactions using OpenAI GPT-4, LangChain framework, ElevenLabs TTS, and Whisper STT for natural conversation flow.",
#             "tech": ["OpenAI GPT-4", "LangChain", "ElevenLabs", "Whisper", "Voice Processing"]
#         },
#         {
#             "title": "👁️ UGC Facial Analysis",
#             "subtitle": "AI-Powered Feature Detection",
#             "description": "Advanced facial feature detection using OpenAI Vision model with hairstyle similarity scoring, landmark detection, and reference-based matching.",
#             "tech": ["OpenAI Vision", "Computer Vision", "Haar Cascade", "Async Processing"]
#         },
#         {
#             "title": "🎬 AI Content Generation",
#             "subtitle": "Images & Videos with Stable Diffusion",
#             "description": "Professional content creation pipeline using Stable Diffusion and ComfyUI for marketing materials with flicker-free video generation.",
#             "tech": ["Stable Diffusion", "ComfyUI", "ControlNet", "Video Processing"]
#         },
#         {
#             "title": "🤖 ComfyUI Automation",
#             "subtitle": "Video Style Transfer Pipeline",
#             "description": "Automated workflow for transforming videos into stylized animations using Python, OpenCV, FFmpeg, and AI-driven scene selection.",
#             "tech": ["ComfyUI", "OpenCV", "FFmpeg", "Python", "AI Animation"]
#         },
#         {
#             "title": "👤 Face Recognition System",
#             "subtitle": "Automated Attendance Tracking",
#             "description": "Real-time facial recognition attendance system using LBPH algorithm with Tkinter GUI and MySQL database integration.",
#             "tech": ["OpenCV", "LBPH", "Tkinter", "MySQL", "Real-time Processing"]
#         },
#         {
#             "title": "📊 Twitter Sentiment Analysis",
#             "subtitle": "Hybrid AI Architecture",
#             "description": "Advanced sentiment analysis using hybrid RNN and Transformer architectures (BERT) for real-time emotion detection and trend analysis.",
#             "tech": ["BERT", "RNNs", "TensorFlow", "Hugging Face", "NLP"]
#         }
#     ]
    
#     for project in projects:
#         st.markdown(f"""
#         <div class="project-card">
#             <h3 style="color: #6366f1; margin-bottom: 0.5rem;">{project['title']}</h3>
#             <h4 style="opacity: 0.8; margin-bottom: 1rem; font-weight: 500;">{project['subtitle']}</h4>
#             <p style="margin-bottom: 1rem; line-height: 1.6;">{project['description']}</p>
#             <div>
#                 {''.join([f'<span class="skill-pill">{tech}</span>' for tech in project['tech']])}
#             </div>
#         </div>
#         """, unsafe_allow_html=True)

# elif current_section == "Experience":
#     st.markdown('<h2 class="section-title">Professional Experience</h2>', unsafe_allow_html=True)
    
#     st.markdown("""
#     <div class="timeline-item">
#         <div class="modern-card">
#             <h3 style="color: #6366f1;">🏢 AI Developer</h3>
#             <h4 style="opacity: 0.8; margin: 0.5rem 0;">NOBORDER.z INNOVATIONS, Lahore</h4>
#             <p style="color: #6366f1; font-weight: 600; margin-bottom: 1rem;">October 2023 - Present</p>
            
#             <p style="margin-bottom: 1.5rem; line-height: 1.6;">
#                 Leading AI development initiatives with focus on conversational AI, computer vision, and generative AI solutions. 
#                 Responsible for developing sophisticated AI-driven systems and implementing cutting-edge NLP technologies.
#             </p>
            
#             <h4 style="margin-bottom: 1rem;">🎯 Key Achievements:</h4>
#             <ul style="line-height: 1.8; margin-left: 1rem;">
#                 <li>Developed personality-driven conversational AI using state-of-the-art LLMs</li>
#                 <li>Implemented advanced facial feature detection with OpenAI Vision</li>
#                 <li>Created AI-powered image and video generation systems for marketing</li>
#                 <li>Built automated ComfyUI workflows for video transformation</li>
#                 <li>Designed real-time face recognition attendance systems</li>
#                 <li>Engineered sentiment analysis pipelines with hybrid architectures</li>
#                 <li>Optimized model performance using Groq for real-time processing</li>
#             </ul>
#         </div>
#     </div>
#     """, unsafe_allow_html=True)
    
#     # Professional Competencies
#     st.markdown("""
#     <div class="modern-card">
#         <h3>🎯 Professional Competencies</h3>
#         <div style="margin-top: 1.5rem;">
#             <div style="margin-bottom: 1.5rem;">
#                 <h4 style="color: #6366f1; margin-bottom: 0.5rem;">Advanced AI System Development</h4>
#                 <p>Proficient in designing and deploying sophisticated AI-driven systems with proven track record in AI chatbot development using OpenAI frameworks.</p>
#             </div>
#             <div style="margin-bottom: 1.5rem;">
#                 <h4 style="color: #6366f1; margin-bottom: 0.5rem;">Natural Language Processing Excellence</h4>
#                 <p>Strong proficiency in NLP, sentiment analysis, language understanding, and automated content generation with emotion classification expertise.</p>
#             </div>
#             <div>
#                 <h4 style="color: #6366f1; margin-bottom: 0.5rem;">Innovative Technical Integration</h4>
#                 <p>Renowned for seamlessly integrating AI technologies to deliver superior functionality, including expertise in image and video generation.</p>
#             </div>
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

# elif current_section == "Contact":
#     st.markdown('<h2 class="section-title">Let\'s Connect</h2>', unsafe_allow_html=True)
    
#     # Contact Information
#     st.markdown("""
#     <div class="contact-grid">
#         <div class="contact-item">
#             <div class="contact-icon">📧</div>
#             <h4>Email</h4>
#             <p>basitali171480@gmail.com</p>
#         </div>
#         <div class="contact-item">
#             <div class="contact-icon">📱</div>
#             <h4>Phone</h4>
#             <p>+92-3219498096</p>
#         </div>
#         <div class="contact-item">
#             <div class="contact-icon">📍</div>
#             <h4>Location</h4>
#             <p>Lahore, Pakistan</p>
#         </div>
#         <div class="contact-item">
#             <div class="contact-icon">💼</div>
#             <h4>LinkedIn</h4>
#             <p>Professional Profile</p>
#         </div>
#     </div>
#     """, unsafe_allow_html=True)
    
#     # Contact Form
#     st.markdown("""
#     <div class="modern-card">
#         <h3>📝 Send a Message</h3>
#         <p style="opacity: 0.8; margin-bottom: 1.5rem;">Ready to discuss AI projects and opportunities? Let's connect!</p>
#     </div>
#     """, unsafe_allow_html=True)
    
#     with st.form("contact_form", clear_on_submit=True):
#         col1, col2 = st.columns(2)
#         with col1:
#             name = st.text_input("Your Name *")
#         with col2:
#             email = st.text_input("Your Email *")
        
#         subject = st.text_input("Subject *")
#         message = st.text_area("Your Message *", height=120)
        
#         submitted = st.form_submit_button("Send Message 🚀")
        
#         if submitted:
#             if name and email and subject and message:
#                 st.success("🎉 Thank you for your message! I'll get back to you soon.")
#                 st.balloons()
#             else:
#                 st.error("⚠️ Please fill in all required fields.")

# # Footer
# st.markdown("""
# <div style="margin-top: 4rem; padding: 2rem; text-align: center; border-top: 1px solid rgba(255, 255, 255, 0.1);">
#     <p style="opacity: 0.7; margin: 0;">
#         🚀 Built with Streamlit | © 2024 Basit Ali - AI Developer
#     </p>
#     <p style="opacity: 0.5; margin: 0.5rem 0 0 0; font-size: 0.9rem;">
#         Ready to innovate with AI? Let's build the future together! 🌟
#     </p>
# </div>
# """, unsafe_allow_html=True)

import streamlit as st
import base64
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="Basit Ali - AI Developer Portfolio",
    page_icon="./images/profile_icon.png",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS with horizontal navigation
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    /* Hide Streamlit's default navigation */
    .stAppHeader {
        display: none;
    }
    
    /* Hide sidebar completely */
    section[data-testid="stSidebar"] {
        display: none !important;
    }
    
    /* Custom Horizontal Navigation Bar */
    /*
    .horizontal-nav {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(15px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 1rem 2rem;
        margin: 1rem auto 2rem auto;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        max-width: 800px;
    }
    */
    
    .nav-container {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 2rem;
    }
    
    
    /* Mobile responsive navigation */
    @media (max-width: 768px) {
        .nav-container {
            gap: 1rem;
        }
    }
    
    /* All your existing styles */
    .main-container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 1rem;
    }
    
    .profile-header {
        display: flex;
        align-items: center;
        gap: 2rem;
        padding: 2rem;
        background: rgba(255, 255, 255, 0.02);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        margin-bottom: 2rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    }
    
    .profile-image {
        width: 400px;
        height: 400px;
        border-radius: 50%;
        background: linear-gradient(135deg, #6366f1, #8b5cf6, #ec4899);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 3rem;
        color: white;
        box-shadow: 0 8px 25px rgba(99, 102, 241, 0.3);
        flex-shrink: 0;
        overflow: hidden;
    }
    
    .profile-image img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        border-radius: 50%;
    }
    
    .profile-info h1 {
        font-size: 4rem;
        font-weight: 800;
        margin: -5rem  0 0.5rem 5rem;
        background: linear-gradient(135deg, #6366f1, #8b5cf6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .profile-info .subtitle {
        font-size: 1.2rem;
        opacity: 0.8;
        margin: -1.25rem 0 1rem 5rem;
        font-weight: 600;
    }
    
    /* Social Icons Styling */
    .social-icons {
        display: flex;
        align-items: center;
        gap: 1rem;
        margin-top: 2rem;
        margin-left: 5rem;
    }

    .social-icon {
        width: 30px;
        height: 30px;
        border-radius: 30%;
        background: rgba(255, 255, 255, 0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        box-shadow: 0 4px 15px rgba(99, 102, 241, 0.2);
    }

    .social-icon:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(99, 102, 241, 0.3);
    }
    .modern-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 16px;
        padding: 1.5rem;
        margin: 1rem 0;
        transition: all 0.3s ease;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
    }
    
    .modern-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.1);
        border-color: rgba(99, 102, 241, 0.3);
    }
    
    .skill-pill {
        display: inline-block;
        background: rgba(99, 102, 241, 0.1);
        border: 1px solid rgba(99, 102, 241, 0.3);
        color: #6366f1;
        padding: 0.4rem 0.8rem;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 500;
        margin: 0.2rem;
        transition: all 0.3s ease;
    }
    
    .skill-pill:hover {
        background: rgba(99, 102, 241, 0.2);
        transform: translateY(-1px);
    }
    
    .project-card {
        background: rgba(255, 255, 255, 0.02);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 16px;
        padding: 1.5rem;
        margin: 1rem 0;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .project-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 3px;
        background: linear-gradient(90deg, #6366f1, #8b5cf6, #ec4899);
        opacity: 0;
        transition: opacity 0.3s ease;
    }
    
    .project-card:hover::before {
        opacity: 1;
    }
    
    .project-card:hover {
        transform: translateY(-3px);
        border-color: rgba(99, 102, 241, 0.3);
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1);
    }
    
    .section-title {
        font-size: 2rem;
        font-weight: 700;
        text-align: center;
        margin: 2rem 0;
        background: linear-gradient(135deg, #6366f1, #8b5cf6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .section-divider {
        width: 100%;
        height: 3px !important;
        background: linear-gradient(90deg, transparent, #6366f1, #8b5cf6, #ec4899, transparent) !important;
        border: none !important;
        margin: 3rem 0 !important;
        border-radius: 2px !important;
        display: block !important;
    }
    
    .stats-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 1rem;
        margin: 2rem 0;
    }
    
    .stat-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 1.5rem;
        text-align: center;
        transition: all 0.3s ease;
    }
    
    .stat-card:hover {
        border-color: rgba(99, 102, 241, 0.4);
        transform: translateY(-2px);
    }
    
    .stat-number {
        font-size: 2rem;
        font-weight: 800;
        color: #6366f1;
        margin: 0;
    }
    
    .stat-label {
        font-size: 0.9rem;
        opacity: 0.7;
        margin: 0.5rem 0 0 0;
        font-weight: 500;
    }
    
    .download-btn {
        background: linear-gradient(135deg, #6366f1, #8b5cf6);
        color: white;
        border: none;
        padding: 1rem 2rem;
        border-radius: 12px;
        font-weight: 600;
        font-size: 1rem;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(99, 102, 241, 0.3);
        text-decoration: none;
        display: inline-block;
    }
    
    .download-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(99, 102, 241, 0.4);
    }
    
    .timeline-item {
        position: relative;
        padding-left: 2rem;
        margin: 2rem 0;
    }
    
    .timeline-item::before {
        content: '';
        position: absolute;
        left: 0;
        top: 0.5rem;
        width: 12px;
        height: 12px;
        background: #6366f1;
        border-radius: 50%;
        box-shadow: 0 0 0 4px rgba(99, 102, 241, 0.2);
    }
    
    .timeline-item::after {
        content: '';
        position: absolute;
        left: 5px;
        top: 1.5rem;
        width: 2px;
        height: calc(100% - 1rem);
        background: rgba(99, 102, 241, 0.2);
    }
    
    .timeline-item:last-child::after {
        display: none;
    }
    
    .contact-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 1rem;
        margin: 2rem 0;
    }
    
    .contact-item {
        background: rgba(255, 255, 255, 0.02);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 1.5rem;
        text-align: center;
        transition: all 0.3s ease;
    }
    
    .contact-item:hover {
        border-color: rgba(99, 102, 241, 0.3);
        transform: translateY(-2px);
    }
    
    .contact-item a {
        color: inherit;
        text-decoration: none;
    }
    
    .contact-item:hover a {
        color: #6366f1;
    }
    
    .contact-icon {
        font-size: 2rem;
        margin-bottom: 1rem;
        color: #6366f1;
    }
            
    .contact-link {
        color: #6366f1;
        text-decoration: none;
        transition: color 0.3s ease;
    }
            
    .contact-link:hover {
        color: #8b5cf6;
        text-decoration: underline;
    }
    
    /* Fix for Experience Page */
    .job-description {
        margin-bottom: 1.5rem;
        line-height: 1.6;
        color: white; /* Match dark theme */
    }

    .achievement-list {
        line-height: 1.8;
        margin-left: 1rem;
    }

    .competency-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 1.5rem;
        margin-top: 1.5rem;
    }

    .competency-grid h4 {
        color: #6366f1;
        margin-bottom: 0.5rem;
    }

    .competency-grid p {
        color: white; /* Match dark theme */
    }
    
    @media (max-width: 768px) {
        .profile-header {
            flex-direction: column;
            text-align: center;
        }
        
        .profile-info h1 {
            font-size: 2rem;
        }
    }
    
    .stButton > button {
        /* Base styles from .nav-item */
        background: rgba(255, 255, 255, 0.02) !important;
        border: 2px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 16px !important;
        padding: 1rem 1.5rem !important;
        cursor: pointer !important;
        transition: all 0.3s ease !important;
        position: relative !important;
        overflow: hidden !important;
        text-decoration: none !important;
        color: white !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        min-width: 120px !important;
        height: 80px !important;
        justify-content: center !important;
        font-size: 1rem !important; /* Match text size */
    }

    /* Pseudo-element animation */
    .stButton > button::before {
        content: '';
        position: absolute !important;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(99, 102, 241, 0.1), transparent) !important;
        transition: left 0.5s ease !important;
    }

    /* Hover effects */
    .stButton > button:hover::before {
        left: 100% !important;
    }

    .stButton > button:hover {
        transform: translateY(-3px) !important;
        border-color: rgba(99, 102, 241, 0.5) !important;
        box-shadow: 0 10px 30px rgba(99, 102, 241, 0.2) !important;
        background: rgba(99, 102, 241, 0.05) !important;
    }

    /* Active state (primary button) */
    .stButton > button[aria-pressed="true"] {
        border-color: #6366f1 !important;
        background: rgba(99, 102, 241, 0.1) !important;
        box-shadow: 0 8px 25px rgba(99, 102, 241, 0.3) !important;
    }
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Utility functions
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

def get_img_as_base64(file_path):
    """Convert image to base64 string"""
    try:
        with open(file_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except FileNotFoundError:
        return None

# Initialize session state for navigation
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'Home'

# Custom Horizontal Navigation using Streamlit buttons
def render_horizontal_nav():
    st.markdown('<div class="horizontal-nav"><div class="nav-container">', unsafe_allow_html=True)
    
    nav_items = [
        {"name": "Home", "icon": "🏠"},
        {"name": "Experience", "icon": "💼"},
        {"name": "Projects", "icon": "🚀"},
        {"name": "Contact", "icon": "📞"}
    ]
    
    cols = st.columns(len(nav_items))
    
    for i, item in enumerate(nav_items):
        with cols[i]:
            if st.button(
                f"{item['icon']}\n{item['name']}", 
                key=f"nav_{item['name']}", 
                use_container_width=True,
                type="primary" if st.session_state.current_page == item['name'] else "secondary"
            ):
                st.session_state.current_page = item['name']
                st.rerun()
    
    st.markdown('</div></div>', unsafe_allow_html=True)

# Render the horizontal navigation
render_horizontal_nav()

# Import and render pages based on current selection
if st.session_state.current_page == "Home":
    from pages import home
    home.show()
elif st.session_state.current_page == "Experience":
    from pages import experience
    experience.show()
elif st.session_state.current_page == "Projects":
    from pages import projects
    projects.show()
elif st.session_state.current_page == "Contact":
    from pages import contact
    contact.show()

# Footer
st.markdown("""
<div style="margin-top: 4rem; padding: 2rem; text-align: center; border-top: 1px solid rgba(255, 255, 255, 0.1);">
    <p style="opacity: 0.7; margin: 0;">
        🚀 Built with Streamlit | © 2025 Basit Ali - AI Developer
    </p>
    <p style="opacity: 0.5; margin: 0.5rem 0 0 0; font-size: 0.9rem;">
        Ready to innovate with AI? Let's build the future together! 🌟
    </p>
</div>
""", unsafe_allow_html=True)