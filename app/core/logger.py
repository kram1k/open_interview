import logging

string_logging = "[%(asctime)s.%(msecs)03d] %(module)10s:%(lineno)-3d %(levelname)-7s - %(message)s"


def configure_logging(
    level=logging.INFO,
    format_log=string_logging
):
    logging.basicConfig(
        format=format_log,
        level=level,
        datefmt="%Y-%m-%d %H:%M:%S",
    )
