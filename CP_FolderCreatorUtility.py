import os
import shutil
import time

def main():
    prereq_common_folder = "common"
    prereq_files = [
        "main.cpp", "inputf.in", "outputf.out"
    ]
    # Create path for prerequisite files
    for i in range(len(prereq_files)):
        prereq_files[i] = f"{prereq_common_folder}/{prereq_files[i]}"
    # There are platform-specific features down there, so make sure you also update their folder names if you decide to change folder names in this array. (Hint: Ctrl + F)
    platform_folders = [
        "CodeForces", "LQDOJ"
    ]

    print("-------- Folder Creator Utility --------")
    print("Choose platform (input index):")
    for i in range(len(platform_folders)):
        print(f"{i+1}. {platform_folders[i]}")

    chosen_platform_folder = int(input("\n>> "))
    if chosen_platform_folder not in range(1, len(platform_folders)+1):
        print("Invalid platform! Retrying....")
        time.sleep(0.5)
        os.system("cls")
        main()

    chosen_platform_folder = platform_folders[chosen_platform_folder - 1];

    fts = input("First-time setup? (y/n) >> ")
    root_folder = ""
    if fts.lower() == 'y':
        root_folder = input("Enter root folder name >> ")
        print("Folder created successfully! Reloading...")
        time.sleep(0.5)
        os.system("cls")

    elif fts.lower() == 'n':
        root_folder = input("Enter root folder name >> ")
        if not os.path.isdir(f"{chosen_platform_folder}/{root_folder}"):
            print(f'Folder "{root_folder}" does not exist! Retrying...')
            time.sleep(0.5)
            os.system("cls")
            main()
        
    
    # There are some platform-specific features that will make the code longer, especially if it's a general folder creator utility

    # PLATFORM-SPECIFIC BEGIN
    CF_multiple_subfolders = False
    CF_new_subfolders = []
    if chosen_platform_folder == "CodeForces":
        des = input(f"Create multiple subfolders for {chosen_platform_folder}? (y/n) >> ")
        if des.lower() == 'y':
            CF_multiple_subfolders = True
            CF_new_subfolders = input("Enter subfolder names, separated by 1 whitespace (e.g. >> A B C D E F) >> ").split(" ")
            CF_multiple_subfolders_folder = f"{chosen_platform_folder}/{root_folder}"
    # PLATFORM-SPECIFIC END
   
    # PLATFORM-SPECIFIC BEGIN         
    if chosen_platform_folder != "CodeForces" or (chosen_platform_folder == "CodeForces" and not CF_multiple_subfolders):
        #new_folder = input("Enter folder name >> ")
        new_folder = f"{chosen_platform_folder}/{root_folder}" # /{new_folder}"
    # PLATFORM-SPECIFIC END

    # PLATFORM-SPECIFIC BEGIN
    if chosen_platform_folder == "LQDOJ": url = input(f"Enter {chosen_platform_folder} URL >> ")
    # PLATFORM-SPECIFIC END

    try:
        # PLATFORM-SPECIFIC BEGIN
        if chosen_platform_folder == "CodeForces" and CF_multiple_subfolders:
            for subfolder in CF_new_subfolders:
                subfolder = f"{CF_multiple_subfolders_folder}/{subfolder}"
                os.makedirs(subfolder, exist_ok=True)
                for file in prereq_files:
                    shutil.copy(file, subfolder)
        # PLATFORM-SPECIFIC END
                
        else:
            os.makedirs(new_folder, exist_ok=True)
            for file in prereq_files:
                shutil.copy(file, new_folder)

        # PLATFORM-SPECIFIC BEGIN
        if chosen_platform_folder == "LQDOJ":
            with open(f"{new_folder}/link.txt", "w") as file:
                file.write(url)
        # PLATFORM-SPECIFIC END

        print("\nFolder setup successful.");

    except FileNotFoundError as fnfe:
        print(f'ERROR: File not found. You may have renamed the root folder, or the files in the "common" folder.\n\tError message: {str(fnfe)}')

    except Exception as e:
        print(f"ERROR: Unknown error.\n\tError message: {str(e)}")

main()