from typing import Dict, Any

from aiohttp import web

import controller
from . import utils

from . import users


class Presenter:
    def __init__(self, controller_: controller.Controller):
        self.controller: controller.Controller = controller_

    users_signup = users.users_signup


async def init(config: Dict[str, Any], controller_: controller.Controller):

    presenter = Presenter(controller_)

    app = web.Application(middlewares=[utils.handle])

    app.router.add_route("POST", "/users.signup", presenter.users_signup)

    runner = web.AppRunner(app, access_log=False)
    await runner.setup()
    site = web.TCPSite(runner,
                       config["host"],
                       config["port"],
                       backlog=config["backlog"],
                       reuse_port=True)
    await site.start()
