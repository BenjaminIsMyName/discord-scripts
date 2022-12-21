# Block Discord

Sometimes, we need to make sure we don't get calls or messages from Discord, from no one. That's why I built this python script.

## How to contribute?

1. Fork the project, so you could change things on your end.
1. Clone the project to your local computer, to run, change and test the code.
1. To create isolated environment use venv (AKA `virtualenv`, make sure it is installed via pip list).
   1. Run virtualenv my-env (or any other name) in the terminal.
   1. Run my-env\Scripts\activate (everytime you open the project).
1. Install all the packages needed using:

   ```bash
   pip install -r requirements.txt
   ```

1. Run `pip list` to see the packages that are installed on this specific project.

1. In order to create exe file, use:

   ```bash
   pyinstaller --noconsole --onefile --noupx --icon=app.ico app.py
   ```

   You can remove the `--onefile` flag and use the default one-folder mode if you want the program to load faster. Recommended.

1. **Warning**: do not rename or move the project folder. Otherwise, the packages might stop working.
