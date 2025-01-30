from laravel_queue import LaravelJob

def run_example():
    """
    Example usage with default queue and ap-northeast-1 region
    """
    # Configuration
    queue_url = "http://localhost:4566/000000000000/default"
    region = "ap-northeast-1"
    endpoint = "http://localhost:4566"

    job = (LaravelJob("App\\Jobs\\ExampleJob", {
            "message": "Hello from Python",
            "data": {
                "user_id": 123,
                "action": "test"
            }
        })
        .set_max_tries(3)
        .set_timeout(60)
        .add_tags("example", "test")
    )

    try:
        # Dispatch to SQS
        response = job.dispatch_to_sqs(
            queue_url=queue_url,
            aws_region=region,
            endpoint_url=endpoint
        )
        print("\nJob dispatched successfully!")
        print(f"MessageId: {response.get('MessageId')}")

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    run_example()