# Automation Test 1
## Requirements
* A WebDriver .exe file (e.g geckodriver for Firefox)
* Python 3.x installed

## Quick execution manual

1. Clone this Repository and change directory into it:
    ```shell
    git clone https://github.com/maurogarciac/automation_test1.git
    cd automation_test1
    ```
1. Install virtualenv
    ```shell
    python -m pip install virtualenv 
    ```
1. Create a Virtual Environment inside a folder named `venvs`:
    ```shell
    python -m virtualenv venvs/<your_venv_name>
    ```
    * The path of the Environments created has to be set to venvs because it is ignored by git.
1. Activate the Environment:
    ```shell
    venvs/<your_venv_name>/Scripts/activate
    ```
1. Install the required Packages:
    ```shell
    python -m pip install -r requirements.txt
    ```
1. Move your chosen WebDriver.exe to the Scripts folder of your Virtual Environment.
   
1. Run tests:
    ```shell
    behave
    ```