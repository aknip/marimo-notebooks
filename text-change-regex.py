import marimo

__generated_with = "0.8.7"
app = marimo.App()


@app.cell
def __():
    import marimo as mo
    return mo,


@app.cell
def __():
    # Read full file
    f= open('gvnw_symposium_teilnehmer.txt','r')
    if f.mode == 'r':
          contents =f.read()
    f.close()
    return contents, f


@app.cell
def __(contents):
    nameList = []
    doubCheck = []
    lastLine = "xxx"
    counter = 0
    contentsArray = contents.split('\n')
    while True:
        currentLine = contentsArray[counter]
        if (currentLine == lastLine):
            nameblock_start = counter
            lastLine = "xxx"
            while True:
                counter = counter + 1
                if counter == len(contentsArray):
                    break
                currentLine = contentsArray[counter]
                if (currentLine == lastLine):
                    nameblock_end = counter-2
                    if contentsArray[nameblock_start] not in doubCheck:
                        nameCSV = ""
                        for i in range(nameblock_start, nameblock_end + 1):
                            if ((i == nameblock_start + 1) and (nameblock_end-nameblock_start == 1)):
                                nameCSV = nameCSV + ';'    
                            nameCSV = nameCSV + contentsArray[i] + ';'
                        nameList.append(nameCSV)
                        doubCheck.append(contentsArray[nameblock_start])
                        print(nameCSV)
                    break
                else:    
                    lastLine = currentLine            
        else:
            counter = counter + 1
            lastLine = currentLine
        if counter == len(contentsArray):
            break

    print(len(nameList))
    return (
        contentsArray,
        counter,
        currentLine,
        doubCheck,
        i,
        lastLine,
        nameCSV,
        nameList,
        nameblock_end,
        nameblock_start,
    )


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
