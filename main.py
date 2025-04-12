from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
from resume_generator import generate_resume_text
from formatter import format_as_pdf

app = FastAPI()

# ✅ Define the input structure
class ResumeInput(BaseModel):
    name: str
    education: str
    skills: str
    projects: str

# ✅ POST route for resume generation
@app.post("/generate_resume")
async def generate_resume(data: ResumeInput):
    try:
        resume_text = generate_resume_text(data)
        pdf_path = format_as_pdf(data.name, resume_text)
        return FileResponse(pdf_path, media_type="application/pdf", filename="resume.pdf")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


