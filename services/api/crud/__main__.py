import os

import connexion
import connexion.mock
from connexion.middleware import MiddlewarePosition
from connexion.options import SwaggerUIOptions
from starlette.middleware.cors import CORSMiddleware

from crud.wrapper import GunicornWrapper


def main():
    try:
        options = SwaggerUIOptions(swagger_ui_path="/docs")
        app = connexion.FlaskApp(
            __name__,
            specification_dir=os.path.dirname(os.path.dirname(__file__)),
            swagger_ui_options=options,
        )
        app.add_middleware(
            CORSMiddleware,
            position=MiddlewarePosition.BEFORE_EXCEPTION,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

        app.add_api(
            "openapi.yml",
            resolver=connexion.mock.MockResolver(mock_all=False),
            strict_validation=True,
            validate_responses=True,
        )

        if 1 == 1:
            print("Running local app...")
            app.run(host="0.0.0.0", port="3000")
        else:
            print("Running server mode app...")
            g_app = GunicornWrapper(app, 3000)
            g_app.run()

    except Exception as ex:
        print("Error when running app: ", ex)


#main()
