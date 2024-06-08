from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def root():
    with open("app.html") as f:
        return f.read()


@app.get("/get-column1-data")
def get_column1_data():
    # Query your database to get data for column 1 for all rows
    data = ["Row1-Col1", "Row2-Col1", "Row3-Col1"]
    html = "".join(
        [
            f"<div id='row{index + 1}-col1'>{item}</div>"
            for index, item in enumerate(data)
        ]
    )
    return html


@app.get("/get-column2-data")
def get_column2_data():
    # Query your database to get data for column 2 for all rows
    data = ["Row1-Col2", "Row2-Col2", "Row3-Col2"]
    html = "".join(
        [
            f"<div id='row{index + 1}-col2'>{item}</div>"
            for index, item in enumerate(data)
        ]
    )
    return html


@app.get("/get-column3-data")
def get_column3_data():
    # Query your database to get data for column 3 for all rows
    data = ["Row1-Col3", "Row2-Col3", "Row3-Col3"]
    html = "".join(
        [
            f"<div id='row{index + 1}-col3'>{item}</div>"
            for index, item in enumerate(data)
        ]
    )
    return html
