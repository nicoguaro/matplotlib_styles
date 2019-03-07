# Matplotlib style sheets

This repository was inspired by a post on [my blog](https://nicoguaro.github.io/posts/matplotlib_styles/) related to
the use of style sheets on Matplotlib.  The main idea is to create a file with
some of the parameters that want to be defined.

## How to use it?
You can use the URL for the style sheet in Python, as the example below.

```python
import numpy as np
import matplotlib.pyplot as plt

repo = "https://github.com/nicoguaro/matplotlib_styles"
style = repo + "/styles/clean.mplstyle"
with plt.style.context(style):
    x = np.linspace(0, 4, 201)
    cos = np.cos(np.pi*x)
    sin = np.sin(np.pi*x)
    plt.plot(x, sin, x, cos)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.savefig("sin_cos-ex.svg")
```

## How to contribute?

If you want to add style sheets to the repository in some of the groups you can
create a Pull Request with the new file under the folder ``styles``.

## License

Style sheets and code are availabe under [MIT license](https://opensource.org/licenses/mit-license.php).
