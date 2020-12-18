import re

string = input()
carts = input()
pattern_for_email = r"^[a-zA-Z]{0,100000000}[@][a-zA-Z]{0,100000000}\.[a-zA-Z]{1,10000}"

post_domain_pattern = r"@[a-zA-Z]"
first_domain_pattern = r"@$"
name_email_pattern = r"^@"
post_domain_pattern = r"@[a-zA-Z]+\.$"

isChanged = False


def addPostDomain(final_string, i):
    global isChanged
    if re.findall(post_domain_pattern, final_string):
        final_string += carts[i]
        isChanged = True
    return final_string


def addEmailName(final_string, i):
    global isChanged
    if re.findall(name_email_pattern, final_string):
        final_string = carts[i] + final_string
        isChanged = True
    return final_string


def addFirstDomain(final_string, i):
    global isChanged
    if re.findall(first_domain_pattern, final_string):
        final_string += carts[i]
        isChanged = True
    return final_string


def addEmailDog(final_string, i):
    global isChanged
    if "@" not in final_string and carts[i] == "@":
        if final_string[-1] != ".":
            final_string += "@"
        else:
            final_string = "@" + final_string
        isChanged = True
    return final_string


for i in range(len(carts)):
    isChanged = False
    if not isChanged:
        string = addEmailDog(string, -i)
    if not isChanged:
        string = addFirstDomain(string, -i)
    if not isChanged:
        string = addEmailName(string, -i)
    if not isChanged:
        string = addPostDomain(string, -i)
    if i == len(carts) - 1:
        if re.findall(pattern_for_email, string):
            pass
        else:
            string = "Impossible"
        break
    if not isChanged:
        string = "Impossible"
        break

print(string)
