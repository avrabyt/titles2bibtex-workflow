import subprocess
import os

input_file = "biswas_photosyn_refs.txt"
output_file = "biswas_photosyn_refs.bib"
success_file = "successful_titles.txt"
error_file = "error_titles.txt"

def run_title2bib(title):
    # Create a temporary input file for the title
    temp_input_file = "temp_title.txt"
    with open(temp_input_file, "w") as temp_infile:
        temp_infile.write(title)
    
    temp_output_file = "temp.bib"
    
    try:
        result = subprocess.run(
            ["title2bib", "--input", temp_input_file, "--output", temp_output_file, "--first"],
            check=True,
            capture_output=True,
            text=True
        )
        with open(temp_output_file, "r") as temp_bib:
            bib_content = temp_bib.read()
        # Clean up temporary files
        os.remove(temp_input_file)
        os.remove(temp_output_file)
        return bib_content, None
    except subprocess.CalledProcessError as e:
        # Clean up temporary file
        os.remove(temp_input_file)
        return None, str(e)

successful_titles = 0
failed_titles = 0
failed_titles_list = []

with open(input_file, "r") as infile, open(output_file, "w") as outfile, \
        open(success_file, "w") as success_outfile, open(error_file, "w") as error_outfile:
    for line in infile:
        title = line.strip()
        if title:
            bib_content, error = run_title2bib(title)
            if bib_content:
                outfile.write(bib_content)
                success_outfile.write(title + "\n")
                successful_titles += 1
            else:
                error_outfile.write(title + "\n")
                failed_titles_list.append(title)
                failed_titles += 1
                print(f"Error processing title: {title}")
                print(error)

# Print summary statistics
print(f"Processing complete. {successful_titles} titles processed successfully, {failed_titles} titles failed.")
print("Titles that failed to process:")
for failed_title in failed_titles_list:
    print(failed_title)

print("Check 'successful_titles.txt' and 'error_titles.txt' for details.")
