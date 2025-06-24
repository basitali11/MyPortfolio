import streamlit as st

def show():
    st.markdown('<h2 class="section-title">Professional Experience</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="timeline-item">
        <div class="modern-card">
            <h3 style="color: #6366f1;">🏢 AI Developer</h3>
            <h4 style="opacity: 0.8; margin: 0.5rem 0;">NOBORDER.z INNOVATIONS, Lahore</h4>
            <p style="color: #6366f1; font-weight: 600; margin-bottom: 1rem;">October 2023 - Present</p>
            <p style="margin-bottom: 1.5rem; line-height: 1.6;">
                Leading AI development initiatives with focus on conversational AI, computer vision, and generative AI solutions. 
                Responsible for developing sophisticated AI-driven systems and implementing cutting-edge NLP technologies.
            </p>
            <h4 style="margin-bottom: 1rem;">🎯 Key Achievements:</h4>
            <ul style="line-height: 1.8; margin-left: 1rem;">
                <li>Developed personality-driven conversational AI using state-of-the-art LLMs</li>
                <li>Implemented advanced facial feature detection with OpenAI Vision</li>
                <li>Created AI-powered image and video generation systems for marketing</li>
                <li>Built automated ComfyUI workflows for video transformation</li>
                <li>Designed real-time face recognition attendance systems</li>
                <li>Engineered sentiment analysis pipelines with hybrid architectures</li>
                <li>Optimized model performance using Groq for real-time processing</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Professional Competencies
    st.markdown("""
    <div class="modern-card">
        <h3>🎯 Professional Competencies</h3>
        <div style="margin-top: 1.5rem;">
            <div style="margin-bottom: 1.5rem;">
                <h4 style="color: #6366f1; margin-bottom: 0.5rem;">Advanced AI System Development</h4>
                <p>Proficient in designing and deploying sophisticated AI-driven systems with proven track record in AI chatbot development using OpenAI frameworks.</p>
            </div>
            <div style="margin-bottom: 1.5rem;">
                <h4 style="color: #6366f1; margin-bottom: 0.5rem;">Natural Language Processing Excellence</h4>
                <p>Strong proficiency in NLP, sentiment analysis, language understanding, and automated content generation with emotion classification expertise.</p>
            </div>
            <div>
                <h4 style="color: #6366f1; margin-bottom: 0.5rem;">Innovative Technical Integration</h4>
                <p>Renowned for seamlessly integrating AI technologies to deliver superior functionality, including expertise in image and video generation.</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)