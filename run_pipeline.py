import json
import os
import time
import google.generativeai as genai

# ==============================================================================
# CONFIGURE YOUR API KEY HERE
# ==============================================================================
API_KEY = "AIzaSyDhz5pjjgQBWKNUbzoZ1Y_EWxmsf7CcAUo"
genai.configure(api_key=API_KEY)

# Select Google model
model = genai.GenerativeModel('gemini-2.5-flash')

def load_file(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return f"Error loading {filepath}: {e}"

def load_pipeline():
    with open("pipeline.json", "r", encoding="utf-8") as f:
        return json.load(f)

def run_pipeline():
    print("Launching Playbook System with Gemini API...")
    
    if API_KEY == "ENTER_YOUR_API_KEY_HERE":
        print("[ERROR] Please open run_pipeline.py and enter your API Key in the API_KEY variable.")
        return
        
    config = load_pipeline()
    output_dir = config.get("output_dir", "outputs")
    os.makedirs(output_dir, exist_ok=True)
    
    # Read core context files
    context_text = load_file("prompt-templates/CONTEXT.md")
    plan_text = load_file("prompt-templates/PLAN.md")
    role_prompts_text = load_file("prompt-templates/ROLE_PROMPTS.md")
    
    # Replace variables in context
    for key, val in config['variables'].items():
        context_text = context_text.replace(f"{{{{{key}}}}}", val)
        plan_text = plan_text.replace(f"{{{{{key}}}}}", val)

    final_output_path = os.path.join(output_dir, "final_executive_research_report.md")
    
    # Delete old output file if it exists
    if os.path.exists(final_output_path):
        os.remove(final_output_path)
    
    accumulated_output = ""
    
    for epic in config['epics']:
        print(f"\n[Executing] {epic['id']} - {epic['task_name']}...")
        
        epic_id = epic['id']
        epic_files = os.listdir("prompt-templates/epics")
        epic_filename = next((f for f in epic_files if f.startswith(epic_id)), None)
        
        if not epic_filename:
            print(f"[ERROR] Could not find file for {epic_id}")
            continue
            
        epic_text = load_file(f"prompt-templates/epics/{epic_filename}")
        skill_text = load_file(epic['skill_file'])
        
        # 1. Create prompt for Executor Agent
        prompt = f"""
You are a professional AI Agent executing Game Research tasks.
Below are the guiding documents:

--- CONTEXT ---
{context_text}

--- SPECIALIZED SKILL ---
{skill_text}

--- CURRENT TASK ({epic_id}) ---
{epic_text}

--- ACCUMULATED REPORT (Inherited from previous steps) ---
{accumulated_output if accumulated_output else "No content yet. This is the first step."}

--- REQUIREMENT ---
Write the content for {epic_id} based on the instructions above. Output the article content only, do not add conversational filler or explanations. Strictly adhere to Markdown format.
"""
        print(f"   [System] Calling Gemini to generate content...")
        try:
            response = model.generate_content(prompt)
            result_text = response.text
        except Exception as e:
            print(f"[ERROR] API Call Failed: {e}")
            continue
            
        # 2. QA Evaluator evaluation
        print(f"   [System] Calling QA Evaluator to score the output...")
        qa_prompt = f"""
You are the QA Evaluator. Please evaluate the following output report based on logic, adherence to the task, and Markdown formatting.

--- CONTEXT & TASK ---
This output was generated for task {epic_id}.

--- GENERATED OUTPUT ---
{result_text}

--- REQUIREMENT ---
If the report violates major constraints (e.g., hallucinating impossible data without marking it as an estimate, completely wrong format), reply: [FAIL - BUG] along with the reason.
If the report meets the standards, reply: [PASS - DELIVER].
"""
        try:
            qa_response = model.generate_content(qa_prompt)
            qa_result = qa_response.text
            print(f"   [QA Result]:\n      {qa_result.strip()}")
        except Exception as e:
            print(f"[ERROR] QA API Failed: {e}")
            
        # 3. Write to output file
        accumulated_output += f"\n\n{result_text}\n\n"
        with open(final_output_path, "a", encoding="utf-8") as out_f:
            out_f.write(f"\n\n{result_text}\n\n")
            
        print(f"   [Success] Result merged into {final_output_path}")
        time.sleep(2) # Prevent rate limit

    print("\n[PROCESS COMPLETE] Final report has been successfully saved.")

if __name__ == "__main__":
    run_pipeline()
