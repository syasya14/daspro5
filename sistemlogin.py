def sistem_login (username, password=None):
    if username == "Admin" and password == "Admin123":
        return "Akses admin diberikan"
    elif username == "use" and password == "user123":
        return "Akses terbatas diberikan"
    elif username == "guest" and password is None:
        return "Akses minimal diberikan"
    else:
        return "Akses ditolak"
    

username = input("Masukan username: ")
password = input("masukan password (kosongkan jika guest): ") or None

print(sistem_login(username,password))

