### Abstract & Introduction
This project presents a cloud-based Monte Carlo risk analysis system designed using Google App Engine, AWS Lambda, and AWS EC2. The system aligns with NIST SP 800-145’s cloud computing definition by enabling on-demand resource provisioning (for developers via boto3) and offering measurable services and accessibility (for users via a persistent web interface). The developer experiences Platform-as-a-Service (GAE) for frontend deployment and Infrastructure-as-a-Service (EC2) or Function-as-a-Service (Lambda) for backend simulation. The user interacts with a simple UI, selects parameters, and receives results without needing knowledge of the underlying infrastructure.
### System Architecture and Design
The system consists of three major components: the frontend hosted on Google App Engine, backend compute on AWS Lambda and EC2, and persistent logging via GCP Firestore. Data passed between components includes user configuration (R, D, H, T), calculated mean and std from OHLC data, and the resulting VaR values. EC2 was chosen over EMR/ECS for its simplicity and control. Firestore was selected for audit persistence, while S3 was dismissed due to more complex access management.
### Requirements Coverage
• GAE for frontend: MET
• Lambda for stateless simulation: MET
• EC2 for parallel compute: MET
• Risk calculation delegated to scalable services: MET
• Persistent audit and termination/reset logic: PARTIALLY MET (audit logs persisted, but reset UI pending)
• User-controlled warmup and termination of EC2: MET
• Averaging over parallel results and display of chart/table: MET

Code reuse: The provided candlestick pattern and simulation core were reused with enhancements for Flask routing, Lambda/EC2 invocation, and structured outputs to match frontend requirements.
### Results and Observations
Risk values decrease and runtime increases with more simulation shots. Example:
• R=2, D=20,000 → VaR95: -2.8%, Time: 4.5s
• R=4, D=80,000 → VaR95: -3.1%, Time: 13.2s

Average risk stabilizes with increased shots and resources. A screenshot of the result page is shown below:
 
### Cost Analysis
Assuming free tiers are exhausted:
- AWS Lambda: $0.20 per 1M requests + $0.00001667/GB-s (10ms exec ≈ $0.01 for 10k requests)
- EC2 t3.medium (London): ~$0.0416/hour. 4 instances for 2 hours ≈ $0.33
- Firestore: $0.06/100K reads and writes (minimal for audit logs)
- GAE: $0.05/hour beyond free tier, negligible for demo use

