# i-Citty-Assistant

Assistente Virtual com IBM Watson (Assistant, Translator), Google Learning (STT e TTS) e Banco de Dados para Curadoria

Toda esta tecnologia ainda aplicaremos dentro de uma raspberry PI, vamos trabalhar o microfone e placa de Som, sensor de presença sensor de distância, câmera para reconhecimento de imagens que pode disparar uma notificação qualdo encontra algo que está no alvo das buscas na imagem.

Esta aplicação poderá também ser utilizada juntamente com servo motores gerando um veículo espião.

### Atenção:
No Windows, ao rodar o ASGI com channels recebemos um erro NotImplementedError.
Então, para rodar no windows é preciso fazer uma alteração no arquivo venv/lib/site-packages/twisted/internet/asyncioreactor.py:

onde temos:
```python
from twisted.internet.interfaces import IReactorFDSet

try:
    from asyncio import get_event_loop
except ImportError:
    raise ImportError("Requires asyncio.")

# As per ImportError above, this module is never imported on python 2, but
```
substitua por:
```python
from twisted.internet.interfaces import IReactorFDSet

import sys

try:
    from asyncio import get_event_loop, set_event_loop_policy, WindowsSelectorEventLoopPolicy
except ImportError:
    raise ImportError("Requires asyncio.")

if sys.platform == 'win32':
    set_event_loop_policy(WindowsSelectorEventLoopPolicy())

# As per ImportError above, this module is never imported on python 2, but
```

Desta forma o sistema estará apto a rodar no windows. Obeserve que em servidores linux não é necessária esta mudança.
