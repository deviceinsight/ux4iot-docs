#!/bin/bash

set -e

SUBSCRIPTION_ID=ab92703c-7fdb-4a1e-8ea8-b402f4e2ea25
RG_NAME="ux4iot-shared"
SWA_NAME="ux4iot-docs"
LOCATION="westeurope"

az deployment group create \
  --resource-group $RG_NAME \
  --subscription $SUBSCRIPTION_ID \
  --parameters infra/main.bicepparam

TOKEN=$(az staticwebapp secrets list --name $SWA_NAME --resource-group $RG_NAME --subscription $SUBSCRIPTION_ID --query "properties.apiKey" -o tsv)
npm install -g @azure/static-web-apps-cli 2>/dev/null || true
swa deploy ./site --deployment-token $TOKEN --env production
