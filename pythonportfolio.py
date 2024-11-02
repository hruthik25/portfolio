import flask
from flask import Flask, render_template, jsonify, request
import plotly
import plotly.express as px
import plotly.graph_objects as go
import plotly.utils
import pandas as pd
import numpy as np
from datetime import datetime
import json
import os

# Print versions
print(f"Flask version: {flask.__version__}")
print(f"Plotly version: {plotly.__version__}")
print(f"Pandas version: {pd.__version__}")
print(f"Numpy version: {np.__version__}")

app = Flask(__name__)

# Updated projects data
projects_data = [
    {
        "title": "Flight Delay Analysis and Prediction",
        "description": "Led a team to develop a predictive model using Databricks, analyzing over 61 million records which improved flight scheduling efficiency and reduced delays by 15%.",
        "metrics": {"Records": "61M+", "Efficiency": "+15%", "Impact": "Flight Scheduling"},
        "technologies": ["Python", "Databricks", "Machine Learning", "Big Data"],
        "github_link": "#"
    },
    {
        "title": "Advanced Health Insurance Analysis Dashboard",
        "description": "Created an Excel-based dashboard that processed $2M+ in claims data, identifying key factors leading to a 10% decrease in claim denials.",
        "metrics": {"Claims Processed": "$2M+", "Denials": "-10%", "Impact": "Healthcare"},
        "technologies": ["Excel", "Data Analysis", "Dashboard Design", "Healthcare Analytics"],
        "github_link": "#"
    },
    {
        "title": "Healthcare Data Analysis Using Power BI",
        "description": "Implemented Power BI dashboards that streamlined data analysis processes, leading to a 20% quicker decision-making for healthcare providers.",
        "metrics": {"Decision Speed": "+20%", "Impact": "Healthcare Providers"},
        "technologies": ["Power BI", "SQL", "Data Visualization", "Healthcare Analytics"],
        "github_link": "#"
    },
    {
        "title": "Medical Chatbot – Llama-2",
        "description": "AI-powered chatbot using Llama-2 and Langchain for processing medical queries and providing accurate responses.",
        "metrics": {"Response Time": "0.5s", "Accuracy": "92%", "Users": "1000+"},
        "technologies": ["Python", "Llama-2", "LangChain", "AI"],
        "github_link": "#"
    }
]

# Experience data
experience_data = [
    {
        "role": "Freelance AI Coder",
        "company": "Outlier",
        "period": "June 2024 - Present",
        "description": "Enhanced AI coding algorithms and optimized large-scale models",
        "achievements": [
            "Improved processing accuracy by 25%",
            "Enhanced efficiency by 30%",
            "Reduced error rates by 15%"
        ]
    },
    {
        "role": "Data Analyst Intern",
        "company": "Orbit Information Systems and Consultants LLC",
        "period": "May 2023 - November 2023",
        "description": "Led SQL and Power BI projects for data transformation",
        "achievements": [
            "Increased report generation speed by 20%",
            "Automated key data processing tasks",
            "Improved operational efficiency by 13%"
        ]
    },
    {
        "role": "Data Analyst Intern",
        "company": "Lasya Infotech",
        "period": "January 2021 - June 2021",
        "description": "Redesigned and secured database systems",
        "achievements": [
            "Reduced data retrieval times by 40%",
            "Improved system response times",
            "Decreased data access time by 50%"
        ]
    }
]

# Updated skills data
skills_data = {
    "Technical": [
        {"name": "Python", "proficiency": 90},
        {"name": "SQL", "proficiency": 85},
        {"name": "Databricks", "proficiency": 80},
        {"name": "Power BI", "proficiency": 90},
        {"name": "Excel", "proficiency": 85},
        {"name": "Machine Learning", "proficiency": 80}
    ],
    "Domain": [
        {"name": "Data Analysis", "proficiency": 90},
        {"name": "Healthcare Analytics", "proficiency": 85},
        {"name": "Big Data", "proficiency": 80},
        {"name": "AI/ML", "proficiency": 85},
        {"name": "Visualization", "proficiency": 90}
    ]
}

@app.route('/')
def home():
    return render_template('index.html',
                         name="Hruthik Vurukonda",
                         title="Data Analyst & AI Specialist",
                         location="Boston, MA",
                         email="hruthik.vurukonda@gmail.com",
                         phone="+1 (774) 271-8616",
                         linkedin="hruthik-vurukonda",
                         about_me="""Experienced Data Analyst and AI Specialist with a Master's in Data Science 
                                   from UMass Dartmouth. Passionate about transforming complex data into actionable 
                                   insights, specializing in healthcare analytics and machine learning solutions. 
                                   Proven track record of processing over 61 million data points and improving 
                                   operational efficiencies across multiple projects.""")

@app.route('/api/projects')
def get_projects():
    return jsonify(projects_data)

@app.route('/api/experience')
def get_experience():
    return jsonify(experience_data)

@app.route('/api/skills')
def get_skills():
    return jsonify(skills_data)

@app.route('/api/skill-chart')
def get_skill_chart():
    try:
        fig = go.Figure()
        
        # Technical Skills
        tech_skills = pd.DataFrame(skills_data["Technical"])
        fig.add_trace(go.Scatterpolar(
            r=tech_skills["proficiency"].tolist(),
            theta=tech_skills["name"].tolist(),
            fill='toself',
            name='Technical',
            line_color='#4F46E5',
            fillcolor='rgba(79, 70, 229, 0.3)'
        ))
        
        # Domain Skills
        domain_skills = pd.DataFrame(skills_data["Domain"])
        fig.add_trace(go.Scatterpolar(
            r=domain_skills["proficiency"].tolist(),
            theta=domain_skills["name"].tolist(),
            fill='toself',
            name='Domain Expertise',
            line_color='#EC4899',
            fillcolor='rgba(236, 72, 153, 0.3)'
        ))
        
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 100],
                    showline=False,
                    color='white'
                ),
                angularaxis=dict(
                    color='white'
                ),
                bgcolor='rgba(0,0,0,0)'
            ),
            showlegend=True,
            legend=dict(
                font=dict(color='white'),
                bgcolor='rgba(0,0,0,0)'
            ),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            margin=dict(l=80, r=80, t=20, b=20)
        )
        
        return json.dumps(fig.to_dict())
    except Exception as e:
        print(f"Error generating chart: {str(e)}")
        return jsonify({"error": str(e)}), 500
# HTML Template with updated styling and About Me section
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ name }} - Portfolio</title>
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        html {
            scroll-behavior: smooth;
        }
        body {
            background: linear-gradient(135deg, #1a237e 0%, #1e3a8a 100%);
            min-height: 100vh;
            color: white;
        }
        .project-card {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border-radius: 16px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            transition: all 0.3s ease;
        }
        .project-card:hover {
            background: rgba(255, 255, 255, 0.15);
            transform: translateY(-2px);
        }
        .metrics-badge {
            background: rgba(79, 70, 229, 0.2);
            border-radius: 9999px;
            padding: 0.25rem 1rem;
            font-size: 0.875rem;
            color: #fff;
            border: 1px solid rgba(79, 70, 229, 0.3);
        }
        .timeline-card {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border-radius: 16px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            transition: all 0.3s ease;
            position: relative;
        }
        .timeline-card:hover {
            background: rgba(255, 255, 255, 0.15);
            transform: translateX(5px);
        }
        .tech-tag {
            background: rgba(59, 130, 246, 0.2);
            border-radius: 9999px;
            padding: 0.25rem 1rem;
            font-size: 0.875rem;
            color: #fff;
            transition: all 0.3s ease;
        }
        .tech-tag:hover {
            background: rgba(59, 130, 246, 0.3);
        }
        .nav-link {
            color: #fff;
            opacity: 0.8;
            transition: all 0.3s ease;
            text-decoration: none;
        }
        .nav-link:hover {
            opacity: 1;
            color: #60A5FA;
        }
        #skills-chart {
            background: rgba(255, 255, 255, 0.05);
            border-radius: 16px;
            padding: 1rem;
        }
        .section-title {
            background: linear-gradient(45deg, #60A5FA, #93C5FD);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: bold;
        }
        .achievement-item {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            padding: 0.25rem 0;
        }
        .achievement-item::before {
            content: "→";
            color: #60A5FA;
        }
        .company-badge {
            background: linear-gradient(135deg, #4F46E5 0%, #60A5FA 100%);
            padding: 0.25rem 1rem;
            border-radius: 9999px;
            font-size: 0.875rem;
            font-weight: 500;
        }
        .hero-stat {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border-radius: 16px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            transition: all 0.3s ease;
        }
        .hero-stat:hover {
            background: rgba(255, 255, 255, 0.15);
            transform: translateY(-2px);
        }
    </style>
</head>
<body class="antialiased">
    <!-- Navigation -->
    <nav class="fixed w-full z-50 px-4 py-4 bg-opacity-90 backdrop-blur-md bg-gray-900">
        <div class="container mx-auto flex justify-between items-center">
            <h1 class="text-2xl font-bold text-blue-400">{{ name }}</h1>
            <div class="space-x-8">
                <a href="#about" class="nav-link">About</a>
                <a href="#projects" class="nav-link">Projects</a>
                <a href="#experience" class="nav-link">Experience</a>
                <a href="#skills" class="nav-link">Skills</a>
                <a href="mailto:{{ email }}" class="nav-link">Contact</a>
            </div>
        </div>
    </nav>

    <!-- Hero Section -->
    <header class="min-h-screen flex items-center px-4" id="about">
        <div class="container mx-auto pt-20">
            <h1 class="text-7xl font-bold mb-6 section-title">{{ name }}</h1>
            <p class="text-3xl text-gray-300 mb-8">{{ title }}</p>
            
            <div class="max-w-3xl">
                <p class="text-xl text-gray-300 leading-relaxed mb-8">
                    {{ about_me }}
                </p>
                
                <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
                    <div class="hero-stat p-4">
                        <h3 class="font-bold text-blue-400">Education</h3>
                        <p class="text-sm">Master's in Data Science</p>
                        <p class="text-xs text-gray-400">UMass Dartmouth</p>
                    </div>
                    <div class="hero-stat p-4">
                        <h3 class="font-bold text-blue-400">Expertise</h3>
                        <p class="text-sm">Healthcare & Aviation Analytics</p>
                        <p class="text-xs text-gray-400">Data Science | AI</p>
                    </div>
                    <div class="hero-stat p-4">
                        <h3 class="font-bold text-blue-400">Location</h3>
                        <p class="text-sm">{{ location }}</p>
                        <p class="text-xs text-gray-400">Available for Remote Work</p>
                    </div>
                </div>

                <div class="flex gap-4">
                    <a href="#projects" 
                       class="px-6 py-3 bg-gradient-to-r from-blue-600 to-blue-400 rounded-full 
                              hover:from-blue-500 hover:to-blue-300 transition-all duration-300 
                              font-semibold text-white">
                        View Projects
                    </a>
                    <a href="mailto:{{ email }}" 
                       class="px-6 py-3 border border-blue-400 rounded-full 
                              hover:bg-blue-400/20 transition-all duration-300 
                              font-semibold text-white">
                        Get in Touch
                    </a>
                </div>
            </div>
        </div>
    </header>

    <!-- Projects Section -->
    <section class="py-20 px-4" id="projects">
        <div class="container mx-auto">
            <h2 class="text-4xl font-bold mb-12 section-title">Projects</h2>
            <div class="grid md:grid-cols-2 gap-8" id="projects-container"></div>
        </div>
    </section>

    <!-- Experience Section -->
    <section class="py-20 px-4" id="experience">
        <div class="container mx-auto">
            <h2 class="text-4xl font-bold mb-12 section-title">Experience</h2>
            <div class="space-y-6" id="experience-container"></div>
        </div>
    </section>

    <!-- Skills Section -->
    <section class="py-20 px-4" id="skills">
        <div class="container mx-auto">
            <h2 class="text-4xl font-bold mb-12 section-title">Skills</h2>
            <div id="skills-chart" class="w-full h-[600px]"></div>
        </div>
    </section>

    <script>
        // Load Projects
        fetch('/api/projects')
            .then(response => response.json())
            .then(projects => {
                const projectsContainer = document.getElementById('projects-container');
                projects.forEach(project => {
                    const projectElement = document.createElement('div');
                    projectElement.className = 'project-card p-6';
                    projectElement.innerHTML = `
                        <h3 class="text-xl font-bold mb-3">${project.title}</h3>
                        <p class="text-gray-300 mb-4">${project.description}</p>
                        <div class="flex flex-wrap gap-2 mb-4">
                            ${Object.entries(project.metrics).map(([key, value]) => 
                                `<span class="metrics-badge">${key}: ${value}</span>`
                            ).join('')}
                        </div>
                        <div class="flex flex-wrap gap-2">
                            ${project.technologies.map(tech => 
                                `<span class="tech-tag">${tech}</span>`
                            ).join('')}
                        </div>
                    `;
                    projectsContainer.appendChild(projectElement);
                });
            });

        // Load Experience
        fetch('/api/experience')
            .then(response => response.json())
            .then(experiences => {
                const experienceContainer = document.getElementById('experience-container');
                experiences.forEach(exp => {
                    const expElement = document.createElement('div');
                    expElement.className = 'timeline-card p-6';
                    expElement.innerHTML = `
                        <div class="flex flex-col md:flex-row md:justify-between md:items-start mb-4">
                            <div>
                                <h3 class="text-xl font-bold mb-2">${exp.role}</h3>
                                <span class="company-badge mb-2 inline-block">${exp.company}</span>
                            </div>
                            <span class="text-gray-400 md:text-right">${exp.period}</span>
                        </div>
                        <p class="text-gray-300 mb-4">${exp.description}</p>
                        <div class="space-y-2">
                            ${exp.achievements.map(achievement => `
                                <div class="achievement-item">
                                    <span>${achievement}</span>
                                </div>
                            `).join('')}
                        </div>
                    `;
                    experienceContainer.appendChild(expElement);
                });
            });

        // Load Skills Chart
        fetch('/api/skill-chart')
            .then(response => response.json())
            .then(chartData => {
                Plotly.newPlot('skills-chart', chartData.data, {
                    ...chartData.layout,
                    paper_bgcolor: 'rgba(0,0,0,0)',
                    plot_bgcolor: 'rgba(0,0,0,0)',
                    font: { color: '#fff' }
                });
            });
    </script>
</body>
</html>
"""

# Create templates directory and save the template
if not os.path.exists('templates'):
    os.makedirs('templates')

template_path = os.path.join('templates', 'index.html')
with open(template_path, 'w') as f:
    f.write(html_content)

if __name__ == '__main__':
    print("Starting Flask application...")
    app.run(debug=True, port=5000)