import pydantic


class Settings(pydantic.BaseSettings):
    provider: str
    output_collection: str = "konstantin-stream-time-collection"
    version: int = 1


SETTINGS = Settings()