from pdf_reader import read_pdf
from planner import ask_ai, make_plan


def extract_topics(syllabus_text):
    prompt = f"""Below is the text of a course syllabus.
List the main topics a student must learn, in the order they should be studied.
Return only a numbered list, one topic per line, with no extra commentary.

SYLLABUS:
{syllabus_text[:12000]}
"""
    return ask_ai(prompt)


if __name__ == "__main__":
    path = input("PDF file name (for example syllabus.pdf): ")
    text = read_pdf(path)

    if not text.strip():
        print("I couldn't read any text from that PDF. It may be a scanned file.")
    else:
        print("\nFinding topics...\n")
        topics = extract_topics(text)
        print(topics)

        days = input("\nHow many days do you have? ")
        hours = input("How many hours can you study per day? ")

        print("\nMaking your plan...\n")
        print(make_plan(topics, days, hours))