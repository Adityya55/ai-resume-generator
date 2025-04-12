from fpdf import FPDF

class ResumePDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "Professional Resume", ln=True, align="C")
        self.ln(5)

    def section_title(self, title):
        self.set_font("Arial", "B", 12)
        self.set_text_color(0, 0, 128)
        self.cell(0, 10, title, ln=True)
        self.set_text_color(0, 0, 0)

    def section_body(self, text):
        self.set_font("Arial", "", 11)
        self.multi_cell(0, 8, text)
        self.ln(3)

def format_as_pdf(name, text):
    pdf = ResumePDF()
    pdf.add_page()

    # Split text by section headers if they exist
    sections = ["Summary", "Education", "Skills", "Projects"]
    for section in sections:
        if section in text:
            start = text.index(section)
            end = min([text.find(s, start + 1) for s in sections if s != section and s in text] + [len(text)])
            content = text[start:end].strip()

            # Write section
            pdf.section_title(section)
            pdf.section_body(content.replace(section, "").strip())

    filename = f"{name.replace(' ', '_')}_resume.pdf"
    pdf.output(filename)
    return filename
