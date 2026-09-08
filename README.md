# Repository Coverage

[Full report](https://htmlpreview.github.io/?https://github.com/newtmagalhaes/controle-gastos/blob/ci/actions/py-coverage/htmlcov/index.html)

| Name                                                 |    Stmts |     Miss |   Branch |   BrPart |  Cover |   Missing |
|----------------------------------------------------- | -------: | -------: | -------: | -------: | -----: | --------: |
| apps/core/\_\_init\_\_.py                            |        0 |        0 |        0 |        0 |   100% |           |
| apps/core/admin/\_\_init\_\_.py                      |       23 |       23 |        0 |        0 |     0% |      1-34 |
| apps/core/apps.py                                    |        5 |        5 |        0 |        0 |     0% |       1-7 |
| apps/core/filters/\_\_init\_\_.py                    |        0 |        0 |        0 |        0 |   100% |           |
| apps/core/filters/categoria\_despesas.py             |        7 |        7 |        0 |        0 |     0% |      1-19 |
| apps/core/models/\_\_init\_\_.py                     |        2 |        2 |        0 |        0 |     0% |       2-3 |
| apps/core/models/categoria\_despesa.py               |       13 |       13 |        0 |        0 |     0% |      1-33 |
| apps/core/models/item\_despesa.py                    |       15 |       15 |        0 |        0 |     0% |      1-42 |
| apps/core/templatetags/\_\_init\_\_.py               |        0 |        0 |        0 |        0 |   100% |           |
| apps/core/templatetags/core.py                       |        6 |        6 |        0 |        0 |     0% |       1-9 |
| apps/core/urls.py                                    |        5 |        5 |        0 |        0 |     0% |      1-14 |
| apps/core/views/\_\_init\_\_.py                      |       13 |       13 |        0 |        0 |     0% |      1-18 |
| apps/core/views/categorias\_view.py                  |       10 |       10 |        0 |        0 |     0% |      1-14 |
| apps/core/views/dashboard\_view.py                   |       49 |       49 |        2 |        0 |     0% |      1-91 |
| apps/core/views/despesas\_mensais\_view.py           |       14 |       14 |        0 |        0 |     0% |      1-19 |
| apps/django\_chartjs/\_\_init\_\_.py                 |        0 |        0 |        0 |        0 |   100% |           |
| apps/django\_chartjs/apps.py                         |        4 |        4 |        0 |        0 |     0% |       1-6 |
| apps/django\_chartjs/chartjs.py                      |       24 |       24 |        0 |        0 |     0% |      1-59 |
| apps/django\_chartjs/constants.py                    |        8 |        8 |        0 |        0 |     0% |      1-12 |
| apps/django\_chartjs/templatetags/\_\_init\_\_.py    |        0 |        0 |        0 |        0 |   100% |           |
| apps/django\_chartjs/templatetags/django\_chartjs.py |       10 |       10 |        0 |        0 |     0% |      1-16 |
| apps/django\_chartjs/utils.py                        |        6 |        6 |        0 |        0 |     0% |      1-10 |
| apps/manager/\_\_init\_\_.py                         |        0 |        0 |        0 |        0 |   100% |           |
| apps/manager/admin.py                                |        4 |        4 |        0 |        0 |     0% |       1-6 |
| apps/manager/apps.py                                 |        5 |        5 |        0 |        0 |     0% |       1-7 |
| apps/manager/fields.py                               |       13 |       13 |        0 |        0 |     0% |      1-21 |
| apps/manager/models.py                               |        3 |        3 |        0 |        0 |     0% |       1-7 |
| **TOTAL**                                            |  **239** |  **239** |    **2** |    **0** | **0%** |           |


## Setup coverage badge

Below are examples of the badges you can use in your main branch `README` file.

### Direct image

[![Coverage badge](https://raw.githubusercontent.com/newtmagalhaes/controle-gastos/ci/actions/py-coverage/badge.svg)](https://htmlpreview.github.io/?https://github.com/newtmagalhaes/controle-gastos/blob/ci/actions/py-coverage/htmlcov/index.html)

This is the one to use if your repository is private or if you don't want to customize anything.

### [Shields.io](https://shields.io) Json Endpoint

[![Coverage badge](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/newtmagalhaes/controle-gastos/ci/actions/py-coverage/endpoint.json)](https://htmlpreview.github.io/?https://github.com/newtmagalhaes/controle-gastos/blob/ci/actions/py-coverage/htmlcov/index.html)

Using this one will allow you to [customize](https://shields.io/endpoint) the look of your badge.
It won't work with private repositories. It won't be refreshed more than once per five minutes.

### [Shields.io](https://shields.io) Dynamic Badge

[![Coverage badge](https://img.shields.io/badge/dynamic/json?color=brightgreen&label=coverage&query=%24.message&url=https%3A%2F%2Fraw.githubusercontent.com%2Fnewtmagalhaes%2Fcontrole-gastos%2Fci%2Factions%2Fpy-coverage%2Fendpoint.json)](https://htmlpreview.github.io/?https://github.com/newtmagalhaes/controle-gastos/blob/ci/actions/py-coverage/htmlcov/index.html)

This one will always be the same color. It won't work for private repos. I'm not even sure why we included it.

## What is that?

This branch is part of the
[python-coverage-comment-action](https://github.com/marketplace/actions/python-coverage-comment)
GitHub Action. All the files in this branch are automatically generated and may be
overwritten at any moment.