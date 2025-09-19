import os
from pydantic_settings import BaseSettings, SettingsConfigDict

# Set an environment variable for demonstration if not using a .env file
# os.environ['ENVIRONMENT'] = 'production'

class AppSettings(BaseSettings):
    # Pydantic will automatically look for environment variables with these names (case-insensitive)
    api_key: str
    database_url: str
    environment: str = 'development' # A field with a default value

    # This tells Pydantic to load variables from a .env file
    model_config = SettingsConfigDict(env_file='.env')


# Instantiate the settings class
# No arguments are needed; Pydantic does the work.
settings = AppSettings()

print(f"API Key: {settings.api_key}")
#> API Key: abc-123-def-456
print(f"Database URL: {settings.database_url}")
#> Database URL: postgresql://user:pass@localhost/db
print(f"Environment: {settings.environment}")
#> Environment: development (or 'production' if you set the env var)