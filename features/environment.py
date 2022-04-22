import os
import take_screenshots
from behave import *


def before_all(context):
    context.output_filename = "test1.txt"
    try:
        os.remove(context.output_filename)
    except FileNotFoundError:
        pass
    

def before_feature(context, feature):
    context.feature = feature
    context.current_screenshot_dir = take_screenshots.make_screenshots_dir(context)
    

def before_scenario(context, scenario):
    context.scenario = scenario


def before_step(context, step):
    context.step = step
    take_screenshots.save_picture(context, "before")


def after_step(context, step):
    take_screenshots.save_picture(context, "after")


def after_scenario(context, scenario):
    context.driver.quit()
    del context.driver
    