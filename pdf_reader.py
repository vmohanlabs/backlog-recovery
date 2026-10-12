from pypdf import PdfReader


def read_pdf(path):
    reader = PdfReader(path)
    pages = []
    for page in reader.pages:
        text = page.extract_text()
        if text:
            pages.append(text)
    return "\n".join(pages)


if __name__ == "__main__":
    text = read_pdf("syllabus.pdf")
    print(f"Characters read: {len(text)}")
    print(text[:500])