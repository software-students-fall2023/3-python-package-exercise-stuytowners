import pytest
from unittest.mock import patch
from my_module.functions import gptchat  

# A mock response that mimics the OpenAI API response structure
mock_openai_response = {
    'choices': [
        {'message': {'content': 'mocked response'}}
    ]
}

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


