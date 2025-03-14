# evaluation_latency_tokens.py
import time

def simulate_api_call(prompt):
    # Simulate latency and token count (replace with real model API call)
    time.sleep(0.5)  # Simulate network/model latency
    response = f"Simulated response for: {prompt}"
    tokens_used = len(response.split())
    return response, tokens_used

def evaluate_response(prompt):
    start_time = time.time()
    response, tokens = simulate_api_call(prompt)
    latency = time.time() - start_time
    print("Response:", response)
    print("Tokens used:", tokens)
    print("Latency: {:.2f} seconds".format(latency))
    return tokens, latency

# Example usage
if __name__ == "__main__":
    evaluate_response("Explain prompt engineering in simple terms.")
