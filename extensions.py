print("This script is output file's media.")
extension = input("What's the file name?  ")
name, ext = extension.split(".")
if ext == "gif":
    print("image/gif")

elif ext == "jpg" or ext == "jpeg":
    print("image/jpeg")

elif ext == "png":
    print("image/png")

elif ext == "pdf":
    print("application/pdf")

elif ext == "txt":
    print("application/txt")

elif ext == "zip":
    print("application/zip")

else:
    print("application/octet-stream")
