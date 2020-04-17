from typing import Dict, Any

from aiohttp import web

import controller
from . import utils


class Presenter:
    def __init__(self, controller_: controller.Controller):
        self.controller: controller.Controller = controller_


async def init(config: Dict[str, Any], controller_: controller.Controller):

    presenter = Presenter(controller_)

    app = web.Application(middlewares=[utils.handle])

    app.add_routes([])

    runner = web.AppRunner(app, access_log=False)
    await runner.setup()
    site = web.TCPSite(runner,
                       config["host"],
                       config["port"],
                       backlog=config["backlog"],
                       reuse_port=True)
    await site.start()
