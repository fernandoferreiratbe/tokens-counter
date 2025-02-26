import pytest

from src.domain.large_language_model import LargeLanguageModel
from src.infrastructure.open_ai_token_counter import OpenAITokenCounter


def test_given_valid_large_language_model_and_prompt_should_return_tokens_quantity() -> None:
    token_counter = OpenAITokenCounter(large_language_model=LargeLanguageModel.GPT_3_5_TURBO)
    prompt = """You are an software engineering. Write a code to put item into an amazon bucket s3 using Python."""
    # Expected value according to https://platform.openai.com/tokenizer
    expected_value = 21
    token_quantity = token_counter.count_tokens_from(prompt=prompt)

    assert token_quantity == expected_value, "Invalid token quantity"


def test_given_invalid_large_language_model_should_raise_exception() -> None:
    with pytest.raises(AttributeError) as attr_error:
        OpenAITokenCounter(large_language_model=LargeLanguageModel.GPT_3_5_TURB)

    assert str(attr_error.value) == "GPT_3_5_TURB"
