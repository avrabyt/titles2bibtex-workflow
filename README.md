## Reference Processing Workflow

This workflow helps you convert a list of references into a BibTeX file while handling any errors gracefully. Follow the steps below to process your references efficiently.

### Steps:

1. **Prepare Your References**:
    - Collect / Copy all the references

2. **Extract Titles**:
    - Paste your list of references into ChatGPT to extract the titles.
    - ChatGPT will provide a downloadable text file (`references_titles.txt`) containing only the titles.

3. **Download the Titles File**:
    - Download `references_titles.txt` from the ChatGPT interface.

4. **Processing Script**:
    - Python script named `process_titles.py` will do the rest

5. **Place the Input File**:
    - Ensure that `references_titles.txt` is in the same directory as your script file.

6. **Run the Script**:
    - Open your terminal or command prompt.
    - Navigate to the directory where your script file is located.
    - Run the script with the command:
      ```bash
      python process_titles.py
      ```

7. **Review the Output**:
    - The script will generate three files:
        - `refs.bib`: Contains the BibTeX entries for the successfully processed titles.
        - `successful_titles.txt`: Contains the titles that were successfully processed.
        - `error_titles.txt`: Contains the titles that caused errors.
    - It will also print a summary of the processing, including the titles that failed, to the terminal.
