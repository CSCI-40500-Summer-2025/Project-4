# Pyinstaller Windows

1. Ensure all necessary modules and libraries are installed. Administrator prompt may be required to install modules, but not required for pyinstaller to run.
   ```shell
   pip install pyinstaller
   ```
3. Copy all .py files from scripts into the same directory.
4. Run the command:
   ```shell
   pyinstaller --onefile main.py
   ```
5. "main.exe" is now available in the Dist sub-folder.
6. The program will run as portable as long as "data.csv" exists in the same directory as main.exe in the correct format (Google Forms output using readme instructions).

# Python Scripts

![demo.gif](./assets/demo.gif)

## Run Scripts

Must have `python3` installed.

1. Create the virtual environment.

   ```shell
   python3 -m venv venv
   ```

2. Activate the `venv`:

   ```shell
   source venv/bin/activate
   ```

3. Install dependencies.

   ```shell
   pip install -r requirements.txt
   ```

4. Run `main.py`:

   ```shell
   python3 main.py
   ```

5. Deactivate the `venv`

   ```shell
   deactivate
   ```

   ![assets/run.gif](./assets/run.gif)
