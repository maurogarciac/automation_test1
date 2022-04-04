import os
import datetime
from pathlib import Path

def save_picture(context, driver, b_a = 0):
    before_after = ["only", "before", "after"]
    itemorder = before_after[int(b_a)]
    
    #variable that declares the name of the new dir
    new_dir_name = f"{datetime.date.today()}-{datetime.datetime.now().hour}hs-{datetime.datetime.now().minute}mins-{context.feature.name}"
    
    #declare the parent directory
    absolute_path = os.path.abspath(__file__)
    project_directory = os.path.dirname(absolute_path)
    screenshots_directory = os.path.join(project_directory, "screenshots")
    new_path = os.path.join(screenshots_directory, new_dir_name)
    #check if directory exists, and create it if it doesn't
    try:
        Path(new_path).is_dir()
    except FileNotFoundError:
        os.mkdir(new_path)
    #now take the screenshot and save it in the new directory
    driver.get_full_page_screenshot_as_png(f"{context.scenario.name} - {context.step.number} - {itemorder}-full",  f"{new_path}")
    driver.save_screenshot(f"{context.scenario.name} - {context.step.number} - {itemorder}",  f"{new_path}")
    """
    for files in os.walk(screenshots_directory):
        for file in files:
            if file.__contains__(f"{context.scenario.name}-{context.step.number}-only.png"):
                return before_after[1]
            if file.__contains__(f"{context.scenario.name}-{context.step.number}-before.png"):
                before_after = "after"
            else:
                #except there is no before and after in some instances, i.e. "Google Search Is Loaded"
                before_after = "before"
    """
