# dictionary for the algorithm(length of site mod 10)
special = {
    0: ")",
    1: "!",
    2: "@",
    3: "#",
    4: "$",
    5: "%",
    6: "^",
    7: "&",
    8: "*",
    9: "("
}


def gen_password(site: str):
    # reverse the string
    password = site[::-1]
    # get length of site
    size = len(site) % 10
    # add the special character to end of reversed site
    password = password + special[size]
    # add the length of the site to the end of the string
    password = password + str(size)
    return password


def prompt():
    print("What is the website that your password is for?")
    # get the site password is generated for
    site = input()
    return site

# function isn't used anymore, but good practice for Dynamic Programming
def __factorial__(n: int):
    nums = [1]
    a: int
    for i in range(1, n + 1):
        a = nums[i - 1] * i
        nums.append(a)
    return a


g = prompt()

c = gen_password(g)
print(c)
