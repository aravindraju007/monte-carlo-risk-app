import json, random

def lambda_handler(event, context):
    mean = event['mean']
    std = event['std']
    shots = event['shots']
    simulated = [random.gauss(mean, std) for _ in range(shots)]
    simulated.sort(reverse=True)
    return {
        'var95': simulated[int(0.95 * shots)],
        'var99': simulated[int(0.99 * shots)]
    }
