import time
from fastapi import Request
from logger import logger


async def ecommerce_middleware(request: Request, call_next):
    logger.info("Starting=============")
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    logger.info(f"ended. process time: {process_time}")
    return response
