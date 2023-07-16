
class UtilClass:


    def __init__(self) -> None:
        pass


    def generateAPIResponse(self,responseStatusCode:int,  responseData:dict, responseStatus:str,responseError=""):
 
        return {
            "responseStatusCode" : responseStatusCode,
            "responseStatus":responseStatus,
            "responseError":responseError,
            "responseData":responseData
        }

    
         