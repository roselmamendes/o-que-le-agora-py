from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env'
print(f'carregando .env em {env_path}')
load_dotenv(dotenv_path=env_path, verbose=True)
