# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from anthropic import Anthropic, AsyncAnthropic
from tests.utils import assert_matches_type
from anthropic._client import Anthropic, AsyncAnthropic
from anthropic.types.beta import Message

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "my-anthropic-api-key"


class TestMessages:
    strict_client = Anthropic(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Anthropic(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create_overload_1(self, client: Anthropic) -> None:
        message = client.beta.messages.create(
            max_tokens=1024,
            messages=[
                {
                    "role": "user",
                    "content": "In one sentence, what is good about the color blue?",
                }
            ],
            model="claude-2.1",
        )
        assert_matches_type(Message, message, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: Anthropic) -> None:
        message = client.beta.messages.create(
            max_tokens=1024,
            messages=[
                {
                    "role": "user",
                    "content": "In one sentence, what is good about the color blue?",
                }
            ],
            model="claude-2.1",
            metadata={"user_id": "13803d75-b4b5-4c3e-b2a2-6f21399b021b"},
            stop_sequences=["string", "string", "string"],
            stream=False,
            system="Today's date is 2024-01-01.",
            temperature=1,
            top_k=5,
            top_p=0.7,
        )
        assert_matches_type(Message, message, path=["response"])

    @parametrize
    def test_raw_response_create_overload_1(self, client: Anthropic) -> None:
        response = client.beta.messages.with_raw_response.create(
            max_tokens=1024,
            messages=[
                {
                    "role": "user",
                    "content": "In one sentence, what is good about the color blue?",
                }
            ],
            model="claude-2.1",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(Message, message, path=["response"])

    @parametrize
    def test_method_create_overload_2(self, client: Anthropic) -> None:
        client.beta.messages.create(
            max_tokens=1024,
            messages=[
                {
                    "role": "user",
                    "content": "In one sentence, what is good about the color blue?",
                }
            ],
            model="claude-2.1",
            stream=True,
        )

    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: Anthropic) -> None:
        client.beta.messages.create(
            max_tokens=1024,
            messages=[
                {
                    "role": "user",
                    "content": "In one sentence, what is good about the color blue?",
                }
            ],
            model="claude-2.1",
            stream=True,
            metadata={"user_id": "13803d75-b4b5-4c3e-b2a2-6f21399b021b"},
            stop_sequences=["string", "string", "string"],
            system="Today's date is 2024-01-01.",
            temperature=1,
            top_k=5,
            top_p=0.7,
        )

    @parametrize
    def test_raw_response_create_overload_2(self, client: Anthropic) -> None:
        response = client.beta.messages.with_raw_response.create(
            max_tokens=1024,
            messages=[
                {
                    "role": "user",
                    "content": "In one sentence, what is good about the color blue?",
                }
            ],
            model="claude-2.1",
            stream=True,
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        response.parse()


class TestAsyncMessages:
    strict_client = AsyncAnthropic(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncAnthropic(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create_overload_1(self, client: AsyncAnthropic) -> None:
        message = await client.beta.messages.create(
            max_tokens=1024,
            messages=[
                {
                    "role": "user",
                    "content": "In one sentence, what is good about the color blue?",
                }
            ],
            model="claude-2.1",
        )
        assert_matches_type(Message, message, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_1(self, client: AsyncAnthropic) -> None:
        message = await client.beta.messages.create(
            max_tokens=1024,
            messages=[
                {
                    "role": "user",
                    "content": "In one sentence, what is good about the color blue?",
                }
            ],
            model="claude-2.1",
            metadata={"user_id": "13803d75-b4b5-4c3e-b2a2-6f21399b021b"},
            stop_sequences=["string", "string", "string"],
            stream=False,
            system="Today's date is 2024-01-01.",
            temperature=1,
            top_k=5,
            top_p=0.7,
        )
        assert_matches_type(Message, message, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_1(self, client: AsyncAnthropic) -> None:
        response = await client.beta.messages.with_raw_response.create(
            max_tokens=1024,
            messages=[
                {
                    "role": "user",
                    "content": "In one sentence, what is good about the color blue?",
                }
            ],
            model="claude-2.1",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(Message, message, path=["response"])

    @parametrize
    async def test_method_create_overload_2(self, client: AsyncAnthropic) -> None:
        await client.beta.messages.create(
            max_tokens=1024,
            messages=[
                {
                    "role": "user",
                    "content": "In one sentence, what is good about the color blue?",
                }
            ],
            model="claude-2.1",
            stream=True,
        )

    @parametrize
    async def test_method_create_with_all_params_overload_2(self, client: AsyncAnthropic) -> None:
        await client.beta.messages.create(
            max_tokens=1024,
            messages=[
                {
                    "role": "user",
                    "content": "In one sentence, what is good about the color blue?",
                }
            ],
            model="claude-2.1",
            stream=True,
            metadata={"user_id": "13803d75-b4b5-4c3e-b2a2-6f21399b021b"},
            stop_sequences=["string", "string", "string"],
            system="Today's date is 2024-01-01.",
            temperature=1,
            top_k=5,
            top_p=0.7,
        )

    @parametrize
    async def test_raw_response_create_overload_2(self, client: AsyncAnthropic) -> None:
        response = await client.beta.messages.with_raw_response.create(
            max_tokens=1024,
            messages=[
                {
                    "role": "user",
                    "content": "In one sentence, what is good about the color blue?",
                }
            ],
            model="claude-2.1",
            stream=True,
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        response.parse()
