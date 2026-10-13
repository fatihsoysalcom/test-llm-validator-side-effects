# test-llm-validator-side-effects
This example demonstrates how to test the side effects of an LLM validator using a fake LLM client. It features a `FakeLLMClient` that returns controlled responses and an `LLMValidator` that performs checks and logs internal state changes or simulates external alerts as side effects. The script orchestrates a test run, allowing observation of the v
