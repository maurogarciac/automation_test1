import datetime
import os


def make_screenshots_dir(context):
    #variable that declares the name of the new dir
    #reemplazar espacios por underscores o algo parecido
    new_dir_name = f"{datetime.date.today()}-{datetime.datetime.now().hour}hs-{datetime.datetime.now().minute}mins-{context.feature.name}"
    #current working dir
    cwd = os.getcwd()
    screenshots_directory = os.path.join(cwd, "screenshots")
    os.makedirs(screenshots_directory, exist_ok = True)
    new_path = os.path.join(screenshots_directory, new_dir_name)
    #check if directory exists, and create it if it doesn't
    candidate = new_path
    created = False
    i = 0
    while not created:
        try:
            os.mkdir(candidate)
            created = True
        except:
            i += 1
            candidate = f"{new_path}_{i}"
    return candidate


def save_picture(context, before_after = ""):
    #now take the screenshot and save it in the new directory
    if "driver" in context and context.driver is not None:
        step_name = f"{context.step.line}"
        if context.step.table is not None:
            step_name = f"{step_name}_{context.step.table.iteration}"
        screenshot_file_name_prefix = os.path.join(f"{context.current_screenshot_dir}", f"{context.scenario.name}-{context.step.line}-{before_after}")
        context.driver.find_element_by_tag_name("body").screenshot(f"{screenshot_file_name_prefix}-full.png")
        context.driver.save_screenshot(f"{screenshot_file_name_prefix}.png")