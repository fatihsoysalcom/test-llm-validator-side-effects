# Test LLM Validator Side Effects

This example demonstrates how to test the side effects of an LLM validator using a fake LLM client. It features a `FakeLLMClient` that returns controlled responses and an `LLMValidator` that performs checks and logs internal state changes or simulates external alerts as side effects. The script orchestrates a test run, allowing observation of the validator's behavior beyond just returning a boolean validation result.

## Language

`python`

## How to Run

Save the code as `main.py` and run from your terminal:
`python main.py`

## Original Article

This example accompanies the Turkish article: [LLM Doğrulayıcınızın Yan Etkilerini Sahte Model İstemcisiyle Test Etme](https://fatihsoysal.com/blog/llm-dogrulayicinizin-yan-etkilerini-sahte-model-istemcisiyle-test-etme/).

## License

MIT — see [LICENSE](LICENSE).
