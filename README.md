# python-lib
useful python pieces of code, outdated, see [xsthunder/xs_lib](https://github.com/xsthunder/xs_lib) for latest lib.

## usage

### installation
python don't allow dash `-` in import, so we'll rename it.

```bash
git clone --depth=1 https://github.com/xsthunder/python-lib.git xs_python_lib
```

or 

```bash
git clone --depth=1 git@github.com:xsthunder/python-lib.git xs_python_lib
```

or use as submodule

```bash
git submodule add https://github.com/xsthunder/python-lib.git xs_python_lib
```

### usage

assume the follow file structure.
```bash
.
├── xs_python_lib
├── READMD.md
├── data_struct_info
│   └── prepare_data_struct.ipynb // in here
├── input_data
└── output_data
```

#### recommanded import way

python don't allow loading pakage in higher level directory than its module file, see [this](https://stackoverflow.com/questions/6323860/sibling-package-imports)

```python
import sys
sys.path.append('..') # wherever this package at
from xs_python_lib.json_helper import save_as_json
```

#### or you're sure this module is called in higher level module

```python
from ..xs_python_lib.json_helper import save_as_json
```
