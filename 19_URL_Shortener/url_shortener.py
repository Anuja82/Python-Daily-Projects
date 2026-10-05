import random
import  string
urls={}
def generate_short_code():
    characters=string.ascii_letters+string.digits
    while True:
        code="".join(random.choices(characters,k=6))
        if code not in urls:
            return code
while True:
    print("\n-- URL Shortener ---")
    print("1. Shorten URL")
    print("2. View URLs")
    print("3. Open Short URL")
    print("4. Exit")
    choice=input("Enter your choice:")
    if choice=="1":
        original_url=input("Enter URL:")
        short_code=generate_short_code()
        urls[short_code]=original_url
        print("URL shortenend successfully")
        print("Short code:",short_code)
    elif choice=="2":
        if not urls:
            print("No URLs found.")
        else:
            print("\n--- Saved URLs ---")
            for short_code,original_url in urls.items():
                print("Original URL:",urls[short_code])
            else:
                print("Short URL not found.")
    elif choice=="4":
        print("Goodbye! 👋")
        break
    else:
        print("Invalid choice. Please try again.")
