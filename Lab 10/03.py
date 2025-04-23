def create_vcard():
    print("Enter Contact Details:")
    full_name = input("Full Name: ")
    phone = input("Phone Number: ")
    email = input("Email: ")
    organization = input("Organization (optional): ")
    title = input("Title (optional): ")

    
    vcard = f"""BEGIN:VCARD
VERSION:3.0
FN:{full_name}
TEL;TYPE=CELL:{phone}
EMAIL;TYPE=INTERNET:{email}"""

    if organization:
        vcard += f"\nORG:{organization}"
    if title:
        vcard += f"\nTITLE:{title}"

    vcard += "\nEND:VCARD"

    
    filename = full_name.replace(" ", "_").lower() + ".vcf"
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(vcard)

    print(f"\n✅ vCard saved as '{filename}' — You can now import it into your phone contacts.")


create_vcard()