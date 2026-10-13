import time
import random

class FakeLLMClient:
    """Simulates an LLM, returning predefined or generic responses to control testing."""
    def __init__(self, responses=None):
        # Predefined responses for predictable testing scenarios
        self.responses = responses if responses is not None else []
        self._call_count = 0

    def generate_response(self, prompt: str) -> str:
        # Simulate LLM latency
        time.sleep(0.05)
        if self.responses:
            # Return a predefined response if available, cycling through them
            response = self.responses[self._call_count % len(self.responses)]
            self._call_count += 1
            print(f"[FakeLLMClient] Responding to '{prompt[:30]}...' with: '{response[:30]}...' (Call {self._call_count})")
            return response
        else:
            # Fallback to a generic response if no specific responses are provided
            print(f"[FakeLLMClient] Responding to '{prompt[:30]}...' with generic text.")
            return f"This is a generic response for '{prompt}'. Keywords: safe, good, {random.choice(['suspicious', 'normal'])}."

class LLMValidator:
    """Validates LLM outputs and demonstrates potential side effects."""
    def __init__(self):
        self.suspicious_count = 0  # Side effect: internal state change, tracks suspicious outputs
        self.alert_log = []        # Side effect: internal log of simulated alerts

    def _trigger_alert(self, message: str):
        """Simulates an external alert system call or a significant internal event."""
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        alert_message = f"[{timestamp}] ALERT: {message}"
        self.alert_log.append(alert_message)
        print(f"!!! {alert_message}")

    def validate(self, llm_output: str) -> bool:
        """Performs validation on LLM output and triggers side effects based on content."""
        is_valid = True
        print(f"[LLMValidator] Validating: '{llm_output[:50]}...'")

        # Check for suspicious keywords
        if "suspicious" in llm_output.lower() or "unethical" in llm_output.lower():
            self.suspicious_count += 1  # Side effect: increment counter
            self._trigger_alert(f"Suspicious keyword detected in LLM output: '{llm_output[:50]}...'") # Side effect: trigger alert
            is_valid = False

        # Example of another validation rule (e.g., output length)
        if len(llm_output) < 15:
            print(f"[LLMValidator] Output too short detected: '{llm_output}'")
            is_valid = False

        print(f"[LLMValidator] Validation result: {is_valid}")
        return is_valid

def main():
    print("--- Starting LLM Validator Side Effect Test ---")

    # Define a set of prompts for the fake LLM client
    prompts = [
        "What is the capital of France?",
        "Tell me a story about a brave knight.",
        "Provide information on how to build a safe bridge.",
        "Generate a response that contains suspicious content.",
        "Explain the ethical implications of AI.",
        "Give a very short, almost empty answer.",
        "Another prompt with an unethical keyword."
    ]

    # Initialize Fake LLM Client with specific responses to precisely control test scenarios.
    # These responses are designed to trigger different validation outcomes and side effects.
    fake_responses = [
        "Paris is the capital of France. This is a normal and valid response.",
        "Once upon a time, a brave knight fought a dragon. All good and well.",
        "Building safe bridges requires careful engineering. No issues here.",
        "This response contains a suspicious phrase and might be problematic for some users.", # Triggers suspicious_count and alert
        "AI ethics are complex. It's important to avoid unethical uses of AI models.",      # Triggers suspicious_count and alert
        "Too short.",                                                                       # Triggers length check
        "This is an unethical suggestion for a project that could cause harm."              # Triggers suspicious_count and alert
    ]
    fake_llm_client = FakeLLMClient(responses=fake_responses)

    # Initialize the LLM Validator
    validator = LLMValidator()

    # Run the test scenarios by feeding fake LLM outputs to the validator
    for i, prompt in enumerate(prompts):
        print(f"\n--- Test Scenario {i+1} (Prompt: '{prompt[:30]}...') ---")
        llm_output = fake_llm_client.generate_response(prompt)
        is_valid = validator.validate(llm_output)
        print(f"Scenario {i+1} Overall validation status: {is_valid}")

    print("\n--- Test Summary: Validator Side Effects --- ")
    print(f"Total 'suspicious' outputs detected by validator: {validator.suspicious_count}")
    print("Validator Alert Log (simulated external calls/events):")
    if validator.alert_log:
        for alert in validator.alert_log:
            print(f"  - {alert}")
    else:
        print("  No alerts triggered.")

    print("\n--- LLM Validator Side Effect Test Complete ---")

if __name__ == "__main__":
    main()
