Deploy a small Flask API to Kubernetes using a Helm chart with multiple values files (dev / staging / prod).

Flask app (simple API with env-driven greeting, /health and /).

Dockerfile to build local image.

Helm chart flask-api with templates for Deployment, Service, Ingress, ConfigMap, HPA.

values.yaml (defaults) + values-dev.yaml, values-staging.yaml, values-prod.yaml.

Demonstrates switching environment-specific settings (replica count, resources, host, service type, ingress enabled, image tag, feature flags).