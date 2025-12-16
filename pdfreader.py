import pdfplumber
from gtts import gTTS

def text_extractor(pdf_input):
    all_text = ""
    with pdfplumber.open(pdf_input) as text_output:
        pages = text_output.pages
        for i in range(len(pages)):
            page_obj = text_output.pages[i]
            page_text = page_obj.extract_text()
            all_text+=page_text
        
    # with open("all_text.txt", 'w') as file:
    #     file.write(all_text)
    return all_text

def text_to_audio(text_input):
    audio_output = gTTS(text_input,  lang="en")
    audio_output.save('converted_pdf.mp3')

arg1 = text_extractor("sample.pdf")
text_to_audio(arg1)
