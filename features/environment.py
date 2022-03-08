import os
from behave import *


def before_all(context):
    context.output_filename = "test1.txt"
    try:
        os.remove(context.output_filename)
    except FileNotFoundError:
        pass


def after_scenario(context, scenario):
    context.driver.quit()