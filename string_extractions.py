	
import time

def requirements():
    instructions = """
    \033[01m\033[44m\n
    This script assumes you have already followed all setup steps found in "Extracting strings for l10n quick-start guide."

    Bedrock, Mozilla-l10n, Langchecker all need to be cloned and dependencies installed.
    \033[0m\n
    """
    return step_handler(instructions)

def first_section():

    instructions = """
    \n 
    Step 1: Extract strings from a template.

      From Bedrock directory if you do not have a locales folder:
        - Run bin/bootstrap.sh to generate a fresh locales folder
      Create the lang file template:
        - Remove the templates folder
        - Start virtual environment `source venv/bin/activate`
        - Extract strings `./manage.py l10n_extract < Relative_path_to_file >`
    \n
    """
    error_instructions = "\nTry `pip install -r requirements/dev.txt` then follow these instructions again:"

    return step_handler(instructions, error_instructions)

def second_section():
    instructions = """
    \n
    Step 2: Prepare a PR in the Mozilla-l10n repo.

      From Bedrock:
        - Copy your new lang file from bedrock/locale/templates/
      In Mozilla-l10n:
        - Paste the copied file into the ‘en-US’ directory with the same relative path as the original file starting at "template"
      Open the file in your editor:
        - Include notes to add context to file \033[90m\033[47m\n
            Example: 
                ## NOTE: demo page available at https://www-dev.allizom.org/about/history/
                ## URL: https://www-dev.allizom.org/%LOCALE%/about/history/

                # HTML page title
                # HTML page description \n\033[0m
        - Confirm all sets of strings have 2 new lines inbetween them
        - Submit the PR
      
      A member of the localization team will review the pr. While you are waiting you can continue to the next step.
    \n
    """
    return step_handler(instructions)

def third_section():
    instructions = """
    \n
    Step 3: Create a Langchecker PR

      In the langchecker repo:
        - Open app/config/sources.inc.php
        - Add an new entry for your file \033[90m\033[47m\n
            Example:
            'mozorg/about/history.lang' => [
                'flags' => [
                    'opt-in' => ['all'],
                ],
                'priority'          => 2,
                'supported_locales' => [
                    'af', 'am', 'ar', 'azz', 'bg', 'bn', 'bs', 'ca', 'cak', 'crh',
                    'cs', 'cy', 'de', 'dsb', 'el', 'en-CA', 'en-GB', 'es-AR', 'es-CL',
                    'es-ES', 'es-MX', 'eu', 'fa', 'fr', 'fy-NL', 'gl', 'hi-IN', 'hr',
                    'hsb', 'ia', 'id', 'it', 'ja', 'kab', 'km', 'ko', 'lt', 'ms', 'nl',
                    'nn-NO', 'nv', 'pa-IN', 'pai', 'pl', 'pt-BR', 'pt-PT', 'ro', 'ru',
                    'sk', 'sl', 'son', 'sq', 'sr', 'sv-SE', 'sw', 'ta', 'tr', 'uk',
                    'uz', 'zam', 'zh-CN', 'zh-TW',
                ],
            ], \n\033[0m
        - Create a PR in the Langchecker repo
        - Cross link your langchecker PR with the PR from Step 2.

      After this is done you can start the next step\033[01m do not commit\033[0m the next changes until asked.
    \n
    """
    return step_handler(instructions)

def fourth_section():
    instructions = """
    \033[01m\033[44m\n
    For this step you will need langchecker installed
    \033[0m\n
    Step 4: Populate other locales

      In the langchecker directory run:
        - `./app/scripts/lang_update`
        - `./app/scripts/lang_update < Relative_path_to_file > 0 all` 
      In your bedrock-l10n/www.mozilla.org directory:
        - Check for new .lang files created in all declared locales
        - Once approved by the localization team commit these files to the PR created in Step 2
        - Squash all commits into one
        - After final approval, merge branch
    \n
    """
    return step_handler(instructions)
    

def step_handler(instructions, error_instructions = "No error instructions available", status = True):
    current_status = status
    while current_status:
        print(instructions)
        print("\033[92m","\nDid that work or was there a problem?")
        move_on = input("Next step (n), there was an error (e), or quit (q) \n(n/e/q) >>> " + "\033[0m")
        if move_on == 'n':
            return "continue"
        elif move_on == 'e':
            print("\033[94m", error_instructions, "\033[0m")
            time.sleep(4)
        elif move_on == "q":
            return "quit"
        else:
            print("\033[91m","\nThat is an invalid input","\033[0m")

def main():
    should_continue = requirements()

    if should_continue == "continue":
        should_continue = first_section()

    if should_continue == "continue":
        should_continue = second_section()
    
    if should_continue == "continue":
        should_continue = third_section()

    if should_continue == "continue":
        should_continue = fourth_section()

    print("\nGood bye\n")

if __name__ == '__main__':
    main()
