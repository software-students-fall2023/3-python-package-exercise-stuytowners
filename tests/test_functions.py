import pytest
from unittest.mock import patch
from io import StringIO
from my_module.functions import onewordperline, changepreset, gptchat, cowtalk


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

#Cowtalk test
# Helper function to create the expected 'moo' pattern
def create_moo_pattern(sentence):
    words = sentence.split()
    moo_pattern = []
    for i in range(0, len(words), 3):
        moo_pattern.extend(words[i:i+3])
        moo_pattern.append("moo")
    return " ".join(moo_pattern).strip()

# Test for a regular sentence with multiples of three words
def test_cowtalk_regular_sentence(capsys):
    test_input = "This is a test sentence for the cowtalk function."
    expected_output = create_moo_pattern(test_input) + "\n"
    cowtalk(test_input)
    captured = capsys.readouterr()
    assert captured.out == expected_output

# Test for a sentence with a non-multiple of three words
def test_cowtalk_non_multiple_of_three(capsys):
    test_input = "One two three four five"
    expected_output = create_moo_pattern(test_input) + "\n"
    cowtalk(test_input)
    captured = capsys.readouterr()
    assert captured.out == expected_output

# Test for an empty string
def test_cowtalk_empty_string(capsys):
    test_input = ""
    expected_output = "\n"  # Assuming no "moo" added if there are no words
    cowtalk(test_input)
    captured = capsys.readouterr()
    assert captured.out == expected_output


#Oneword per line check
@pytest.mark.parametrize("input_type, expected_output", [
    ("test", "T i a t "),
    ("example", "H W "),
    ("default", ""),
])
def test_onewordperline(mocker, input_type, expected_output):
    # Mock the gptchat function to return controlled input
    mocker.patch('my_module.functions.gptchat', return_value=input_type)
    
    # Call the onewordperline function
    result = onewordperline()
    
    # Check if the result matches the expected output
    assert result == expected_output

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

#change preset test
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
