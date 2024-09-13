import marimo

__generated_with = "0.7.17"
app = marimo.App(app_title="Hello World Mario")


@app.cell
def __():
    import marimo as mo
    import requests
    from datetime import datetime
    import random
    return datetime, mo, random, requests


@app.cell
def __(mo):
    mo.md(
        """
        <br>
        <br>
        # How to step through your notebook

        This notebook explores several approaches to step through your Marimo notebook - executing cells in a controlled, interactive way (a little bit like Juypter...)
        """
    )
    return


@app.cell
def __(mo):
    mo.md(
        """
        <br>
        <br>
        # But before we start: A quick SQL intermezzo...
        """
    )
    return


@app.cell
def __(cars, mo):
    _mydf = mo.sql(
        f"""
        -- Download a CSV and create an in-memory table; this is optional.
        CREATE OR replace TABLE cars as
        FROM 'https://datasets.marimo.app/cars.csv';

        -- Query the table
        SELECT * from cars;
        """
    )
    return


@app.cell
def __(mo):
    mo.md(
        """
        <br>
        <br>
        # Setup
        """
    )
    return


@app.cell
def __(mo):
    openaikey = mo.ui.text(label="OpenAI Key", kind="password")
    mo.accordion({"Enter your OpenAI key (click to expand)": openaikey})
    return openaikey,


@app.cell
def __(mo):
    mo.md(
        """
        <br>
        <br>
        # Idea 1: The Marimo way
        - Hiding **output** of a cell by adding `if...` condition after `mo.md...` (but the cell is executed initially!)
        - Using buttons as triggers for re-exectuing the next cell - but the next cell is executed initially
        - Using `mo.stop...` to stop (initial) execution of a cell, and triggering it by a button
        """
    )
    return


@app.cell
def __(mo, openaikey):
    step1 = mo.ui.text(label="Start with this initial input: ").form(show_clear_button = True)
    step1 if openaikey.value else None
    return step1,


@app.cell
def __(mo):
    button = mo.ui.button(label="Click to re-trigger next cell")
    button
    return button,


@app.cell
def __(button, mo, random):
    # the button acts as a trigger: every time it is clicked, this cell is run
    button 
    # Replace with your custom logic:
    mo.md("This is executed initally - and everytime the button above is clicked: Random = " + str(random.randint(0, 10000)))
    return


@app.cell
def __(mo, step1):
    step2 = f"This is shown after clicking 'Submit': Do something with the input value: {step1.value}"
    mo.md(step2) if step1.value else None
    return step2,


@app.cell
def __(datetime, mo, step1):
    result_step3 = None
    if step1.value:
        result_step3 = datetime.now().strftime("%d.%m.%Y, %H:%M:%S")
    mo.md(f"Do something more... Response: {result_step3}") if step1.value else None
    return result_step3,


@app.cell
def __(mo, result_step3):
    button_step4 = mo.ui.run_button(label="Click to continue")
    button_step4 if result_step3 else None
    return button_step4,


@app.cell
def __(button_step4, datetime, mo):
    mo.stop(not button_step4.value)

    choices = ['red', 'yellow', 'blue']
    colorselect = mo.ui.dropdown(choices)
    result_step4 = datetime.now().strftime("%d.%m.%Y, %H:%M:%S")

    mo.md(f"This is **EXECUTED** after clicking the button above. \n\nChoose a color: {colorselect} \n\n {result_step4}")
    return choices, colorselect, result_step4


@app.cell
def __(mo):
    mo.md(
        """
        <br>
        <br>
        # Idea 2: Step through code execution
        - "Protect" each cell with `mo.stop(get_index() == 1)`, adjusting the value to 1,2,3 etc.
        - Use a button "Next Step" to increase the index. This triggers the cells to execute, dependent on the index
        """
    )
    return


@app.cell
def __(mo):
    get_mode, set_mode = mo.state(True)
    def change_mode():
        set_mode(lambda v: not(v))

    mode_button = mo.ui.button(label='Switch Mode', on_change=lambda _: change_mode())
    mode_button
    return change_mode, get_mode, mode_button, set_mode


@app.cell
def __(get_mode, mo):
    mo.md('Current mode: ' + str(get_mode()))
    return


@app.cell
def __(mo):
    get_index, set_index = mo.state(1)

    step_button = mo.ui.button(label=f"{mo.icon('lucide:rocket')} Next Step", on_change=lambda _: set_index(lambda v: v + 1))   
    #step_button = mo.ui.button(label="Next Step", on_change=lambda _: increment_index())
    step_button
    return get_index, set_index, step_button


@app.cell
def __(get_index, mo):
    mo.stop(get_index() == 1)
    mo.md("Step 1")
    return


@app.cell
def __(get_index, mo):
    mo.stop(get_index() <= 2)
    mo.md("Step 2")
    return


@app.cell
def __(get_index, mo, requests):
    mo.stop(get_index() <= 3)
    # Ollama
    url = "http://127.0.0.1:11434/api/generate"
    headers = {
        "Content-Type": "application/json",
    }
    data = {
        "model": "llama3.1",
        "prompt": "Hello, how are you?",
        "stream": False
    }
    response = requests.post(url, headers=headers, json=data)
    response_data = response.json()
    output = response_data['response']
    mo.md("Step 3 \n\n" + output)
    return data, headers, output, response, response_data, url


@app.cell
def __():
    return


@app.cell
def __(mo):
    mo.md(
        """
        <br>
        <br>
        # Idea 3 : Use functions to structure code execution (WIP)
        - Call functions by explicitly by using buttons
        - Idea: Use a global variable `global state` which is used by every function => Global objects are not reactive in Marimo!
        - Better: Hand over the global state to each function and return the changed state object. Problem: How to handle the returned object from withn the on_change-event of the button
        """
    )
    return


@app.cell
def __():
    # Use this as NON REACTIVE global state store
    # used for all functions
    global_state = {'var1': 'var1 inital value', 'var2': 'var2 inital value'}
    return global_state,


@app.cell
def __(global_state):
    def do_stepA(dummy):
        #mo.md("Executing Step A") # does not work if executed from another cell
        print('Executing Step A')
        global_state['var1'] = 'xxx'
    return do_stepA,


@app.cell
def __(do_stepA, mo):
    mo.ui.button(label='Start Step A', on_change= lambda _: do_stepA(None))
    return


@app.cell
def __(global_state):
    print(global_state['var1'])
    return


@app.cell
def __(mo):
    mo.md(
        """
        <br>
        <br>
        # Idea 4: Use forms to structure code execution
        """
    )
    return


@app.cell
def __(mo):
    form = mo.md(
       r"""
       Choose your algorithm parameters:

       - $\epsilon$: {epsilon}
       - $\delta$: {delta}
       """
    ).batch(epsilon=mo.ui.slider(0.1, 1, step=0.1), delta=mo.ui.number(1, 10)).form()
    form
    return form,


@app.cell
def __(form, mo, random):
    mo.stop(not form.value, "Click 'Submit' to generate a random number")

    mo.md(str(random.randint(0, 1000)))
    return


@app.cell
def __(form, mo):
    mo.md(str(form.value))
    return


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
