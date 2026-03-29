import azure.functions as func
from function1 import bp1
from function2 import bp2

# Note: Using AuthLevel.ANONYMOUS because we will use 
# Azure AD (App Service Auth) for Managed Identity security.
app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

app.register_functions(bp1)
app.register_functions(bp2)