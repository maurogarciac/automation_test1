import os
from behave import *
from take_screenshots import save_picture


def before_all(context):
    context.output_filename = "test1.txt"
    try:
        os.remove(context.output_filename)
    except FileNotFoundError:
        pass


def before_step(context, step):
    
    save_picture(context, 1)


def after_step(context, step):
    save_picture(context, 2)


def after_scenario(context, scenario):
    context.driver.quit()