# tests for one_word_per_line
import pytest
from pytest_mock import mocker
import sys

sys.path.append('my_module')

# Now you can import your module
from functions import onewordperline, changepreset, gptchat

@pytest.mark.parametrize("input_type, expected_output", [
    ("test", "T i a t "),
    ("example", "H W "),
    ("default", ""),
])

def test_onewordperline(mocker, input_type, expected_output):
    # Mock the gptchat function to return controlled input
    mocker.patch('functions.gptchat', return_value=input_type)
    
    # Call the onewordperline function
    result = onewordperline()
    
    # Check if the result matches the expected output
    assert onewordperline() == expected_output



# Run the tests
if __name__ == '__main__':
    pytest.main()




# def test_onewordperline_default_type(capsys):
#     onewordperline(type='joke')
#     captured = capsys.readouterr()
#     assert captured.out.strip() == "T h i s   i s   a   t e s t   j o k e"

# def test_onewordperline_custom_type(capsys):
#     onewordperline(type='haiku')
#     captured = capsys.readouterr()
#     assert captured.out.strip() == "T h i s   i s   a   t e s t   s t o r y"

# def test_onewordperline_empty_response(capsys):
#     onewordperline(type=None)
#     captured = capsys.readouterr()
#     assert captured.out.strip() == ""


# print(test_onewordperline_empty_input())

preset = None

def test_changepreset_input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'NewPreset')
    changepreset()
    assert preset == 'NewPreset'

def test_changepreset_multiple_inputs(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'AnotherPreset')
    changepreset()
    assert preset == 'AnotherPreset'

def test_changepreset_empty_input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '')
    changepreset()
    assert preset == ''

if __name__ == '__main__':
    pytest.main()
