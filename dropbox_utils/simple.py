import dropbox

TOK = 'YzhCOnmeCxcAAAAAAAAXJCYc57j6CHEgMH2XZ4_gale3nwuVQ8RsEY12uYbKTJXA'

dbx = dropbox.Dropbox(TOK)
print(dbx.users_get_current_account())

print(dbx.file_requests_list())

