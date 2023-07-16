
from fastapi.templating import Jinja2Templates
from src.app.templatesConst import TemplateConst
 
 
class TemplateBaseClass: 
    jinjaTemplates = Jinja2Templates(directory="src/templates")
    templateConst =TemplateConst
 
    

