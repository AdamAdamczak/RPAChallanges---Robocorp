from robocorp import workitems
from robocorp.tasks import get_output_dir, task
from robocorp.log import LogHTMLStyle
from utils.dataHandle import get_file
from utils.browserHandle import open_browser, start_challenge,fill_forms,get_results
import pandas as pd

@task
def producer():
    """Split Excel rows into multiple output Work Items for the next step."""
    filename_path = get_file()
    dt = pd.read_excel(filename_path, sheet_name="Sheet1")
    dt.columns = dt.columns.str.strip()
    for _,row in dt.iterrows():
        payload = {
                "First Name": row["First Name"],
                "Last Name": row["Last Name"],
                "Company Name": row["Company Name"],
                "Role in Company": row["Role in Company"],
                "Address": row["Address"],
                "Email": row["Email"],
                "Phone Number": row["Phone Number"],
            }
        
        workitems.outputs.create(payload)


@task
def consumer():
    """Process all the produced input Work Items from the previous step."""
    page = open_browser()
    start_challenge(page)
    for item in workitems.inputs:
        try:
            fill_forms(page, item.payload)
            item.done()
        except KeyError as err:
            item.fail("APPLICATION", code="ERROR", message=str(err))
    get_results(page)
