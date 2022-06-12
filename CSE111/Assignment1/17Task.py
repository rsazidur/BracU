def replace_domain(email, domain, old_domain="kaaj.com"):
    new_email = ""
    index = -1
    for char in range(len(email)):
        if email[char] == "@":
            index = char
            break

    if index == -1:
        return "Incorrect E-Mail Address!"

    new_email = email[: index + 1]

    if old_domain in email:
        new_email += domain
        comment = "Changed"
    else:
        new_email += domain
        comment = "Unchanged"

    return f"{comment}: {new_email}"


print(replace_domain("alice@kaaj.com", "sheba.xyz", "kaaj.com"))
print(replace_domain("bob@sheba.xyz", "sheba.xyz"))