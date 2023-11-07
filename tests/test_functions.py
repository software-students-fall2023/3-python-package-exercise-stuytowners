import pytest
from unittest.mock import patch
from pytest_mock import mocker
from my_module.functions import onewordperline, changepreset, gptchat, cowtalk
from io import StringIO

# A mock response that mimics the OpenAI API response structure
mock_openai_response = {
    'choices': [
        {'message': {'content': 'mocked response'}}
    ]
}

#test for gptchat
@pytest.fixture
def mock_llm(monkeypatch):
    # This fixture replaces 'llm' with a mock that returns a predefined response
    def mock(*args, **kwargs):
        return mock_openai_response
    monkeypatch.setattr("my_module.functions.llm", mock)

@pytest.mark.parametrize("test_input, expected", [
    (("joke", "computers"), "mocked response"),
    (("joke", None), "mocked response"),
    (("haiku", "spring"), "mocked response"),
    (("haiku", None), "mocked response"),
(("compliment", "music"), "mocked response"),
    (("compliment", None), "mocked response"),
    (("email", "project"), "mocked response"),
    (("email", None), "mocked response"),
    ((None, "a fact"), "mocked response"),
    ((None, None), "mocked response"),])
def test_gptchat(mock_llm, capsys, test_input, expected):
    type_, subject_ = test_input
    # Here, we don't need to patch 'llm' again since it's already patched by the 'mock_llm' fixture
    gptchat(type=type_, subject=subject_)
    captured = capsys.readouterr()  # Capture the print output
    assert expected in captured.out  # Check if the expected string is in the output

@pytest.mark.parametrize("test_input, expected", [
    (("unknown_type", "anything"), "mocked response"),  # Invalid type with subject
    (("unknown_type", None), "mocked response"),  # Invalid type without subject
])
def test_gptchat_invalid_type(mock_llm, capsys, test_input, expected):
    type_, subject_ = test_input
    gptchat(type=type_, subject=subject_)
    captured = capsys.readouterr()  # Capture the print output
    assert expected in captured.out  # Check if the expected string is in the output

@pytest.mark.parametrize("test_input, expected", [
    (("", ""), "mocked response"),  # Empty type and subject
    (("joke", ""), "mocked response"),  # Valid type with empty subject
    (("", "space"), "mocked response"),  # Empty type with valid subject
])
def test_gptchat_empty_strings(mock_llm, capsys, test_input, expected):
    type_, subject_ = test_input
    gptchat(type=type_, subject=subject_)
    captured = capsys.readouterr()  # Capture the print output
    assert expected in captured.out  # Check if the expected string is in the output

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
