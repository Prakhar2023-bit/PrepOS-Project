import json
from groq import Groq
from app.core.config import settings

# Initialize the Groq client securely using the key from config
client = Groq(api_key=settings.GROQ_API_KEY)

def generate_career_roadmap(target_role: str, current_skills: str = "None specified"):
    """
    Calls the Groq API to generate a structured JSON roadmap.
    """
    
    # We use Llama 3 70B because it is exceptional at reasoning and JSON formatting
    model = "llama-3.3-70b-versatile" 
    
    prompt = f"""
    You are an elite Technical Career Coach and System Architect.
    A user wants to achieve the following target role: {target_role}.
    Their current skills are: {current_skills}.
    
    Create a 3-step technical roadmap to bridge the gap.
    You MUST return ONLY valid JSON in the exact structure below, with no markdown formatting or extra text:
    
    {{
        "title": "Roadmap to {target_role}",
        "steps": [
            {{
                "step_number": 1,
                "focus": "String (e.g., Core Foundation)",
                "action_items": ["Action 1", "Action 2"]
            }},
            {{
                "step_number": 2,
                "focus": "String (e.g., Backend Architecture)",
                "action_items": ["Action 1", "Action 2"]
            }},
            {{
                "step_number": 3,
                "focus": "String (e.g., System Design & Interviews)",
                "action_items": ["Action 1", "Action 2"]
            }}
        ]
    }}
    """

    try:
        # Send the request to Groq
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model=model,
            temperature=0.2, # Low temperature keeps the AI focused and deterministic
        )
        
        # Extract the text and parse it into a Python dictionary
        raw_output = response.choices[0].message.content
        parsed_json = json.loads(raw_output)
        
        return parsed_json

    except Exception as e:
        # If the AI fails or returns bad JSON, we catch it gracefully
        print(f"AI Engine Error: {e}")
        return {
            "title": "Fallback Roadmap",
            "steps": [{"step_number": 1, "focus": "Error generating roadmap", "action_items": ["Please try again later"]}]
        }
    
def analyze_job_description(job_description: str, current_skills: str = "None specified"):
    """
    Analyzes a raw Job Description and generates a targeted roadmap.
    """
    model = "llama-3.3-70b-versatile" 
    
    prompt = f"""
    You are an elite Technical Career Coach and System Architect.
    
    Analyze the following Job Description:
    {job_description}
    
    The user's current skills are: {current_skills}
    
    CRITICAL INSTRUCTION: When analyzing the job requirements, carefully evaluate "OR" conditions (e.g., 'React OR Angular', 'AWS OR GCP'). Do not identify a skill gap or penalize the user if they meet at least one side of an "OR" condition.
    
    Create a 3-step technical roadmap to bridge the gap between their current skills and the required skills in the JD.
    You MUST return ONLY valid JSON in the exact structure below, with no markdown formatting or extra text:
    
    {{
        "title": "JD Analysis: Roadmap",
        "steps": [
            {{
                "step_number": 1,
                "focus": "String",
                "action_items": ["Action 1", "Action 2"]
            }},
            {{
                "step_number": 2,
                "focus": "String",
                "action_items": ["Action 1", "Action 2"]
            }},
            {{
                "step_number": 3,
                "focus": "String",
                "action_items": ["Action 1", "Action 2"]
            }}
        ]
    }}
    """

    try:
        response = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model=model,
            temperature=0.2, 
        )
        return json.loads(response.choices[0].message.content)

    except Exception as e:
        print(f"AI Engine Error (JD Analysis): {e}")
        return {
            "title": "Fallback Roadmap",
            "steps": [{"step_number": 1, "focus": "Error parsing JD", "action_items": ["Please check the JD format and try again"]}]
        }