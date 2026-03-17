import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.express as px
import plotly.graph_objects as go
from streamlit_option_menu import option_menu
import base64
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="Niveditha B | Cybersecurity Portfolio",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Function to load and encode image
@st.cache_data
def get_image_base64(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except:
        return None

# Custom CSS for better styling
def load_css():
    st.markdown("""
        <style>
        /* Main container styling */
        .main {
            padding: 0rem 1rem;
        }
        
        /* Gradient text for headers */
        .gradient-text {
            background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 700;
            font-size: 2.5rem;
            margin-bottom: 1rem;
        }
        
        /* Card styling */
        .card {
            background: linear-gradient(145deg, #ffffff 0%, #f8f9fa 100%);
            border-radius: 20px;
            padding: 1.5rem;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            transition: transform 0.3s ease;
            margin-bottom: 1rem;
            border: 1px solid rgba(102, 126, 234, 0.1);
        }
        
        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 40px rgba(102, 126, 234, 0.2);
        }
        
        /* Skill tag styling */
        .skill-tag {
            display: inline-block;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 0.5rem 1rem;
            border-radius: 25px;
            margin: 0.3rem;
            font-size: 0.9rem;
            font-weight: 500;
            box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
            transition: all 0.3s ease;
        }
        
        .skill-tag:hover {
            transform: scale(1.05);
            box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
        }
        
        /* Timeline styling */
        .timeline-item {
            border-left: 3px solid #667eea;
            padding-left: 1.5rem;
            margin-bottom: 2rem;
            position: relative;
        }
        
        .timeline-item::before {
            content: '';
            position: absolute;
            left: -8px;
            top: 0;
            width: 13px;
            height: 13px;
            border-radius: 50%;
            background: #667eea;
            border: 2px solid white;
            box-shadow: 0 0 0 2px #667eea;
        }
        
        /* Profile image styling */
        .profile-image {
            width: 180px;
            height: 180px;
            border-radius: 50%;
            object-fit: cover;
            border: 4px solid white;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            margin: 0 auto 1.5rem auto;
            display: block;
        }
        
        /* Statistic card */
        .stat-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 1.5rem;
            border-radius: 15px;
            text-align: center;
            box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
            margin-bottom: 1rem;
        }
        
        .stat-number {
            font-size: 2.5rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
        }
        
        .stat-label {
            font-size: 1rem;
            opacity: 0.9;
        }
        
        /* Contact button */
        .contact-button {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 0.8rem 2rem;
            border-radius: 50px;
            text-decoration: none;
            font-weight: 600;
            display: inline-block;
            transition: all 0.3s ease;
            border: none;
            cursor: pointer;
            margin: 0.5rem;
        }
        
        .contact-button:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 30px rgba(102, 126, 234, 0.4);
        }
        
        /* Section divider */
        .section-divider {
            height: 3px;
            background: linear-gradient(90deg, #667eea 0%, #764ba2 50%, #667eea 100%);
            margin: 2rem 0;
            border-radius: 3px;
        }
        
        /* Responsive adjustments */
        @media (max-width: 768px) {
            .gradient-text {
                font-size: 2rem;
            }
            .profile-image {
                width: 140px;
                height: 140px;
            }
        }
        </style>
    """, unsafe_allow_html=True)

# Load CSS
load_css()

# Header section with profile
def render_header():
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        # Try to load profile image
        img_base64 = None
        for ext in ['jpg', 'jpeg', 'png', 'gif']:
            img_path = Path(f"profile.{ext}")
            if img_path.exists():
                img_base64 = get_image_base64(img_path)
                break
        
        if img_base64:
            # Display with actual photo
            st.markdown(f"""
                <div style='text-align: center; padding: 2rem 0;'>
                    <img src='data:image/jpeg;base64,{img_base64}' class='profile-image'>
                    <h1 class='gradient-text'>Niveditha B</h1>
                    <p style='font-size: 1.2rem; color: #666; margin-bottom: 1.5rem;'>
                        Cybersecurity Engineer | UI/UX Enthusiast | Digital Forensics Specialist
                    </p>
                    <div style='display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap;'>
                        <a href='mailto:nivedithab8089@gmail.com' class='contact-button'>📧 Email Me</a>
                        <a href='https://linkedin.com/in/niveditha-b-716bbb27b' class='contact-button'>🔗 LinkedIn</a>
                        <a href='https://github.com/NivedithaB34' class='contact-button'>💻 GitHub</a>
                    </div>
                </div>
            """, unsafe_allow_html=True)
        else:
            # Display with emoji if no photo
            st.markdown("""
                <div style='text-align: center; padding: 2rem 0;'>
                    <div style='width: 150px; height: 150px; border-radius: 50%; 
                              background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                              margin: 0 auto 1.5rem auto; display: flex; align-items: center; 
                              justify-content: center; border: 4px solid white; box-shadow: 0 10px 30px rgba(0,0,0,0.2);'>
                        <span style='font-size: 4rem; color: white;'>👩‍💻</span>
                    </div>
                    <h1 class='gradient-text'>Niveditha B</h1>
                    <p style='font-size: 1.2rem; color: #666; margin-bottom: 1.5rem;'>
                        Cybersecurity Engineer | UI/UX Enthusiast | Digital Forensics Specialist
                    </p>
                    <div style='display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap;'>
                        <a href='mailto:nivedithab8089@gmail.com' class='contact-button'>📧 Email Me</a>
                        <a href='https://linkedin.com/in/niveditha-b-716bbb27b' class='contact-button'>🔗 LinkedIn</a>
                        <a href='https://github.com/NivedithaB34' class='contact-button'>💻 GitHub</a>
                    </div>
                </div>
            """, unsafe_allow_html=True)

# Navigation menu
def render_navigation():
    selected = option_menu(
        menu_title=None,
        options=["About", "Skills", "Experience", "Projects", "Certifications", "Contact"],
        icons=["person", "code-slash", "briefcase", "folder", "award", "envelope"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "transparent"},
            "icon": {"color": "#667eea", "font-size": "1.2rem"},
            "nav-link": {
                "font-size": "1rem",
                "text-align": "center",
                "margin": "0px",
                "color": "#666",
                "border-radius": "10px",
                "transition": "all 0.3s ease"
            },
            "nav-link-selected": {
                "background": "linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
                "color": "white"
            },
        }
    )
    return selected

# About section
def render_about():
    st.markdown("<h2 class='gradient-text'>📋 About Me</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
            <div class='card'>
                <p style='font-size: 1.1rem; line-height: 1.8; color: #444;'>
                    I am a Computer Science Engineering student specializing in Cyber Security, with a strong foundation in 
                    network security, cryptography, digital forensics, risk assessment, and cyber defense tools. I have hands-on 
                    experience in PDR/IPDR analysis and a growing interest in UI/UX design, integrating security with usability 
                    in digital systems.
                </p>
                <p style='font-size: 1.1rem; line-height: 1.8; color: #444; margin-top: 1rem;'>
                    With a keen analytical mindset, I am proficient in identifying vulnerabilities and designing secure solutions. 
                    I thrive in collaborative environments and possess excellent communication, problem-solving, and critical 
                    thinking skills.
                </p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        # Quick stats
        st.markdown("""
            <div class='stat-card'>
                <div class='stat-number'>3+</div>
                <div class='stat-label'>Years of Learning</div>
            </div>
            <div class='stat-card'>
                <div class='stat-number'>15+</div>
                <div class='stat-label'>Security Tools</div>
            </div>
            <div class='stat-card'>
                <div class='stat-number'>5+</div>
                <div class='stat-label'>Projects Completed</div>
            </div>
        """, unsafe_allow_html=True)

# Skills section
def render_skills():
    st.markdown("<h2 class='gradient-text'>🛠️ Skills & Expertise</h2>", unsafe_allow_html=True)
    
    # Programming skills with proficiency
    programming_skills = {
        "Python": 85,
        "C": 75,
        "SQL": 80,
        "Java": 70,
        "HTML/CSS": 85,
        "Bash": 65,
        "React": 60
    }
    
    # Create progress bars for programming skills
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 💻 Programming")
        for skill, proficiency in list(programming_skills.items())[:4]:
            st.markdown(f"**{skill}**")
            st.progress(proficiency/100)
    
    with col2:
        st.markdown("### 💻 Programming")
        for skill, proficiency in list(programming_skills.items())[4:]:
            st.markdown(f"**{skill}**")
            st.progress(proficiency/100)
    
    # Security tools as tags
    st.markdown("### 🔧 Security Tools")
    tools = [
        "Wireshark", "Nmap", "Hydra", "Burp Suite", "Metasploit",
        "Autopsy", "FTK Imager", "Hashcat", "John the Ripper",
        "Volatility", "IDA Pro", "Sleuthkit", "Steghide", "Kali Linux"
    ]
    
    tools_html = ""
    for tool in tools:
        tools_html += f"<span class='skill-tag'>{tool}</span>"
    
    st.markdown(f"<div style='margin: 1rem 0;'>{tools_html}</div>", unsafe_allow_html=True)
    
    # Soft skills
    st.markdown("### 🤝 Soft Skills")
    soft_skills = [
        "Leadership", "Communication", "Mentoring", "Problem-solving",
        "Team coordination", "Decision making", "Time management",
        "Adaptability", "Attention to detail"
    ]
    
    soft_skills_html = ""
    for skill in soft_skills:
        soft_skills_html += f"<span class='skill-tag'>{skill}</span>"
    
    st.markdown(f"<div style='margin: 1rem 0;'>{soft_skills_html}</div>", unsafe_allow_html=True)

# Experience section
def render_experience():
    st.markdown("<h2 class='gradient-text'>💼 Experience</h2>", unsafe_allow_html=True)
    
    experiences = [
        {
            "title": "Student Intern - Cyber Crime Police Station",
            "company": "Cyber Crime Police Station, Kottayam",
            "period": "2025",
            "description": [
                "Observed case analysis and digital evidence handling",
                "Applied cyber laws in real-world scenarios",
                "Developed skills in IP tracking and data recovery",
                "Familiarized with CDR/IPDR analysis for investigation"
            ]
        },
        {
            "title": "Intern - PHP & Angular Developer",
            "company": "ShiRah InfoTech Pvt. Ltd.",
            "period": "2025",
            "description": [
                "Developed basic web applications",
                "Improved skills in component-based architecture",
                "Implemented server-side scripting",
                "Integrated client-side and server-side logic"
            ]
        },
        {
            "title": "Designer - Cybersecurity Execom",
            "company": "SJCET",
            "period": "2025",
            "description": [
                "Designed posters and digital content for cybersecurity awareness",
                "Strengthened creative and technical skills",
                "Contributed to cybersecurity culture on campus"
            ]
        },
        {
            "title": "Intern - Cybersecurity",
            "company": "Academor",
            "period": "2025",
            "description": [
                "Analyzed network traffic using Wireshark and Nmap",
                "Identified vulnerabilities in network systems",
                "Implemented cybersecurity tools for network assessment"
            ]
        }
    ]
    
    for exp in experiences:
        desc_html = "".join([f"<li>{item}</li>" for item in exp['description']])
        st.markdown(f"""
            <div class='card'>
                <h3 style='color: #667eea; margin-bottom: 0.5rem;'>{exp['title']}</h3>
                <p style='color: #666; margin-bottom: 0.5rem;'>{exp['company']} | {exp['period']}</p>
                <ul style='color: #444;'>{desc_html}</ul>
            </div>
        """, unsafe_allow_html=True)

# Projects section
def render_projects():
    st.markdown("<h2 class='gradient-text'>🚀 Projects</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
            <div class='card'>
                <h3 style='color: #667eea;'>BlockShare</h3>
                <p style='color: #888; margin-bottom: 1rem;'>Blockchain based File sharing System</p>
                <p style='color: #444;'>Developed an app for secure file sharing using blockchain, AES encryption, 
                and IPFS for decentralized, tamper-proof storage. Implemented user authentication with Supabase 
                and designed a simple interface with Recent Transfers feature.</p>
                <a href='https://github.com/NivedithaB34' style='color: #667eea; text-decoration: none;'>
                    🔗 View on GitHub →
                </a>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div class='card'>
                <h3 style='color: #667eea;'>Bank Management System</h3>
                <p style='color: #888; margin-bottom: 1rem;'>ATM System with Secure Authentication</p>
                <p style='color: #444;'>Developed an ATM system using Java Swing for the user interface and MySQL 
                as the backend database. Implemented secure customer authentication by validating ATM card numbers 
                and PINs through database queries.</p>
                <a href='https://github.com/NivedithaB34' style='color: #667eea; text-decoration: none;'>
                    🔗 View on GitHub →
                </a>
            </div>
        """, unsafe_allow_html=True)

# Certifications section
def render_certifications():
    st.markdown("<h2 class='gradient-text'>📜 Certifications</h2>", unsafe_allow_html=True)
    
    certifications = [
        {"name": "Foundations of Cybersecurity", "provider": "Coursera", "date": "2025"},
        {"name": "Ethical Hacker", "provider": "Cisco Networking Academy", "date": "2025"},
        {"name": "Ethics and Privacy - Digital Forensics", "provider": "Infosys Springboard", "date": "2025"},
        {"name": "Packet Tracer", "provider": "Cisco Networking Academy", "date": "2024"},
        {"name": "Cybersecurity and Privacy", "provider": "NPTEL", "date": "2024"},
        {"name": "Network Analysis using Wireshark 3", "provider": "Infosys Springboard", "date": "2024"}
    ]
    
    # Create a timeline-like display for certifications
    for cert in certifications:
        st.markdown(f"""
            <div class='timeline-item'>
                <h4 style='color: #667eea; margin-bottom: 0.3rem;'>{cert['name']}</h4>
                <p style='color: #666;'>{cert['provider']} | {cert['date']}</p>
            </div>
        """, unsafe_allow_html=True)

# Contact section
def render_contact():
    st.markdown("<h2 class='gradient-text'>📫 Get in Touch</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
            <div class='card'>
                <h3 style='color: #667eea; margin-bottom: 1.5rem;'>Contact Information</h3>
                <p style='margin-bottom: 1rem;'>📍 Kottayam, Kerala</p>
                <p style='margin-bottom: 1rem;'>📧 nivedithab8089@gmail.com</p>
                <p style='margin-bottom: 1rem;'>📱 +91 8089403962</p>
                <div style='margin-top: 2rem;'>
                    <h4 style='color: #667eea; margin-bottom: 1rem;'>Education</h4>
                    <p><strong>B.Tech in Computer Science (Cybersecurity)</strong><br>
                    SJCET, Palai | CGPA: 7.07 | Sept 2022 - May 2026</p>
                    <p><strong>Higher Secondary Education</strong><br>
                    Mount Carmel HSS, Kanjikuzhy | GPA: 8.8</p>
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div class='card'>
                <h3 style='color: #667eea; margin-bottom: 1.5rem;'>Send a Message</h3>
        """, unsafe_allow_html=True)
        
        with st.form("contact_form"):
            name = st.text_input("Name")
            email = st.text_input("Email")
            message = st.text_area("Message", height=150)
            submit = st.form_submit_button("Send Message")
            
            if submit:
                st.success("Thanks for reaching out! I'll get back to you soon.")
        
        st.markdown("</div>", unsafe_allow_html=True)

# Main app
def main():
    # Header
    render_header()
    
    # Navigation
    selected = render_navigation()
    
    # Section divider
    st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)
    
    # Render selected section
    if selected == "About":
        render_about()
    elif selected == "Skills":
        render_skills()
    elif selected == "Experience":
        render_experience()
    elif selected == "Projects":
        render_projects()
    elif selected == "Certifications":
        render_certifications()
    elif selected == "Contact":
        render_contact()
    
    # Footer
    st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)
    st.markdown("""
        <div style='text-align: center; padding: 2rem; color: #666;'>
            <p>© 2025 Niveditha B | Cybersecurity Portfolio</p>
            <p style='font-size: 0.9rem;'>Built with Python and Streamlit</p>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()