# What is pytest ?
- pytest is a testing framework for Python that makes it easy to write simple as well as scalable test cases. It is designed to support both unit tests and functional tests, providing a rich set of features to help developers ensure their code works as expected.
- pytest allows you to write test cases using simple assert statements, making it easy to understand and maintain tests.
- It supports fixtures, which are functions that can set up some context for your tests, such as creating test data or initializing resources.


Example:
```python
def test_addition():
    assert 1 + 1 == 2
def test_subtraction():
    assert 2 - 1 == 1
def test_multiplication():
    assert 2 * 3 == 6
def test_division():
    assert 6 / 2 == 3
def test_exponentiation():
    assert 2 ** 3 == 8
def test_modulus():
    assert 5 % 2 == 1
def test_floor_division():
    assert 5 // 2 == 2
def test_string_concatenation():
    assert "Hello, " + "World!" == "Hello, World!"
def test_list_append():
    my_list = []
    my_list.append(1)
    assert my_list == [1]
def test_dictionary_key():
    my_dict = {'a': 1, 'b': 2}
    assert my_dict['a'] == 1
def test_set_membership():
    my_set = {1, 2, 3}
    assert 2 in my_set
```
- pytest provides powerful command-line options to run tests selectively, generate reports, and control the verbosity of test output.
- It integrates well with other tools and libraries, making it a popular choice for testing in the Python ecosystem.


# how to install pytest  and create python environment ?
- To install pytest, you can use pip, the package installer for Python. Open your terminal or command prompt and run the following command:
```bash
pip install pytest
```
- If you want to create a virtual environment for your Python project, you can use the following commands:
```bash
python -m venv myenv
source myenv/bin/activate  # On Windows, use: myenv\Scripts\activate    
```
- After activating the virtual environment, you can install pytest within that environment:
```bash
pip install pytest
```