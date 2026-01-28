# Renovate-config-validator-action

GitHub Actions for renovate-config-validator, to validate Mintmaker custom configs.

## Input
### `config_file`

required: false

Renovate Configuration file path.
By default, the action fetches `renovate.json` file in the repo.

### `repository_config`

required: false
default: `'true'`

Whether to treat configuration files as repository-level configs (passes `--no-global` to the validator).
Set to `'false'` to validate as global self-hosted configuration.
Defaults to `'true'` for repository-level validation, which is the most common use case.

## Example Workflows

### Repository-level config validation (default)

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
          # repository_config: 'true' is the default
```

### Global self-hosted config validation

```yaml
name: "Validate global renovate config"

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
          config_file: config.js
          repository_config: 'false'  # Treat as global config
```
