import os
import fnmatch

def search_files(search_terms, directory='.', file_extensions=['*.txt', '*.py']):
    matches = []
    for root, dirnames, filenames in os.walk(directory):
        for extension in file_extensions:
            for filename in fnmatch.filter(filenames, extension):
                if any(term.lower() in filename.lower() for term in search_terms):
                    matches.append(os.path.join(root, filename))
    return matches

def main():
    search_terms = ["youtube","channel"]
    directory_to_search = 'c:\\'  # Change this to the directory you want to search
    file_extensions = ['*.txt', '*.py']

    matched_files = search_files(search_terms, directory_to_search, file_extensions)
    
    if matched_files:
        print("Found the following files:")
        for file in matched_files:
            print(file)
    else:
        print("No files found matching the search terms.")

if __name__ == "__main__":
    main()
