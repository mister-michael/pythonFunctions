def run(*kids):
    for kid in kids:
        print(f"{kid} ran")

def slide(*kids):
    for kid in kids:
        print(f"{kid} slid")

def hide_and_seek(seeker, *kids):
    print(f"{seeker} sought")
    for kid in kids:
        print(f"{kid} ran")

def swing(*kids):
    for kid in kids:
        print(f"{kid} swung")

run("pam", "sam", "andrea", "will")
swing("marybeth", "ariel", "kevin", "courtney")
slide("mike", "jack", "jessifer", "earl")
hide_and_seek("bob", "henry", "heather", "hayley", "hugh")