import webbrowser  # 1. Import the browser library

# 1. Writing to a file
with open("data.txt", "w") as file:
    file.write("Welcome to Dip's collection!\n")
    file.write("Python Profile found on GitHub:\n")
    file.write("https://github.com/diptarafder17-prog\n")

# 2. Reading from a file
with open("data.txt", "r") as file:
    content = file.read()
    print(content)

# 3. Automatically open your website in the browser!
print("\nOpening your GitHub profile...")
webbrowser.open("https://github.com/diptarafder17-prog")
