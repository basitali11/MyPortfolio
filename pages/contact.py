from email_sender import send_email   
import streamlit as st

def show():
    st.markdown('<h2 class="section-title">Let\'s Connect</h2>', unsafe_allow_html=True)
    
    # Contact Information
    st.markdown("""
    <div class="contact-grid">
        <div class="contact-item">
            <div class="contact-icon">📧</div>
            <h4>Email</h4>
            <p><a href="mailto:basitali171480@gmail.com" class="contact-link">basitali171480@gmail.com</a></p>
        </div>
        <div class="contact-item">
            <div class="contact-icon">📱</div>
            <h4>Phone</h4>
            <p>+92-3219498096</p>
        </div>
        <div class="contact-item">
            <div class="contact-icon">💼</div>
            <h4>LinkedIn</h4>
            <p><a href="https://www.linkedin.com/in/basit-ali11/"  target="_blank" rel="noopener noreferrer" class="contact-link">LinkedIn Profile</a></p>
        </div>
        <div class="contact-item">
            <div class="contact-icon">💻</div>
            <h4>GitHub</h4>
            <p><a href="https://github.com/basitali11"  target="_blank" rel="noopener noreferrer" class="contact-link">GitHub Repository</a></p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Contact Form
    st.markdown("""
    <div class="modern-card">
        <h3>📝 Send a Message</h3>
        <p style="opacity: 0.8; margin-bottom: 1.5rem;">Ready to discuss AI projects and opportunities? Let's connect!</p>
    </div>
    """, unsafe_allow_html=True)
    
    with st.form("contact_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Your Name *")
        with col2:
            email = st.text_input("Your Email *")
        
        subject = st.text_input("Subject *")
        message = st.text_area("Your Message *", height=120)
        
        submitted = st.form_submit_button("Send Message 🚀")
        
        if submitted:
            if name and email and subject and message:
                # Validate email format
                if "@" in email and "." in email:
                    with st.spinner("Sending your message..."):                        
                        if send_email(name, email, subject, message):
                            st.success("🎉 Thank you for your message! I'll get back to you soon.")
                            st.balloons()
                        else:
                            st.error("⚠️ Sorry, there was an error sending your message. Please try again or email me directly at basitali171480@gmail.com")
                else:
                    st.error("⚠️ Please enter a valid email address.")
            else:
                st.error("⚠️ Please fill in all required fields.")