import dropbox

TOK = ''
with open('private.txt', 'r') as f:
    TOK = f.read()

print(TOK)

dbx = dropbox.Dropbox(TOK)

for r in dbx.files_list_folder('').entries:
    print(r.path_display)




