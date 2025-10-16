from typing import Dict, List, Callable
from json import loads

dataSources: List[Callable[..., Dict[str, str]]] = [
    lambda: loads(open('config.json', 'r').read()),
    lambda: {'content': open('site_content.md', 'r').read().strip()}
]


def get_data() -> Dict[str, str]:
    return {k: v for d in [i() for i in dataSources] for k, v in d.items()}
