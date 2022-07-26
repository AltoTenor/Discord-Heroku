
def srch(query):
    from googlesearch import search
    

    # to search
    u=''
    for j in search(query, tld="co.in", num=3, stop=3):
        u+=j+'\n'
    return(u)
