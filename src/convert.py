from weasyprint import HTML
from pathlib import Path

def convert_html_to_pdf():
    current_dir = Path(__file__).parent
    
    html_path = current_dir / 'template.html'
    pdf_path = current_dir / 'output.pdf'
    
    HTML(html_path.as_uri()).write_pdf(pdf_path)

if __name__ == "__main__":
    convert_html_to_pdf()
    print("PDF successfully created at src/output.pdf")
