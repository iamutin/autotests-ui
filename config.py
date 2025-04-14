from enum import StrEnum

from pydantic import EmailStr, FilePath, HttpUrl, DirectoryPath, BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class Browser(StrEnum):
    WEBKIT = "webkit"
    FIREFOX = "firefox"
    CHROMIUM = "chromium"


class TestUser(BaseModel):
    email: EmailStr
    username: str
    password: str


class TestData(BaseModel):
    image_png_file: FilePath


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_nested_delimiter=".",
    )

    app_url: HttpUrl
    headless: bool
    browsers: list[Browser]
    test_user: TestUser
    test_data: TestData
    videos_dir: DirectoryPath | None = None
    tracing_dir: DirectoryPath | None = None
    allure_results_dir: DirectoryPath| None = None
    browser_state_file: FilePath | None = None

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

        self.videos_dir = DirectoryPath("./videos")
        self.tracing_dir = DirectoryPath("./tracing")
        self.allure_results_dir = DirectoryPath("./allure-results")
        self.browser_state_file = FilePath("browser-state.json")

        self.videos_dir.mkdir(exist_ok=True)
        self.tracing_dir.mkdir(exist_ok=True)
        self.allure_results_dir.mkdir(exist_ok=True)
        self.browser_state_file.touch(exist_ok=True)

    @property
    def get_base_url(self) -> str:
        return f"{self.app_url}/"

settings = Settings()
