import dropbox

TOK = 'YzhCOnmeCxcAAAAAAAAXJCYc57j6CHEgMH2XZ4_gale3nwuVQ8RsEY12uYbKTJXA'

dbx = dropbox.Dropbox(TOK)

for r in dbx.files_list_folder('').entries:
    print(r.path_display)




