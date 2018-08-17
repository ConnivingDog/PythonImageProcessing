**NOTES**

* **FIXED**. The program might encounter errors when hidden directories (such as .git folders) are present in the current path.

**Building into an executable**

1. Install pyinstaller :
    
    pip install pyinstaller

2. Once installed, package script :
    
    pyinstaller --onefile [script_name.py]
    
    in this case,

    pyinstaller --onefile conversion.py


**Usage**

1. Run the executable in the same directory where the images to be converted are.

2. Enter the name of the folder where the converted images will be stored.