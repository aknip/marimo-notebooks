import marimo

__generated_with = "0.3.8"
app = marimo.App()


@app.cell
def __(mo):
    mo.md("""# Test context size in local LLMs

    - Needle in a haystack test
    - Do not use texts on which the model was trained, eg. new texts from https://paulgraham.com (no Gutenberg texts etc.)""")
    return


@app.cell
def __(mo):
    openaikey = mo.ui.text(label="OpenAI Key", kind="password")
    mo.accordion({"Enter your OpenAI key": openaikey})
    #openaikey
    return openaikey,


@app.cell
def __():
    return


@app.cell
def __(openaikey, os, tiktoken):
    os.environ["OPENAI_API_KEY"] = openaikey.value

    enc = tiktoken.get_encoding("cl100k_base")

    text_path = "insurance-emails-anonymized"
    email_texts = []

    # Durchlaufe jedes Datei im angegebenen Verzeichnis
    for dateiname in os.listdir(text_path):
        if dateiname.endswith(".txt"):
            # Erstelle den vollständigen Pfad zur Datei
            dateipfad = os.path.join(text_path, dateiname)
            # Öffne die Datei und lese ihren Inhalt
            with open(dateipfad, 'r', encoding='utf-8') as datei:
                 email_texts.append({"name": dateiname, "text": datei.read()} ) 
    print(email_texts[11]['text'])
    return datei, dateiname, dateipfad, email_texts, enc, text_path


@app.cell
def __(email_texts, enc):
    prompt = """Wie hoch ist die Versicherungssumme? Antworte mit folgendem JSON-Schema: {"Versicherungssumme": "100000", "Versicherungsnehmer_Name": "Testfirma GmbH", "Versicherungsnehmer_Anschrift": "Musterstr. 10, 10000 Berlin", "Versicherungsnehmer_Branche": "Textilproduktion", "Versicherungsnehmer_Umsatz": "23000000", "Vorschäden_benannt": "Ja, in 2019 gab es einen Schaden mit folgenden Details"}. Formatiere Zahlen ohne Tausender-Trennzeichen. 
    Ergänze keinerlei weiteren Text in der Antwort.
    Der Kontext ist die Email  inklusive mehrerer Anhänge eines Versicherungsmaklers, die die Anfrage für eine D&O-Versicherung seines Kunden enthält: 
    """
    prompt2 = """Wie ist der Name des zu versichernden Uneternehmens? Wie hoch ist der Umsatz des Unternehmens? Wie hoch ist die Versicherungssumme? 
    Der Kontext ist die Email  inklusive mehrerer Anhänge eines Versicherungsmaklers, die die Anfrage für eine D&O-Versicherung seines Kunden enthält: 
    """
    full_prompt = prompt + '\n\n\n' + email_texts[11]['text']
    full_prompt = "How are you?"
    print(len(enc.encode(full_prompt)))
    print(len(full_prompt))
    return full_prompt, prompt, prompt2


@app.cell
def __(mo, openaikey):
    button = mo.ui.button(
        value=0, 
        on_click=lambda count: count + 1
        #on_click=lambda _: call_a_function()
    )
    button if openaikey.value else None
    return button,


@app.cell
def __(button, completion, datetime, full_prompt, mo):
    mo.stop(button.value == 0)

    response = completion(
        model="ollama/mixtral-8x7b-instruct-v0.1-q4_0-32k",
        #model="ollama/mixtral-8x7b-instruct-v0.1-q2_K-32k",
        #model="ollama/gemma-7b-instruct-8k",
        #model="ollama/gemma-2b-instruct-8k",
        messages=[{ "content": full_prompt ,"role": "user"}],
        temperature= 0.0, 
        max_tokens= 200
    )

    current_date_time = datetime.now().strftime("%d.%m.%Y, %H:%M:%S")
    print(current_date_time)
    mo.md(
        f"""
        Response: {response.choices[0].message.content}
        """
    )
    return current_date_time, response


@app.cell
def __(mo, set_index):
    button2 = mo.ui.button(label="next", on_change=lambda _: set_index(2))
    button2
    return button2,


@app.cell
def __(get_index, mo):
    mo.stop(get_index() != 2)

    mo.md('yo 2')
    return


@app.cell
def __(mo, set_index):
    button3 = mo.ui.button(label="next", on_change=lambda _: set_index(3))
    button3
    return button3,


@app.cell
def __(get_index, mo):
    mo.stop(get_index() != 3)

    mo.md('yo 3')
    return


@app.cell
def __():
    import marimo as mo
    return mo,


@app.cell
def __():
    import json
    import os
    from getpass import getpass
    import psutil
    import requests
    import time
    import pickle
    import requests
    import textwrap
    import openpyxl
    from types import SimpleNamespace
    from langchain_text_splitters import TokenTextSplitter
    import tiktoken
    from litellm import completion
    from datetime import datetime
    return (
        SimpleNamespace,
        TokenTextSplitter,
        completion,
        datetime,
        getpass,
        json,
        openpyxl,
        os,
        pickle,
        psutil,
        requests,
        textwrap,
        tiktoken,
        time,
    )


@app.cell
def __(mo):
    get_index, set_index = mo.state(0)

    def increment_index():
        set_index(lambda v: v+1)
    return get_index, increment_index, set_index


if __name__ == "__main__":
    app.run()
