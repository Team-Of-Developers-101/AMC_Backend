template = {
    "swagger": "2.0",
    "info": {
        "title": "Advanced Maths Calculator",
        "description": "AMC API Documentations",
        "contact": {
            "responsibleOrganization": "MDigiTech Group",
            "responsibleDeveloper": "MDigiTech Developers",
            "email": "mdigitechgroup@gmail.com",
            "url": "mdigitech.github.io",
        },
        "termsOfService": "amc.com",
        "version": "1.0"
    },
    "basePath": "/api/v1",  # base route for blueprint registration
    "schemes": [
        "http",
        "https"
    ],
    "securityDefinitions": {
        "Bearer": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
            "description": "JWT Authorization header using the Bearer scheme. Example: \"Authorization: Bearer {token}\""
        }
    },
}

swagger_config = {
    "headers": [
    ],
    "specs": [
        {
            "endpoint": 'apispec',
            "route": '/apispec.json',
            "rule_filter": lambda rule: True,  # all in
            "model_filter": lambda tag: True,  # all in
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/api/v1/documentations"
}
