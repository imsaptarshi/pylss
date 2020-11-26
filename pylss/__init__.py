from os import scandir,getcwd

def getDirList():
    dir_entries=scandir("./")
    print(getcwd()[getcwd().rfind('/'):])
    for entry in dir_entries:
        if entry.is_dir():
            print(f'   ├──{entry.name}/')
            sub_dir_entry=scandir(entry.path)
            for sub_entry in sub_dir_entry:
                print(f'   |   ├──{sub_entry.name}')
        else:
            print(f'   ├──{entry.name}')

if __name__ == "__main__":
    getDirList()