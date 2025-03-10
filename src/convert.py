from weasyprint import HTML
from pathlib import Path

def convert_html_to_pdf():
    # Получаем абсолютный путь к текущей директории
    current_dir = Path(__file__).parent
    
    # Пути к входному HTML и выходному PDF
    html_path = current_dir / 'template.html'
    pdf_path = current_dir / 'output.pdf'
    
    # Конвертируем HTML в PDF
    HTML(html_path.as_uri()).write_pdf(pdf_path)

if __name__ == "__main__":
    convert_html_to_pdf()
    print("PDF успешно создан в src/output.pdf")
