Deploy a small Flask API to Kubernetes using a Helm chart with multiple values files (dev / staging / prod).

Flask app (simple API with env-driven greeting, /health and /).

Dockerfile to build local image.

Helm chart flask-api with templates for Deployment, Service, Ingress, ConfigMap, HPA.

values.yaml (defaults) + values-dev.yaml, values-staging.yaml, values-prod.yaml.

Demonstrates switching environment-specific settings (replica count, resources, host, service type, ingress enabled, image tag, feature flags).

Create an IAM Policy using below commands:

aws iam create-role --role-name GitHubActionsOIDCRole --assume-role-policy-document file://trust-policy.json


aws iam put-role-policy \
  --role-name GitHubActionsOIDCRole \
  --policy-name GitHubActionsPolicy \
  --policy-document file://github-actions-policy.json


Create the OpenID Provider for Github Actions;

aws iam create-open-id-connect-provider \
  --url "https://token.actions.githubusercontent.com" \
  --client-id-list "sts.amazonaws.com" \
  --thumbprint-list "6938FD4D98B7C6E3B2AFA2A1A8D7A5DC0B9A1A09"

  Create the config-map at cluster level for access and ensure everything is good.


