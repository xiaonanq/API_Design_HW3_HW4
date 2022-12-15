from concurrent import futures
import logging

import grpc
import Library_pb2_grpc
import Library_pb2

'''
Using a list to store InventoryItems
each InventoryItems follows the structure
defined in Library.proto file
e.g. InventoryItemList = [
    InventoryItem1{
        Id,
        Book{
            id,
            author,
            title,
            year,
            genre
        },
        status
    },
    InventoryItem2{
        ...
    }
]
'''
InventoryItemList = []

class Inventory(Library_pb2_grpc.InventoryServiceServicer):
    def CreateBook(self, request, context):
        newISBN = int(InventoryItemList[len(InventoryItemList)-1].book.Id)+1
        response = Library_pb2.InventoryCreateBookResponse(Id=str(newISBN), title=request.title)
        newBook = Library_pb2.Book(author=request.author,title = request.title,year = request.year,genre = request.genre,Id = response.Id)
        newID = int(InventoryItemList[len(InventoryItemList)-1].Id)+1
        newInventoryItem = Library_pb2.InventoryItem(Id=str(newID), book=newBook, status=Library_pb2.AVAILABLE)
        InventoryItemList.append(newInventoryItem)
        return response
    
    def GetBook(self, request, context):
        for i in range(len(InventoryItemList)):
            if (InventoryItemList[i].book.Id == request.Id):
                return Library_pb2.InventoryGetBookResponse(title=InventoryItemList[i].book.title) 
        
        return Library_pb2.InventoryGetBookResponse(title="Book Not Found") 
    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    Library_pb2_grpc.add_InventoryServiceServicer_to_server(Inventory(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

def generateBooks():
    book1 = Library_pb2.Book(author = "Nannan", title = "Happy Coding", year = 2022, genre = Library_pb2.ENGINEERING, Id = "1")
    InventoryItem1 = Library_pb2.InventoryItem(Id="1", book=book1, status=Library_pb2.AVAILABLE)
    InventoryItemList.append(InventoryItem1)
    
    book2 = Library_pb2.Book(author = "Nann", title = "Take Photos", year = 2022, genre = Library_pb2.ART, Id = "2")
    InventoryItem2 = Library_pb2.InventoryItem(Id="2", book=book2, status=Library_pb2.AVAILABLE)
    InventoryItemList.append(InventoryItem2)
 
if __name__ == '__main__':
    logging.basicConfig()
    generateBooks()
    serve()