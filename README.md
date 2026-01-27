# Renovate-config-validator-action

GitHub Actions for renovate-config-validator, to validate MintMaker custom configs with MintMaker's global context.

## Input

### `config_file`

required: false

Renovate Configuration file path.
By default, the action fetches `renovate.json` file in the repo.

### `repository`

required: false  
default: `'konflux-ci/fake-repo'`

Repository name (e.g., 'owner/repo') for MintMaker context.

### `base_branches`

required: false  
default: `'main'`

Comma-separated list of base branches for MintMaker context.

## Example Workflow

```yaml
name: "Validate renovate.json config file"

on:
  push:
    branches: 
      - main
   
jobs:
  renovate-config-file-validation:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: konflux-ci/renovate-config-validator-action@main
        with:
          config_file: test/renovate.json
```

## MintMaker Compatibility

This action now validates configurations with MintMaker's global context, allowing `matchBaseBranches` rules to work correctly:

```json
{
  "packageRules": [
    {
      "matchBaseBranches": ["main"],
      "matchPackageNames": ["/^quay.io/konflux-ci//"],
      "automerge": true
    }
  ]
}
```