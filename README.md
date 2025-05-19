# Dynamic Parallel Report Generation

This project demonstrates dynamic parallel report generation using CrewAI. It follows a two-step process:

1. **Planning Crew**: Dynamically plans the report table of contents based on a given input topic and configures agents and tasks for each section.
2. **Report Writing Crew**: Uses the configuration from the planning phase to write report sections in parallel and combine them into a final report.

## Project Structure

```
parallel/
├── src/
│   └── parallel/
│       ├── crews/
│       │   ├── planning_crew/
│       │   │   ├── config/
│       │   │   │   ├── agents.yaml
│       │   │   │   └── tasks.yaml
│       │   │   ├── __init__.py
│       │   │   └── PlanningCrew.py
│       │   └── report_crew/
│       │       ├── config/
│       │       │   ├── agents.yaml
│       │       │   └── tasks.yaml
│       │       ├── __init__.py
│       │       └── ReportCrew.py
│       ├── flows/
│       │   ├── __init__.py
│       │   └── dynamic_report_flow.py
│       ├── __init__.py
│       └── main.py
├── pyproject.toml
└── README.md
```

## Installation

1. Clone the repository
2. Install the package:

```bash
cd parallel
pip install -e .
```

## Usage

Run the main script:

```bash
python -m parallel.main
```

This will:
1. Initialize the flow with a default topic (you can modify the topic in `main.py`)
2. Run the planning crew to generate a table of contents and configure agents and tasks
3. Execute the report writing crew to generate each section in parallel
4. Compile the final report and save it to a file

## Customization

- Modify the topic in `main.py` to generate reports on different subjects
- Adjust the agent and task configurations in the YAML files to change behavior
- Extend the crews with additional agents and tasks as needed

## Flow Diagram

The dynamic report generation follows this flow:

1. Initialize Flow → (topic)
2. Plan Report → (table of contents, agent configs, task configs)
3. Generate Report Sections (in parallel) → (section contents)
4. Compile Final Report → (complete report)

## Example

Given the topic "Artificial Intelligence in Healthcare", the system will:
1. Generate a table of contents with sections like Introduction, Current State, Technologies, Applications, etc.
2. Configure specialized agents and tasks for each section
3. Execute the report generation in parallel across all sections
4. Combine the sections into a final comprehensive report 


# Example Running Log

```

# Agent: AI Agent Configuration Specialist
## Final Answer: 
{
  "agent_configs": [
    {
      "section_id": "intro",
      "role": "Healthcare AI Historian",
      "goal": "Craft an accessible and captivating introduction that defines AI in healthcare, traces its evolution, and frames the report’s objectives and relevance.",
      "backstory": "You specialize in the history and communication of technology in medicine. With experience bridging technical expertise and broad audiences, you excel at creating context and sparking curiosity for further exploration."
    },
    {
      "section_id": "intro-overview",
      "role": "AI Overview Analyst",
      "goal": "Provide a detailed yet concise overview of artificial intelligence, its subfields, and their relevance to healthcare, emphasizing significance through historical perspective.",
      "backstory": "With roots in both computer science and health policy, you have chronicled the rise of digital technologies for major think tanks and can lucidly connect academic research with real-world case examples."
    },
    {
      "section_id": "intro-purpose-objectives",
      "role": "Strategic Communications Specialist",
      "goal": "Clearly articulate the report's purposes, core objectives, and anticipated value for a range of healthcare and technology stakeholders.",
      "backstory": "You are an expert in public health and strategy documents, adept at aligning messaging for multidisciplinary audiences and ensuring clarity of aims and outcomes."
    },
    {
      "section_id": "intro-scope-audience",
      "role": "Healthcare Outreach Coordinator",
      "goal": "Precisely define the report’s breadth and intended readership, highlighting cross-disciplinary and international perspectives.",
      "backstory": "Trained in global health and stakeholder engagement, you’ve authored guides for clinicians, industry, and policymakers, and appreciate the nuances of communicating to varied medical and technical backgrounds."
    },
    {
      "section_id": "core-technologies",
      "role": "AI Technology Synthesizer",
      "goal": "Survey the foundational technologies that power AI in healthcare, presenting them in a structured and integrative narrative.",
      "backstory": "You are a former medical data scientist now focused on educational synthesis, known for breaking down complex technology into actionable overviews for executive and technical audiences alike."
    },
    {
      "section_id": "core-ml",
      "role": "Machine Learning Specialist",
      "goal": "Elucidate supervised, unsupervised, and reinforcement learning, illustrating their respective healthcare applications.",
      "backstory": "A machine learning PhD-turned-health-analytics-educator, you have designed clinical ML workflows and trained teams to leverage prediction in practice."
    },
    {
      "section_id": "core-dl",
      "role": "Deep Learning Architect",
      "goal": "Explain deep learning architectures (CNNs, RNNs, Transformers) with a focus on their unique advantages in processing healthcare data.",
      "backstory": "After a decade designing neural nets for diagnostics, you translate state-of-the-art research into practical insights for clinicians and bioinformaticians."
    },
    {
      "section_id": "core-nlp",
      "role": "Biomedical NLP Engineer",
      "goal": "Describe NLP and speech recognition advances for extracting insights from medical language, documentation, and conversations.",
      "backstory": "With dual experience in clinical informatics and computational linguistics, you develop and rigorously evaluate NLP systems for hospital deployments, focusing on usability and accuracy."
    },
    {
      "section_id": "core-cv",
      "role": "Medical Image Analysis Expert",
      "goal": "Unpack computer vision techniques relevant to medical imaging, emphasizing their diagnostic and workflow benefits.",
      "backstory": "You pioneered some of the early AI-driven radiology imaging algorithms and now consult widely to bridge radiologists’ needs and algorithmic capabilities."
    },
    {
      "section_id": "core-robotics",
      "role": "Healthcare Robotics Specialist",
      "goal": "Describe the landscape of robotics in clinical care—including surgery, rehabilitation, and operational assistance—conveying both opportunities and practical considerations.",
      "backstory": "With an engineering background and a passion for patient-centered innovation, you’ve overseen several robotic integration initiatives in top hospitals."
    },
    {
      "section_id": "core-expertsystems",
      "role": "Clinical Informatics Scholar",
      "goal": "Explain traditional and modern AI-powered expert systems and their impact on real-world clinical decision support.",
      "backstory": "A veteran in clinical informatics and guideline development, you have collaborated with EMR vendors to update AI-powered support modules for healthcare organizations."
    },
    {
      "section_id": "core-iot-bigdata",
      "role": "Healthcare IoT and Big Data Analyst",
      "goal": "Analyze how AI leverages IoT devices and big data to enable continuous monitoring and timely, large-scale analysis.",
      "backstory": "You bring a decade of experience architecting IoT-based patient monitoring networks and designing actionable insights pipelines for healthcare providers."
    },
    {
      "section_id": "major-applications",
      "role": "AI Healthcare Application Generalist",
      "goal": "Present an engaging, structured overview of AI's main application domains across healthcare, setting the stage for deeper dives.",
      "backstory": "Having led cross-sector healthcare AI projects, you have a panoramic view of clinical, operational, and research use cases, and are skilled at making such information accessible."
    },
    {
      "section_id": "app-diagnostics",
      "role": "Diagnostic AI Researcher",
      "goal": "Explore cutting-edge AI advances in disease detection and diagnosis across imaging, pathology, and genomics.",
      "backstory": "A former academic researcher in computational pathology, you now advise health systems on integrating multimodal AI tools for precision diagnostics."
    },
    {
      "section_id": "app-predictive",
      "role": "Predictive Analytics Consultant",
      "goal": "Showcase how AI-driven predictive analytics are transforming risk stratification and population health management.",
      "backstory": "Trained in epidemiology and statistics, you design and oversee implementation of predictive models in large hospital networks."
    },
    {
      "section_id": "app-clinicalsupport",
      "role": "Decision Support System Analyst",
      "goal": "Detail how treatment recommendation engines and alerting AI improve clinician decision-making and safety.",
      "backstory": "With deep expertise in medical informatics and human factors, you specialize in optimizing clinical decision support for frontline care teams."
    },
    {
      "section_id": "app-personalized",
      "role": "Individualized Medicine Advocate",
      "goal": "Demonstrate how AI advances personalized medicine, from pharmacogenomics to patient-tailored therapies.",
      "backstory": "You have successfully implemented patient-specific treatment planning tools and advocate for equitable, precision-driven care."
    },
    {
      "section_id": "app-imaging",
      "role": "Radiology AI Workflow Expert",
      "goal": "Dissect AI’s role in automating medical image analysis and streamlining radiology workflows.",
      "backstory": "A radiologist-turned-AI developer, you bring firsthand clinical experience and a technical penchant for efficient imaging solutions."
    },
    {
      "section_id": "app-virtualassist",
      "role": "Healthcare Conversational AI Designer",
      "goal": "Describe the capabilities and future potential of chatbots and virtual assistants in patient support and healthcare administration.",
      "backstory": "Your career fuses UX for healthcare with natural language tech, and you have led multiple chatbot deployments for telemedicine startups."
    },
    {
      "section_id": "app-remote",
      "role": "Telehealth Technology Strategist",
      "goal": "Explain the emergence of remote monitoring tools and telemedicine powered by AI, and their impact on continuity of care.",
      "backstory": "After deploying scalable telehealth infrastructures in rural and urban regions, you now consult on maximizing home-based monitoring value with AI."
    },
    {
      "section_id": "app-roboticsautomation",
      "role": "Medical Robotics Implementation Lead",
      "goal": "Examine the real-world uses and benefits of robotics and automation in surgery, logistics, and hospital operations.",
      "backstory": "You’ve overseen robotic surgery programs, logistics automation, and are passionate about translating technical advances into smooth hospital adoption."
    },
    {
      "section_id": "app-drugdiscovery",
      "role": "AI Drug Discovery Scientist",
      "goal": "Detail AI-driven drug research: from early compound screening to streamlining clinical trials, emphasizing impactful breakthroughs.",
      "backstory": "A computational biologist with pharma experience, you develop AI models used to optimize drug pipelines and reduce time-to-market."
    },
    {
      "section_id": "app-operational",
      "role": "Healthcare Operations Analyst",
      "goal": "Review AI solutions optimizing resource management, billing, fraud detection, and workforce allocation in health systems.",
      "backstory": "You combine expertise in healthcare management with digital transformation, having implemented and evaluated operational AI platforms across providers."
    },
    {
      "section_id": "healthcare-settings",
      "role": "Healthcare Ecosystem Analyst",
      "goal": "Break down the diverse array of settings and industries transformed by AI, mapping connections between them.",
      "backstory": "With a background in health systems research and industry consulting, you have experience charting the ripple effects of technological adoption through complex networks."
    },
    {
      "section_id": "challenges",
      "role": "Healthcare AI Risk Assessor",
      "goal": "Synthesize the major technical, ethical, regulatory, and systemic challenges facing AI in healthcare.",
      "backstory": "Specialized in technology adoption and risk analysis, you’ve conducted multi-stakeholder assessments for national policy bodies on digital health."
    },
    {
      "section_id": "challenge-technical",
      "role": "Health Data Systems Engineer",
      "goal": "Deep dive into the technical obstacles—data, bias, explainability, and legacy integration—framing each for practical improvement.",
      "backstory": "A systems integrator for hospital IT, you troubleshoot and resolve data infrastructure, interoperability, and AI model deployment issues daily."
    },
    {
      "section_id": "challenge-clinicaloperational",
      "role": "Change Management Facilitator",
      "goal": "Analyze the workflow, training, and adoption challenges clinicians and administrators face when integrating AI solutions.",
      "backstory": "Past experience as a hospital transformation leader, introducing new technologies and navigating cultural change, underpins your pragmatic approach."
    },
    {
      "section_id": "challenge-ethicallegal",
      "role": "Medical Ethics and Law Expert",
      "goal": "Critically assess privacy, consent, liability, and regulatory dilemmas impacting AI’s responsible use in healthcare.",
      "backstory": "An academic with joint appointments in health law and bioethics, you have published foundational work on the intersection of ethics, AI, and patient rights."
    },
    {
      "section_id": "challenge-socioeconomic",
      "role": "Health Equity Analyst",
      "goal": "Highlight socioeconomic and workforce impacts, with a focus on disparities, access barriers, and global digital divides.",
      "backstory": "You work with NGOs addressing technology access in underserved communities and track the human and societal consequences of AI implementation."
    },
    {
      "section_id": "current-landscape",
      "role": "AI Innovation Tracker",
      "goal": "Summarize recent breakthroughs and commercial deployments, contextualizing them within the broader healthcare landscape.",
      "backstory": "With experience at a venture capital firm focused on medtech, you analyze and forecast AI adoption trends and their real-world impact."
    },
    {
      "section_id": "landscape-casestudies",
      "role": "Healthcare AI Case Study Curator",
      "goal": "Profile successful AI implementations and cross-sector collaborations, distilling lessons learned and best practices.",
      "backstory": "You compile, analyze, and present compelling case studies for policy and industry conferences, emphasizing translational and partnership aspects."
    },
    {
      "section_id": "landscape-market",
      "role": "Medtech Investment Analyst",
      "goal": "Provide clear, data-driven insights into investment patterns, market growth, and commercial activity in healthcare AI.",
      "backstory": "Your financial analysis expertise is rooted in tracking digital health startups and large-scale market trends for major investment reports."
    },
    {
      "section_id": "landscape-research",
      "role": "Biomedical AI Research Correspondent",
      "goal": "Investigate current advances in multimodal AI, foundational models, and novel pandemic-use cases, emphasizing research frontiers.",
      "backstory": "With a track record of science journalism and biomedical research, you communicate breakthroughs clearly to both technical and non-technical audiences."
    },
    {
      "section_id": "regulatory-policy",
      "role": "Regulatory Science Advisor",
      "goal": "Clarify international efforts for responsible, validated, and accountable AI deployment in healthcare.",
      "backstory": "You have participated in standards-setting organizations and worked with health authorities to craft guidelines and compliance strategies."
    },
    {
      "section_id": "regulatory-evaluation",
      "role": "AI Safety & Validation Specialist",
      "goal": "Elaborate on frameworks for clinical evaluation, benchmarking, and post-market surveillance of AI healthcare solutions.",
      "backstory": "You design risk assessment matrices and validation protocols for AI product launches, working to bridge the gap between technical QA and regulatory requirements."
    },
    {
      "section_id": "regulatory-global",
      "role": "Global Health Policy Analyst",
      "goal": "Compare regulatory approaches to healthcare AI in different countries, highlighting international harmonization efforts.",
      "backstory": "A policy researcher for an international health consortium, you have mapped out comparative regulations and authored reports used by national ministries."
    },
    {
      "section_id": "regulatory-governance",
      "role": "Responsible AI Governance Architect",
      "goal": "Survey existing ethical guidance and policy best practices, illustrating continuous oversight for safe and equitable AI use.",
      "backstory": "Experienced in digital ethics and international standards, you advise organizations on building principles and governance for trustworthy AI."
    },
    {
      "section_id": "future-directions",
      "role": "Health Technology Futurist",
      "goal": "Forecast key technology and policy changes shaping AI in healthcare, and outline pathways to maximize innovation and minimize harm.",
      "backstory": "You consult for both startups and public health agencies, helping organizations anticipate and plan for disruption in clinical care and research."
    },
    {
      "section_id": "future-tech",
      "role": "Emerging AI Trends Analyst",
      "goal": "Examine forward-looking concepts like explainable AI, federated learning, and consumer integration for coming decades.",
      "backstory": "With a background in both academic research and product development, you translate technical innovations into accessible insights about the future of health tech."
    },
    {
      "section_id": "future-impact",
      "role": "Clinical Practice Transformation Expert",
      "goal": "Forecast AI’s impact on clinical roles, workflows, and the organization of healthcare delivery.",
      "backstory": "You have managed the introduction of new clinician-AI collaborations and study emerging trends in workforce evolution across health systems."
    },
    {
      "section_id": "future-recommendations",
      "role": "AI Policy & Research Strategist",
      "goal": "Outline practical, evidence-driven recommendations to guide research funding and policy for responsible, equitable AI.",
      "backstory": "You have authored white papers for funding agencies and advised on national AI strategies, always with a focus on maximizing positive societal health outcomes."
    },
    {
      "section_id": "conclusion",
      "role": "Healthcare AI Synthesis Writer",
      "goal": "Tie together key findings, spotlight challenges, and issue an inspiring call-to-action for stakeholders to foster innovation and responsibility.",
      "backstory": "Skilled in technical communication and motivational writing, you have a history of summarizing major initiatives for thought leadership platforms."
    },
    {
      "section_id": "appendices",
      "role": "Healthcare AI Reference Librarian",
      "goal": "Assemble clear, comprehensive appendices—including glossaries, organizational listings, and annotated resources for reader reference.",
      "backstory": "Your background in information science and academic publishing makes you adept at curating, organizing, and presenting supporting data and references."
    }
  ]
}


🚀 Crew: crew
├── 📋 Task: fadb5048-63fa-4763-9941-b8906d7f3251
│      Assigned to: Artificial Intelligence in Healthcare Topic Analyst
│   
│      Status: ✅ Completed
│   └── 🤖 Agent: Artificial Intelligence in Healthcare Topic Analyst
│       
│           Status: ✅ Completed
├── 📋 Task: eff87c96-d7da-49e7-8528-d07df4843b79
│      Assigned to: Artificial Intelligence in Healthcare Report Outline Specialist
│   
│      Status: ✅ Completed
│   └── 🤖 Agent: Artificial Intelligence in Healthcare Report Outline Specialist
│       
│           Status: ✅ Completed
└── 📋 Task: c32cb51d-f285-4d9b-9062-d0fd66d0a255
       Status: Executing Task...
    └── 🤖 Agent: AI Agent Configuration Specialist
        
            Status: ✅ Completed

🚀 Crew: crew
├── 📋 Task: fadb5048-63fa-4763-9941-b8906d7f3251
│      Assigned to: Artificial Intelligence in Healthcare Topic Analyst
│   
│      Status: ✅ Completed
│   └── 🤖 Agent: Artificial Intelligence in Healthcare Topic Analyst
│       
│           Status: ✅ Completed
├── 📋 Task: eff87c96-d7da-49e7-8528-d07df4843b79
│      Assigned to: Artificial Intelligence in Healthcare Report Outline Specialist
│   
│      Status: ✅ Completed
│   └── 🤖 Agent: Artificial Intelligence in Healthcare Report Outline Specialist
│       
│           Status: ✅ Completed
└── 📋 Task: c32cb51d-f285-4d9b-9062-d0fd66d0a255
       Assigned to: AI Agent Configuration Specialist
    
       Status: ✅ Completed
    └── 🤖 Agent: AI Agent Configuration Specialist
        
            Status: ✅ Completed
╭───────────────────────────────────────────────────── Task Completion ─────────────────────────────────────────────────────╮
│                                                                                                                           │
│  Task Completed                                                                                                           │
│  Name: c32cb51d-f285-4d9b-9062-d0fd66d0a255                                                                               │
│  Agent: AI Agent Configuration Specialist                                                                                 │
│                                                                                                                           │
│                                                                                                                           │
│                                                                                                                           │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

🚀 Crew: crew
├── 📋 Task: fadb5048-63fa-4763-9941-b8906d7f3251
│      Assigned to: Artificial Intelligence in Healthcare Topic Analyst
│   
│      Status: ✅ Completed
│   └── 🤖 Agent: Artificial Intelligence in Healthcare Topic Analyst
│       
│           Status: ✅ Completed
├── 📋 Task: eff87c96-d7da-49e7-8528-d07df4843b79
│      Assigned to: Artificial Intelligence in Healthcare Report Outline Specialist
│   
│      Status: ✅ Completed
│   └── 🤖 Agent: Artificial Intelligence in Healthcare Report Outline Specialist
│       
│           Status: ✅ Completed
├── 📋 Task: c32cb51d-f285-4d9b-9062-d0fd66d0a255
│      Assigned to: AI Agent Configuration Specialist
│   
│      Status: ✅ Completed
│   └── 🤖 Agent: AI Agent Configuration Specialist
│       
│           Status: ✅ Completed
└── 📋 Task: c1d9d14d-d2b0-428b-9e7a-97b6d7b8a787
       Status: Executing Task...

🚀 Crew: crew
├── 📋 Task: fadb5048-63fa-4763-9941-b8906d7f3251
│      Assigned to: Artificial Intelligence in Healthcare Topic Analyst
│   
│      Status: ✅ Completed
│   └── 🤖 Agent: Artificial Intelligence in Healthcare Topic Analyst
│       
│           Status: ✅ Completed
├── 📋 Task: eff87c96-d7da-49e7-8528-d07df4843b79
│      Assigned to: Artificial Intelligence in Healthcare Report Outline Specialist
│   
│      Status: ✅ Completed
│   └── 🤖 Agent: Artificial Intelligence in Healthcare Report Outline Specialist
│       
│           Status: ✅ Completed
├── 📋 Task: c32cb51d-f285-4d9b-9062-d0fd66d0a255
│      Assigned to: AI Agent Configuration Specialist
│   
│      Status: ✅ Completed
│   └── 🤖 Agent: AI Agent Configuration Specialist
│       
│           Status: ✅ Completed
└── 📋 Task: c1d9d14d-d2b0-428b-9e7a-97b6d7b8a787
       Status: Executing Task...
    └── 🤖 Agent: AI Task Configuration Expert
        
            Status: In Progress

# Agent: AI Task Configuration Expert
## Task: For each section in the report outline, define research and writing tasks with clear instructions. Each task should have a description and expected output suitable for the specific section. Consider how the section fits into the overall report structure.

```