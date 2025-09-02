# SDG AI Companion – Prompt Engineering Showcase

This project uses OpenAI to generate actionable solutions for **SDG 2, SDG 3, and SDG 4**.  
The following document shows the **prompt engineering process** from initial ideas to refined prompts and final outputs.

---

## **Prompt Engineering Workflow**

### **1. SDG 2 – Zero Hunger**
| Step | Prompt | Notes / Refinement |
|------|--------|------------------|
| Initial | Provide ways to reduce hunger in rural areas. | Too general; AI may give vague suggestions. |
| Refined | Suggest practical strategies using sustainable agriculture, community gardens, and local resources. | Added actionable elements and focus areas. |
| Final | Suggest three practical strategies to reduce hunger in rural African communities. Include sustainable farming and community involvement. | Concise, specific, and actionable. |
| Example AI Response | 1. Community-run vegetable gardens.<br>2. Training in sustainable farming.<br>3. Local food-sharing initiatives. |

---

### **2. SDG 3 – Good Health & Well-Being**
| Step | Prompt | Notes / Refinement |
|------|--------|------------------|
| Initial | Suggest ways to improve community healthcare in low-income regions. | Too broad; may miss preventive/digital health focus. |
| Refined | Include preventive care and digital solutions in the strategies. | Guides AI to focus on innovative methods. |
| Final | Provide practical methods to improve community health in low-income areas, including preventive care and digital tools. | Clear, focused, and actionable. |
| Example AI Response | 1. Mobile health clinics with telemedicine.<br>2. Health education workshops.<br>3. Digital tracking of vaccinations and check-ups. |

---

### **3. SDG 4 – Quality Education**
| Step | Prompt | Notes / Refinement |
|------|--------|------------------|
| Initial | Suggest ways to improve education quality for rural students. | Too general; lacks low-cost or community focus. |
| Refined | Focus on low-cost digital solutions and community-driven strategies. | Encourages practical AI responses. |
| Final | Provide actionable strategies to improve rural education, focusing on low-cost digital learning and community support. | Clear, specific, and feasible. |
| Example AI Response | 1. Community computer labs with shared devices.<br>2. Teacher training programs with online resources.<br>3. Peer-to-peer learning groups. |

---

## **Key Notes on Prompt Engineering**
- **Clarity:** Make prompts concise and specific.
- **Context:** Add location, community, or resource constraints.
- **Actionable Focus:** Ask for concrete solutions or steps.
- **Refinement:** Test prompts iteratively with AI and adjust wording.

---

## **Project Links**
- **Frontend:** `index.html` in `templates/`
- **Backend:** `app.py` (Flask + OpenAI)
- **Database:** `sdg_ai.prompts` (stores user input and AI responses)

---

## **Usage**
1. Select SDG from the dropdown.
2. Enter a prompt or use the provided examples.
3. Click **Get AI Suggestion**.
4. AI output is displayed and saved in MySQL for tracking.

---

## **Conclusion**
This README highlights how **prompt engineering is a critical part of AI projects**. Properly crafted prompts ensure outputs are:
- Specific and actionable.
- Relevant to the chosen SDG.
- High-quality and useful for real-world applications.


# AI Suggestion Platform with IntaSend Payments

A Flask-based web app that allows users to get AI-powered suggestions and purchase credits via IntaSend payment integration.

---

## Features
- AI suggestions via OpenAI GPT model.
- Credit system for controlling usage.
- Paystack payment
- MySQL database to track users and credits.
- Frontend built with HTML, CSS, and JavaScript.

---
