import re
import pdfplumber
import subprocess
from pathlib import Path

def text_extractor(pdf_input):
    all_text = ""
    with pdfplumber.open(pdf_input) as text_output:
        pages = text_output.pages
        for i in range(len(pages)):
            page_obj = text_output.pages[i]
            page_text = page_obj.extract_text(layout=True)
            all_text+=page_text
    print(all_text)
    new_text = re.sub(r'\n',"", all_text)
    # with open("all_text.txt", 'w') as file:
    #     file.write(new_text)
    return new_text

def text_to_audio(text_input):
    aiff = Path("output.aiff")
    mp3 = Path("output.mp3")
    subprocess.run(["say", "-o", str(aiff), text_input], check=True)

    # Step 2: Convert AIFF to MP3 using ffmpeg
    subprocess.run(["ffmpeg", "-y", "-i", str(aiff), str(mp3)], check=True)


arg1 = text_extractor("Sample.pdf")
text_to_audio(arg1)
