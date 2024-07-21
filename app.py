import streamlit as st
import google.generativeai as palm

# Configure the API with your API key
palm.configure(api_key="AIzaSyBCrrtj3spZUg98MiLpY3hZzcehchSoY94")

# Define the model to use
model = "models/text-bison-001"

# Create A Function To Generate Feedback
def generate_feedback(project_description, project_scenarios, project_code):
    """Generates feedback on a given text using the PaLM API."""
    prompt = f"Project Description:\n{project_description}\nProject Scenarios:\n{project_scenarios}\nProject Code:\n{project_code}\n\nProvide detailed feedback on the project description, scenarios, and code."
    # Call the generative AI model
    response = palm.generate_text(
        model=model,
        prompt=prompt,
        temperature=0.89,
        top_k=50,
        top_p=0.95,
        max_output_tokens=500,
    )
    return response.result

# Create a function to generate a cover letter
def generate_cover_letter(company_name, job_title):
    """Generates a cover letter for a given company and job title using the PaLM API."""
    prompt = f"Write a cover letter for a job application at {company_name} for the position of {job_title}."
    # Call the generative AI model
    response = palm.generate_text(
        model=model,
        prompt=prompt,
        temperature=0.87,
        top_k=50,
        top_p=0.95,
        max_output_tokens=500,
    )
    return response.result

# Create the Streamlit App
st.title("Project Insight: AI Feedback Generator for Development Teams")

# Introduction text
st.markdown("""
Project Insight aims to revolutionize the process of providing feedback for development teams by leveraging AI technology. This project will utilize Palm's models/text-bison-001 model to generate detailed and insightful feedback on various aspects of development projects, including project descriptions, code quality, and overall project direction. By automating the feedback generation process, Project Insight aims to enhance collaboration, accelerate project delivery, and improve the quality of software development projects.

**Scenario 1: Code Review Optimization**
Development teams often spend significant time and resources conducting code reviews to ensure code quality and adherence to coding standards. Project Insight can be used to automate the code review process by analyzing code snippets and providing detailed feedback on areas for improvement, potential bugs, and best practices. This streamlines the code review process, allowing teams to focus on implementing feedback and delivering high-quality code faster.

**Scenario 2: Planning and Direction**
In the early stages of a project, defining project goals, requirements, and overall direction is crucial for its success. Project Insight can assist development teams in refining project descriptions, identifying key objectives, and mapping out project milestones. By analyzing project descriptions and providing constructive feedback, Project Insight helps teams ensure clarity and alignment in project planning, ultimately leading to more successful project outcomes.

**Scenario 3: Continuous Improvement and Learning**
Development teams strive for continuous improvement and learning to stay competitive and deliver innovative solutions. Project Insight can be used as a learning tool to provide developers with personalized feedback on their code and project contributions. By highlighting areas for improvement and suggesting best practices, Project Insight empowers developers to enhance their skills, grow professionally, and contribute more effectively to team projects.
""")

# Sidebar for choosing the option
option = st.sidebar.selectbox("Choose an option", ["Generate Project Feedback", "Generate Cover Letter"])

if option == "Generate Project Feedback":
    st.subheader("Generate Project Feedback")

    # Get the user's input
    height = 250
    project_description = st.text_area("Project Description", height=height)
    project_scenarios = st.text_area("Project Scenarios", height=height)
    project_code = st.text_area("Project Code", height=height)

    if st.button('Get Feedback'):
        project_description = project_description.strip()
        project_scenarios = project_scenarios.strip()
        project_code = project_code.strip()

        if project_description and project_scenarios and project_code:
            with st.spinner('Generating feedback...'):
                try:
                    feedback = generate_feedback(project_description, project_scenarios, project_code)
                    st.success('Here is your AI-driven feedback')
                    st.write(feedback)
                except Exception as e:
                    st.error(f'Error generating feedback: {e}')
        else:
            st.error("Please provide all project details.")

elif option == "Generate Cover Letter":
    st.subheader("Generate Cover Letter")
    company_name = st.text_input("Enter the company name")
    job_title = st.text_input("Enter the job title")
    if st.button("Generate"):
        if company_name and job_title:
            with st.spinner('Generating cover letter...'):
                try:
                    cover_letter = generate_cover_letter(company_name, job_title)
                    st.success('Here is your AI-generated cover letter')
                    st.write(cover_letter)
                except Exception as e:
                    st.error(f'Error generating cover letter: {e}')
        else:
            st.warning("Please fill in all the fields.")
