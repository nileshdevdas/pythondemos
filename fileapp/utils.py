"""
Utils Module for all the common Utilties 
""" 
def check_exists(file_name):
    """
    Verifies if the file exists with the given file name 
    The file_name should be a fully qualified filed name
    """
    file_exists = False
    try:
        file = open(file_name, 'r')
        file.close()
        file_exists = True
    except FileNotFoundError as e:
        print("File Does not Exist")
    return file_exists