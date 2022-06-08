# Captain Cap

Create virtualenv:

```bash
pip install virtualenv
virtualenv .venv
# for macos / linux
source .venv/bin/activate

# for windows
source .venv/Scripts/activate
```

Install python requirements:

```bash
pip install -r requirements.txt
```

Choose interpreter.

```txt
CTRL+SHIFT+P -> Python: Select interpreter
```

Freeze requirement versions:

```bash
pip freeze # находим нужные библиотеки и фиксируем версии в requirements.txt
```

Run:

```bash
python -m cap
```
