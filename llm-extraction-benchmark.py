import marimo

__generated_with = "0.4.3"
app = marimo.App()


@app.cell
def __(mo):
    mo.md("""# LLM Extraction Benchmark
    Batch test for LLMs.""")
    return


@app.cell
def __(get_settings, mo):
    settings = mo.vstack(
        [mo.md("Report configuration"),
         mo.hstack([
         report_name :=mo.ui.text(label="Report filename", 
                                  value=get_settings()["report_name"]),
         report_append :=mo.ui.checkbox(label="append to existing") ], justify="start" ) ])

    organization = mo.vstack(
        [ mo.md("Edit models"), model_list := mo.ui.text_area(label="Models") ])

    tests = mo.vstack(
        [ mo.md("Edit tests"), test_list := mo.ui.text_area(label="Tests") ])

    configs = mo.vstack(
        [ mo.md("Edit configuration"), 
         api_key_list := mo.ui.text_area(label="API keys (JSON)", 
                                  value=get_settings()["api_keys"]) ])

    form3 = mo.ui.form(mo.ui.tabs(
        { "Report": settings, "Models": organization, "Tests": tests, "Configuration": configs }),
        submit_button_label="Start action",               
        show_clear_button=False, 
        bordered=True)

    form3
    return (
        api_key_list,
        configs,
        form3,
        model_list,
        organization,
        report_append,
        report_name,
        settings,
        test_list,
        tests,
    )


@app.cell
def __(api_key_list, os):
    os.environ["OPENAI_API_KEY"] = api_key_list.value
    return


@app.cell
def __(
    form3,
    just_a_function,
    mo,
    model_list,
    report_append,
    report_name,
    save_settings,
):
    mo.stop(form3.value is None, mo.md("Enter data and Click on 'Start action'"))

    save_settings()

    my_date_time2 = just_a_function()

    mo.md(
        f"""
        Welcome {report_name.value} , {report_append.value}

        Models: {model_list.value}

        {my_date_time2}
        """
    ) 
    #if all([report_name.value, model_list.value]) else None
    return my_date_time2,


@app.cell
def __(datetime):
    def just_a_function():
        return datetime.now().strftime("%d.%m.%Y, %H:%M:%S")
    return just_a_function,


@app.cell
def __(api_key_list, get_settings, report_name, saveData):
    def save_settings():
        get_settings()["report_name"] = report_name.value
        get_settings()["api_keys"] = api_key_list.value
        saveData("config.pickle")
    return save_settings,


@app.cell
def __():
    import marimo as mo
    return mo,


@app.cell
def __():
    import json
    import os
    import psutil
    import time
    import textwrap
    import pickle

    from datetime import datetime
    return datetime, json, os, pickle, psutil, textwrap, time


@app.cell
def __(mo, pickle):
    get_settings, set_settings = mo.state({})

    def loadData(filename):
        try:
           with open(filename, 'rb') as file:
                _config = pickle.load(file)
                set_settings(_config)
                file.close()
        except:
            print ("Create config file:", filename)
            _config = {
                "test1": "abc",
                "test2": "xyz",
                "report_name": "default name",
                "api_keys": {}
            }
            set_settings(_config)
            saveData("config.pickle")
        #return _config


    def saveData(filename):
        file = open(filename, 'wb')
        _config = get_settings()
        pickle.dump(_config, file)
        file.close()

    loadData("config.pickle")
    return get_settings, loadData, saveData, set_settings


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
