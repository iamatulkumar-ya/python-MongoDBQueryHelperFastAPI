from src.app.templateBaseClass import TemplateBaseClass
from src.app.appLoggerBaseClass import AppLoggerBaseClass
from src.service.indexService import getIndexPageData


class IndexHandler(TemplateBaseClass,AppLoggerBaseClass):


    def __init__(self) -> None:
        super().__init__()


    
    def getIndexContent(self,request):
        self.appLogger.info(f"Inside {__name__} module")
        _pageData = getIndexPageData()
        
        self.appLogger.info(f"Got page data  {_pageData}") 
        return self.jinjaTemplates.TemplateResponse(self.templateConst.indexTemplate, {"request":request, "pageData":_pageData})






