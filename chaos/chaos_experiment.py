from chaoslib.experiment import run_experiment
from chaoslib.settings import load_settings

settings = load_settings()
experiment = {
    \"title\": \"Terminate a webserver\",
    \"description\": \"Terminate a webserver and check if the system recovers\",
    \"steady-state-hypothesis\": {
        \"title\": \"Webserver is healthy\",
        \"probes\": [
            {
                \"type\": \"probe\",
                \"name\": \"webserver_is_healthy\",
                \"tolerance\": 200,
                \"provider\": {
                    \"type\": \"http\",
                    \"timeout\": 5,
                    \"verify_tls\": False,
                    \"url\": \"http://example.com/health\"
                }
            }
        ]
    },
    \"method\": [
        {
            \"type\": \"action\",
            \"name\": \"terminate_webserver\",
            \"provider\": {
                \"type\": \"aws\",
                \"secrets\": [\"aws\"],
                \"action\": \"terminate_instance\",
                \"arguments\": {
                    \"instance_id\": \"i-1234567890abcdef0\"
                }
            }
        }
    ]
}

run_experiment(experiment)
