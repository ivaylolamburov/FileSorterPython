from pathlib import Path

# getting the directory in which we will sort the files
path = Path(input('Absolute path to directory: ').strip())
# pref - short for preferred
pref_extensions = input('Extensions (leave blank for all): ').split(' ')

# using '*.*' because we only want the files in this folder
files = [file for file in path.glob('*.*') if file.is_file()]
# using a set because we only want every unique extension rather than all
extensions = {file.suffix for file in files}

# in case the user has any preferred extensions
if pref_extensions != ['']:
    extensions = set(filter(lambda ext: ext in pref_extensions, extensions))
    files = list(filter(lambda file: file.suffix in extensions, files))

print('Extensions: ', *extensions)

# we check if files is not empty
if files:

    # we want to do this process for every extension
    for extension in extensions:

        # creating the new directory's name and path
        dir_name = extension.removesuffix('.').upper() + ' Files'
        dir_path = path / dir_name

        # we don't mind if the folder already exists, so we skip the exception (FileExistsError)
        if not Path.exists(dir_path):
            dir_path.mkdir()
            print(f'Directory {dir_name} created!')
        else:
            print(f'Directory {dir_name} already exists')

        # we irritate over every file and check if it has the extension
        for file in files:
            if file.suffix == extension:

                # checks if there is already a file with the same name in the directory (FileExistsError)
                if Path.is_file(dir_path / file.name):
                    print(f'ERROR: {file.name} already exists at {dir_name}!')
                    continue

                file.rename(dir_path / file.name)

else:
    print('ERROR: No files found.')
