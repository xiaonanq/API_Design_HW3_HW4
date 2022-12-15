import inventory_client

def get_book_titles(client, ISBNList):
    return client.getBookTitles(ISBNList)

if __name__ == '__main__':
    client = inventory_client.InventoryClient()
    ISBNList = ["1", "2"]
    titles = get_book_titles(client, ISBNList)
    print("Title 1: \n", titles[0])
    print("Title 2: \n", titles[1])
    client.close()