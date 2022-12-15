import logging
import sys

sys.path.append('../Service')

import grpc
import Library_pb2_grpc
import Library_pb2

class InventoryClient():
    stub = 'portal'
    channel = 'channel'
    def __init__(self):
        self.channel = grpc.insecure_channel('localhost:50051')
        self.stub = Library_pb2_grpc.InventoryServiceStub(self.channel)
    def close(self):    
        self.channel.close()
    def getBookTitles(self,ISBNList):
        TitleList = []
        for i in range(len(ISBNList)):
            title = self.stub.GetBook(Library_pb2.InventoryGetBookRequest(Id=ISBNList[i]))
            TitleList.append(title.title)
        return TitleList
    def createBook(self, author, title, year, genre):
        response = self.stub.CreateBook(Library_pb2.InventoryCreateBookRequest(author=author, title=title, year=year, genre=genre))
        ISBN = response.Id
        return ISBN
        