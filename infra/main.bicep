@description('Name of the static web app')
param staticWebAppName string = 'ux4iot-docs'

@description('Location for the static web app')
param location string = 'westeurope'

@description('Custom domain name')
param customDomain string = 'docs.ux4iot.com'

resource staticWebApp 'Microsoft.Web/staticSites@2023-01-01' = {
  name: staticWebAppName
  location: location
  sku: {
    name: 'Free'
    tier: 'Free'
  }
  properties: {
    repositoryUrl: ''
    branch: ''
    buildProperties: {
      skipGithubActionWorkflowGeneration: true
    }
    stagingEnvironmentPolicy: 'Enabled'
    allowConfigFileUpdates: true
  }
}

resource customDomainResource 'Microsoft.Web/staticSites/customDomains@2023-01-01' = {
  parent: staticWebApp
  name: customDomain
  properties: {}
}

@description('Static Web App hostname')
output staticWebAppHostname string = staticWebApp.properties.defaultHostname

@description('Static Web App ID')
output staticWebAppId string = staticWebApp.id

@description('Static Web App name')
output staticWebAppName string = staticWebApp.name

