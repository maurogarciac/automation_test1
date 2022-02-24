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
1. Create a Virtual Environment named `automation1`:
    ```shell
    python -m virtualenv automation1
    ```
    * The name of the Environment has to be set to automation1 because it is already ignored by git.
1. Activate the Environment:
    ```shell
    activate.bat
    ```
1. Install the required Packages:
    ```shell
    python -m pip install requirements.txt
    ```
2. Move your chosen WebDriver to the Scripts folder of your Virtual Environment.
   
3. Run tests:
    ```shell
    behave
    ```